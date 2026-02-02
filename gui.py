import copy
import random as rand
import cv2
import cube
import twophase.solver as solver
import tkinter as tk
import enums
from tkinter import font
import vision
import vision_params


class Gui:
    def __init__(self):
        self.square_size = 55
        self.canvas_size = {"width": 950, "height": 600}
        self.font_size = 8
        self.button_size = {"width": self.font_size*10, "height": self.font_size*6}

        self.root = tk.Tk()
        self.root.wm_title("Kostka_GUI")
        my_font = font.nametofont("TkDefaultFont")
        my_font.configure(size=self.font_size)
        self.canvas = tk.Canvas(self.root, width=self.canvas_size["width"], height=self.canvas_size["height"])

        self.text_box = None
        self.camera = cv2.VideoCapture(0) # 0 - Webcam, 2 - intel RGB
        self.camera_flag = False
        self.camera_bin_flag = False

        self.kostka = cube.Cube()
        self.kostka_squares = [[[0 for col in range(3)] for row in range(3)] for face in range(6)]

    def start(self):
        self.create_buttons_main()
        self.create_buttons_moves()
        self.create_textbox()
        self.create_cube_view()
        self.create_vision_sliders()
        self.canvas.pack()
        self.root.mainloop()

    def create_buttons_main(self):
        but_get_sol = tk.Button(self.root, text="Get Solution", height=2, width=10, command=self.get_solution)
        self.canvas.create_window(10, 10, anchor=tk.NW, window=but_get_sol)

        but_sol = tk.Button(self.root, text="Solve", height=2, width=10, command=self.solve)
        self.canvas.create_window(10, 10 + self.button_size["height"], anchor=tk.NW, window=but_sol)

        but_clear = tk.Button(self.root, text="Clear", height=2, width=10, command=self.clear_cube)
        self.canvas.create_window(10 + self.button_size["width"], 10, anchor=tk.NW, window=but_clear)

        but_rand = tk.Button(self.root, text="Scramble", height=2, width=10, command=self.scramble)
        self.canvas.create_window(10 + self.button_size["width"], 10 + self.button_size["height"], anchor=tk.NW,
                                  window=but_rand)

        but_start_camera = tk.Button(self.root, text="Start camera", height=2, width=20, command=self.start_camera)
        self.canvas.create_window(10, 10 + 7 * self.button_size["height"], anchor=tk.NW, window=but_start_camera)

        but_stop_camera = tk.Button(self.root, text="Stop camera", height=2, width=20, command=self.stop_camera)
        self.canvas.create_window(10, 10 + 8 * self.button_size["height"], anchor=tk.NW, window=but_stop_camera)

        but_camera_bin = tk.Button(self.root, text="Binary camera view", height=2, width=20, command=self.show_binarized)
        self.canvas.create_window(10, 10 + 9 * self.button_size["height"], anchor=tk.NW, window=but_camera_bin)

    def create_buttons_moves(self):
        b_move_U = tk.Button(text="U", height=1, width=10, command=lambda: self.make_move("U"))
        self.canvas.create_window(20 + 6 * self.square_size, 10 + 7 * self.button_size["height"], anchor=tk.NW,
                                  window=b_move_U)

        b_move_L = tk.Button(text="L", height=1, width=10, command=lambda: self.make_move("L"))
        self.canvas.create_window(20 + 6 * self.square_size, 10 + 7.5 * self.button_size["height"], anchor=tk.NW,
                                  window=b_move_L)

        b_move_F = tk.Button(text="F", height=1, width=10, command=lambda: self.make_move("F"))
        self.canvas.create_window(20 + 6 * self.square_size, 10 + 8 * self.button_size["height"], anchor=tk.NW,
                                  window=b_move_F)

        b_move_R = tk.Button(text="R", height=1, width=10, command=lambda: self.make_move("R"))
        self.canvas.create_window(20 + 6 * self.square_size, 10 + 8.5 * self.button_size["height"], anchor=tk.NW,
                                  window=b_move_R)

        b_move_B = tk.Button(text="B", height=1, width=10, command=lambda: self.make_move("B"))
        self.canvas.create_window(20 + 6 * self.square_size, 10 + 9 * self.button_size["height"], anchor=tk.NW,
                                  window=b_move_B)

        b_move_D = tk.Button(text="D", height=1, width=10, command=lambda: self.make_move("D"))
        self.canvas.create_window(20 + 6 * self.square_size, 10 + 9.5 * self.button_size["height"], anchor=tk.NW,
                                  window=b_move_D)

        b_move_U2 = tk.Button(text="U2", height=1, width=10, command=lambda: self.make_move("U2"))
        self.canvas.create_window(20 + 6 * self.square_size + self.button_size["width"],
                                  10 + 7 * self.button_size["height"], anchor=tk.NW, window=b_move_U2)

        b_move_L2 = tk.Button(text="L2", height=1, width=10, command=lambda: self.make_move("L2"))
        self.canvas.create_window(20 + 6 * self.square_size + self.button_size["width"],
                                  10 + 7.5 * self.button_size["height"], anchor=tk.NW, window=b_move_L2)

        b_move_F2 = tk.Button(text="F2", height=1, width=10, command=lambda: self.make_move("F2"))
        self.canvas.create_window(20 + 6 * self.square_size + self.button_size["width"],
                                  10 + 8 * self.button_size["height"], anchor=tk.NW, window=b_move_F2)

        b_move_R2 = tk.Button(text="R2", height=1, width=10, command=lambda: self.make_move("R2"))
        self.canvas.create_window(20 + 6 * self.square_size + self.button_size["width"],
                                  10 + 8.5 * self.button_size["height"], anchor=tk.NW, window=b_move_R2)

        b_move_B2 = tk.Button(text="B2", height=1, width=10, command=lambda: self.make_move("B2"))
        self.canvas.create_window(20 + 6 * self.square_size + self.button_size["width"],
                                  10 + 9 * self.button_size["height"], anchor=tk.NW, window=b_move_B2)

        b_move_D2 = tk.Button(text="D2", height=1, width=10, command=lambda: self.make_move("D2"))
        self.canvas.create_window(20 + 6 * self.square_size + self.button_size["width"],
                                  10 + 9.5 * self.button_size["height"], anchor=tk.NW, window=b_move_D2)

        b_move_U3 = tk.Button(text="U3/U'", height=1, width=10, command=lambda: self.make_move("U3"))
        self.canvas.create_window(20 + 6 * self.square_size + 2 * self.button_size["width"],
                                  10 + 7 * self.button_size["height"], anchor=tk.NW, window=b_move_U3)

        b_move_L3 = tk.Button(text="L3/L'", height=1, width=10, command=lambda: self.make_move("L3"))
        self.canvas.create_window(20 + 6 * self.square_size + 2 * self.button_size["width"],
                                  10 + 7.5 * self.button_size["height"], anchor=tk.NW, window=b_move_L3)

        b_move_F3 = tk.Button(text="F3/F'", height=1, width=10, command=lambda: self.make_move("F3"))
        self.canvas.create_window(20 + 6 * self.square_size + 2 * self.button_size["width"],
                                  10 + 8 * self.button_size["height"], anchor=tk.NW, window=b_move_F3)

        b_move_R3 = tk.Button(text="R3/R'", height=1, width=10, command=lambda: self.make_move("R3"))
        self.canvas.create_window(20 + 6 * self.square_size + 2 * self.button_size["width"],
                                  10 + 8.5 * self.button_size["height"], anchor=tk.NW, window=b_move_R3)

        b_move_B3 = tk.Button(text="B3/B'", height=1, width=10, command=lambda: self.make_move("B3"))
        self.canvas.create_window(20 + 6 * self.square_size + 2 * self.button_size["width"],
                                  10 + 9 * self.button_size["height"], anchor=tk.NW, window=b_move_B3)

        b_move_D3 = tk.Button(text="D3/D'", height=1, width=10, command=lambda: self.make_move("D3"))
        self.canvas.create_window(20 + 6 * self.square_size + 2 * self.button_size["width"],
                                  10 + 9.5 * self.button_size["height"], anchor=tk.NW, window=b_move_D3)

    def create_textbox(self):
        text_width = 70
        text_height = 8
        self.text_box = tk.Text(self.canvas, height=text_height, width=text_width)
        self.text_box['state'] = tk.DISABLED
        self.canvas.create_window(self.canvas_size["width"] - self.font_size * text_width - 10, 10, anchor=tk.NW, window=self.text_box)

    def create_cube_view(self):
        offsets = [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)]
        for face in range(6):
            for row in range(3):
                x = (row + offsets[face][1] * 3) * self.square_size + 10
                for col in range(3):
                    y = (col + offsets[face][0] * 3) * self.square_size + 10
                    self.kostka_squares[face][col][row] = self.canvas.create_rectangle(x, y, x + self.square_size, y + self.square_size, fill="gray")
                    if [row, col] == [1, 1]:
                        self.canvas.create_text(x + self.square_size // 2, y + self.square_size // 2, font=("", 14), text=str(enums.Face(face)), state=tk.DISABLED)

    def create_vision_sliders(self):
        slider_blur = tk.Scale(self.canvas, from_=0, to=10, orient=tk.HORIZONTAL, label="BlurLevel",
                               command = lambda val: self.update_param("GAUSSIAN_BLUR", val))
        slider_blur.set(vision_params.get("GAUSSIAN_BLUR"))
        self.canvas.create_window(20 + 12 * self.square_size, 10 + 3 * self.square_size, anchor=tk.NW,
                                  window=slider_blur)

        slider_thr = tk.Scale(self.canvas, from_=0, to=255, orient=tk.HORIZONTAL, label="BinThreshold",
                               command = lambda val: self.update_param("BLACK_TRH", val))
        slider_thr.set(vision_params.get("BLACK_TRH"))
        self.canvas.create_window(20 + 12 * self.square_size, 10 + 4 * self.square_size, anchor=tk.NW,
                                  window=slider_thr)

        slider_size_min = tk.Scale(self.canvas, from_=0, to=100, orient=tk.HORIZONTAL, label="SquaresMin",
                               command = lambda val: self.update_param("MIN_SQUARE_SIZE", val))
        slider_size_min.set(vision_params.get("MIN_SQUARE_SIZE"))
        self.canvas.create_window(20 + 12 * self.square_size, 10 + 5 * self.square_size, anchor=tk.NW,
                                  window=slider_size_min)

        slider_size_max = tk.Scale(self.canvas, from_=0, to=200, orient=tk.HORIZONTAL, label="SquaresMax",
                              command = lambda val: self.update_param("MAX_SQUARE_SIZE", val))
        slider_size_max.set(vision_params.get("MAX_SQUARE_SIZE"))
        self.canvas.create_window(20 + 12 * self.square_size, 10 + 6 * self.square_size, anchor=tk.NW,
                                  window=slider_size_max)

    def update_cube(self):
        s = self.kostka.get_string()
        i = 0
        for face in range(6):
            for row in range(3):
                for col in range(3):
                    self.canvas.itemconfig(self.kostka_squares[face][row][col], fill=str(enums.Color(enums.to_Face(s[i]))))
                    i += 1

    def clear_cube(self):
        self.kostka.clear()
        self.update_cube()

    def write_text(self, text):
        self.text_box['state'] = tk.NORMAL
        self.text_box.insert(tk.END, text + "\n")
        self.text_box.see(tk.END)
        self.text_box['state'] = tk.DISABLED

    def get_solution(self):
        s = cube.convert_strings(self.kostka.get_string(), False)
        solution = solver.solve(s)
        self.write_text("Cube string:")
        self.write_text(s)
        self.write_text("Solution:")
        self.write_text(solution)
        return solution

    def solve(self):
        solution = self.get_solution()
        solution = solution.split(" ")
        solution.pop()
        if solution:
            self.make_moves((len(solution), solution))

    def make_moves(self, args):
        (i, solution) = args
        if i == 0:
            return
        self.kostka.make_move(solution.pop(0))
        self.update_cube()
        self.root.after(1000, self.make_moves, (i - 1, solution))

    def make_move(self, move):
        self.kostka.make_move(move)
        self.update_cube()

    def scramble(self):
        self.kostka.clear()
        moves = []
        length = 15
        moves_base = ["U", "R", "F", "D", "L", "B"]
        last_move = ""

        for i in range(length):
            moves_vec = copy.deepcopy(moves_base)
            if i != 0:
                moves_vec.remove(last_move)

            move_index = rand.randint(0, len(moves_vec)-1)
            n = rand.randint(1, 3)

            last_move = moves_vec[move_index]
            moves.append(moves_vec[move_index] + str(n))

        self.write_text("Scramble:")
        moves_str = " ".join(moves)
        self.write_text(moves_str)

        for move in moves:
            self.kostka.make_move(move)
        self.update_cube()

    def start_camera(self):
        self.camera_flag = True
        self.update_camera()

    def update_camera(self):
        if self.camera_flag is False:
            cv2.destroyAllWindows()
            return
        face_colors = vision.detect_cube(self.camera, self.camera_bin_flag)
        self.root.after(20, self.update_camera)

    def stop_camera(self):
        self.camera_flag = False

    def show_binarized(self):
        self.camera_bin_flag = not self.camera_bin_flag

    def update_param(self, param_name, val):
        vision_params.set(param_name, float(val))
