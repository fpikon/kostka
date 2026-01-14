import twophase.solver  as sv
from twophase.face import FaceCube
from face_kostka import *
from tkinter import *

def start_gui():
    cube = FaceKostka()
    width = 60  # width of a facelet in pixels
    facelet_id = [[[0 for col in range(3)] for row in range(3)] for face in range(6)]
    colorpick_id = [0 for i in range(6)]
    curcol = None
    t = ("U", "R", "F", "D", "L", "B")
    cols = ("yellow", "green", "red", "white", "blue", "orange")
    colors = {"U": "white",
              "L": "green",
              "F": "red",
              "R": "blue",
              "B": "orange",
              "D": "yellow"}


    def solve():
        s = convert_strings(cube.get_string(), False)
        show_text("Cube string:")
        show_text(s)
        solution = sv.solve(s, 20, 5).split(" ")
        show_text("Solution:")
        for move in solution:
            show_text(move)
        return solution


    def clean():
        cube = FaceKostka()
        update_facelet_rects()


    def show_text(txt):
        """Display messages."""
        print(txt)
        display.insert(INSERT, txt + "\n")
        root.update_idletasks()

    def create_facelet_rects(a):
        offset = ((1, 0), (2, 1), (1, 1), (1, 2), (0, 1), (3, 1))
        for f in range(6):
            for row in range(3):
                y = 10 + offset[f][1] * 3 * a + row * a
                for col in range(3):
                    x = 10 + offset[f][0] * 3 * a + col * a
                    facelet_id[f][row][col] = canvas.create_rectangle(x, y, x + a, y + a, fill="grey")
                    if row == 1 and col == 1:
                        canvas.create_text(x + width // 2, y + width // 2, font=("", 14), text=t[f], state=DISABLED)
        for f in range(6):
            canvas.itemconfig(facelet_id[f][1][1], fill=cols[f])
        clean()

    def update_facelet_rects():
        s = convert_strings(cube.get_string(), False)
        i = 0
        for f in range(6):
            for row in range(3):
                for col in range(3):
                    canvas.itemconfig(facelet_id[f][row][col], fill=colors[s[i]])
                    i += 1


    def move_U():
        cube.make_move("U")
        update_facelet_rects()
    def move_L():
        cube.make_move("L")
        update_facelet_rects()
    def move_F():
        cube.make_move("F")
        update_facelet_rects()
    def move_R():
        cube.make_move("R")
        update_facelet_rects()
    def move_B():
        cube.make_move("B")
        update_facelet_rects()
    def move_D():
        cube.make_move("D")
        update_facelet_rects()

    root = Tk()
    root.wm_title("Solver Client")
    canvas = Canvas(root, width=12 * width + 20, height=9.5 * width + 20)
    canvas.pack()

    # buttons
    bsolve = Button(text="Solve", height=2, width=10, relief=RAISED, command=solve)
    bsolve_window = canvas.create_window(10, 10 + 6.5 * width, anchor=NW, window=bsolve)
    bclean = Button(text="Clean", height=1, width=10, relief=RAISED, command=clean)
    bclean_window = canvas.create_window(10, 10 + 7.5 * width, anchor=NW, window=bclean)

    # move buttons
    bmoveU = Button(text="U", height=1, width=5, relief=RAISED, command=move_U)
    bmoveU_window = canvas.create_window(10 + 6.5 * width, 6.5 * width, anchor=NW, window=bmoveU)
    bmoveL = Button(text="L", height=1, width=5, relief=RAISED, command=move_L)
    bmoveL_window = canvas.create_window(10 + 6.5 * width, 7 * width, anchor=NW, window=bmoveL)
    bmoveF = Button(text="F", height=1, width=5, relief=RAISED, command=move_F)
    bmoveF_window = canvas.create_window(10 + 6.5 * width, 7.5 * width, anchor=NW, window=bmoveF)
    bmoveR = Button(text="R", height=1, width=5, relief=RAISED, command=move_R)
    bmoveR_window = canvas.create_window(10 + 6.5 * width, 8 * width, anchor=NW, window=bmoveR)
    bmoveB = Button(text="B", height=1, width=5, relief=RAISED, command=move_B)
    bmoveB_window = canvas.create_window(10 + 6.5 * width, 8.5 * width, anchor=NW, window=bmoveB)
    bmoveD = Button(text="D", height=1, width=5, relief=RAISED, command=move_D)
    bmoveD_window = canvas.create_window(10 + 6.5 * width, 9 * width, anchor=NW, window=bmoveD)

    # display and text_window
    display = Text(height=7, width=39)
    text_window = canvas.create_window(10 + 6.5 * width, 10 + .5 * width, anchor=NW, window=display)
    create_facelet_rects(width)
    update_facelet_rects()

    root.mainloop()