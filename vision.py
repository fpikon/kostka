import cv2
import numpy as np
import vision_params
import enums


def find_squares(image):
    size = image.shape[:2]

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    v_bin = cv2.threshold(v, vision_params.BLACK_TRH, 255, cv2.THRESH_BINARY)[1]

    contours, _ = cv2.findContours(v_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    squares = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 1000:
            continue
        if area > 10000:
            continue

        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)

        if len(approx) == 4:
            squares.append(approx)

    return v_bin, squares

def get_center(square):
    x, y, w, h = cv2.boundingRect(square)
    return x + w // 2, y + h // 2

def sort_squares_robust(squares, rows=3):
    # Get centers
    centers = [(sq, get_center(sq)) for sq in squares]

    # Sort by Y first
    centers.sort(key=lambda x: x[1][1])

    # Estimate row height
    y_values = [c[1][1] for c in centers]
    row_height = (max(y_values) - min(y_values)) / (rows - 1)

    rows_list = [[] for _ in range(rows)]

    for sq, (cx, cy) in centers:
        row_idx = int(round((cy - min(y_values)) / row_height))
        row_idx = max(0, min(rows - 1, row_idx))
        rows_list[row_idx].append((sq, cx))

    # Sort each row by X
    sorted_squares = []
    for row in rows_list:
        row.sort(key=lambda x: x[1])
        sorted_squares.extend([sq for sq, _ in row])

    return sorted_squares

def detect_color(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    max_pixels = 0
    detected_color = enums.Color.Undetected

    for color, (lower, upper) in vision_params.COLOR_RANGES.items():
        mask = cv2.inRange(hsv, lower, upper)
        count = cv2.countNonZero(mask)

        if count > max_pixels:
            max_pixels = count
            detected_color = color

    return detected_color

def detect_cube(camera):
    ret, frame = camera.read()
    frame_size = frame.shape[:2]

    black_mask = np.zeros(frame_size, dtype=np.uint8)
    white_mask = np.zeros(frame_size, dtype=np.uint8)
    color_mask = np.zeros(frame_size, dtype=np.uint8)

    detected_colors = np.zeros((3, 3), dtype=np.uint8) * vision_params.Color.Undetected

    # blur
    frame_blur = cv2.GaussianBlur(frame, (5, 5), vision_params.GAUSSIAN_BLUR)

    bin, squares = find_squares(frame_blur)

    if len(squares) == 9:
        squares = sort_squares_robust(squares)
        i = 0
        for square in squares:
            row = i // 3
            col = i % 3
            x, y, w, h = cv2.boundingRect(square)

            pad = 5
            croped_square = frame_blur[y + pad:y + h - pad, x + pad:x + w - pad]

            detected_color = detect_color(croped_square)
            detected_colors[row, col] = detected_color
            cv2.putText(frame, f"{(row, col)}" + str(detected_color), (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.3,
                        (0, 0, 255), 1)
            i += 1


    cv2.drawContours(frame, squares, -1, (0, 0, 255), 1)

    cv2.imshow('camera', frame)

    return detected_colors