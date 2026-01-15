import cv2
import numpy as np
import kamera_params
import enums
from enums import str_ColorCamera


def find_squares(image):
    size = image.shape[:2]

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    v_bin = cv2.threshold(v, kamera_params.BLACK_TRH, 255, cv2.THRESH_BINARY)[1]

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

def square_center(square):
    x, y, w, h = cv2.boundingRect(square)
    return y, x

def detect_color(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    max_pixels = 0
    detected_color = enums.ColorCamera.Undetected

    for color, (lower, upper) in kamera_params.COLOR_RANGES.items():
        mask = cv2.inRange(hsv, lower, upper)
        count = cv2.countNonZero(mask)

        if count > max_pixels:
            max_pixels = count
            detected_color = color

    return detected_color

def get_image(camera):
    ret, frame = camera.read()
    frame_size = frame.shape[:2]

    black_mask = np.zeros(frame_size, dtype=np.uint8)
    white_mask = np.zeros(frame_size, dtype=np.uint8)
    color_mask = np.zeros(frame_size, dtype=np.uint8)

    detected_colors = np.zeros((3, 3), dtype=np.uint8)

    ret, frame = camera.read()

    # blur
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(frame_hsv)

    bin, squares = find_squares(frame)

    squares = sorted(squares, key=square_center)

    if len(squares) == 9:
        i = 0
        for square in squares:
            x, y, w, h = cv2.boundingRect(square)

            pad = 5
            croped_square = frame[y + pad:y + h - pad, x + pad:x + w - pad]

            detected_color = detect_color(croped_square)
            detected_colors[i // 3, i % 3] = detected_color

            i += 1
            cv2.putText(frame, str_ColorCamera(detected_color), (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 0, 255), 1)

    cv2.drawContours(frame, squares, -1, (0, 0, 255), 1)

    cv2.imshow('camera', frame)

    return detected_colors