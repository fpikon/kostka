import twophase.solver  as sv
from face_kostka import *
from tkinter import *

def start_gui():
    cube = FaceKostka()
    width = 60  # width of a facelet in pixels
    facelet_id = [[[0 for col in range(3)] for row in range(3)] for face in range(6)]
    t = ("U", "R", "F", "D", "L", "B")
    cols = ("yellow", "green", "red", "white", "blue", "orange")
    colors = {"U": "white",
              "L": "green",
              "F": "red",
              "R": "blue",
              "B": "orange",
              "D": "yellow"}

    def get_solution():
        s = convert_strings(cube.get_string(), False)
        show_text("Cube string:")
        show_text(s)
        solution = sv.solve(s, 20, 5).split(" ")
        show_text("Solution:")
        for move in solution:
            show_text(move)
        return solution


    def solve():
        solution = get_solution()
        perform_moves((0, solution))

    def perform_moves(args):
        i = args[0]
        solution = args[1]
        if i >= len(solution):
            return

        cube.make_move(solution[i])
        update_facelet_rects()

        root.after(1000, perform_moves, (i + 1, solution))

    def clean():
        cube.clear()
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

    def move_U2():
        cube.make_move("U2")
        update_facelet_rects()
    def move_L2():
        cube.make_move("L2")
        update_facelet_rects()
    def move_F2():
        cube.make_move("F2")
        update_facelet_rects()
    def move_R2():
        cube.make_move("R2")
        update_facelet_rects()
    def move_B2():
        cube.make_move("B2")
        update_facelet_rects()
    def move_D2():
        cube.make_move("D2")
        update_facelet_rects()

    def move_U3():
        cube.make_move("U3")
        update_facelet_rects()
    def move_L3():
        cube.make_move("L3")
        update_facelet_rects()
    def move_F3():
        cube.make_move("F3")
        update_facelet_rects()
    def move_R3():
        cube.make_move("R3")
        update_facelet_rects()
    def move_B3():
        cube.make_move("B3")
        update_facelet_rects()
    def move_D3():
        cube.make_move("D3")
        update_facelet_rects()

    def move_x():
        cube.make_move("x")
        update_facelet_rects()

    def move_y():
        cube.make_move("y")
        update_facelet_rects()

    def move_z():
        cube.make_move("z")
        update_facelet_rects()

    root = Tk()
    root.wm_title("Kostka_symulacja_solver")
    canvas = Canvas(root, width=12 * width + 20, height=9.5 * width + 20)
    canvas.pack()

    # buttons
    bgetsolve = Button(text="Get solution", height=2, width=10, relief=RAISED, command=get_solution)
    bsolve_window = canvas.create_window(10, 10 + 6.5 * width, anchor=NW, window=bgetsolve)
    bsolve = Button(text="Solve", height=2, width=10, relief=RAISED, command=solve)
    bsolve_window = canvas.create_window(10, 10 + 7.5 * width, anchor=NW, window=bsolve)
    bclean = Button(text="Clean", height=1, width=10, relief=RAISED, command=clean)
    bclean_window = canvas.create_window(10, 10 + 8.5 * width, anchor=NW, window=bclean)

    # move buttons
    bmoveU = Button(text="U", height=1, width=10, relief=RAISED, command=move_U)
    bmoveU_window = canvas.create_window(10 + 6.5 * width, 6.5 * width, anchor=NW, window=bmoveU)
    bmoveL = Button(text="L", height=1, width=10, relief=RAISED, command=move_L)
    bmoveL_window = canvas.create_window(10 + 6.5 * width, 7 * width, anchor=NW, window=bmoveL)
    bmoveF = Button(text="F", height=1, width=10, relief=RAISED, command=move_F)
    bmoveF_window = canvas.create_window(10 + 6.5 * width, 7.5 * width, anchor=NW, window=bmoveF)
    bmoveR = Button(text="R", height=1, width=10, relief=RAISED, command=move_R)
    bmoveR_window = canvas.create_window(10 + 6.5 * width, 8 * width, anchor=NW, window=bmoveR)
    bmoveB = Button(text="B", height=1, width=10, relief=RAISED, command=move_B)
    bmoveB_window = canvas.create_window(10 + 6.5 * width, 8.5 * width, anchor=NW, window=bmoveB)
    bmoveD = Button(text="D", height=1, width=10, relief=RAISED, command=move_D)
    bmoveD_window = canvas.create_window(10 + 6.5 * width, 9 * width, anchor=NW, window=bmoveD)

    # double move
    bmoveU2 = Button(text="U2", height=1, width=10, relief=RAISED, command=move_U2)
    bmoveU2_window = canvas.create_window(10 + 8 * width, 6.5 * width, anchor=NW, window=bmoveU2)
    bmoveL2 = Button(text="L2", height=1, width=10, relief=RAISED, command=move_L2)
    bmoveL2_window = canvas.create_window(10 + 8 * width, 7 * width, anchor=NW, window=bmoveL2)
    bmoveF2 = Button(text="F2", height=1, width=10, relief=RAISED, command=move_F2)
    bmoveF2_window = canvas.create_window(10 + 8 * width, 7.5 * width, anchor=NW, window=bmoveF2)
    bmoveR2 = Button(text="R2", height=1, width=10, relief=RAISED, command=move_R2)
    bmoveR2_window = canvas.create_window(10 + 8 * width, 8 * width, anchor=NW, window=bmoveR2)
    bmoveB2 = Button(text="B2", height=1, width=10, relief=RAISED, command=move_B2)
    bmoveB2_window = canvas.create_window(10 + 8 * width, 8.5 * width, anchor=NW, window=bmoveB2)
    bmoveD2 = Button(text="D2", height=1, width=10, relief=RAISED, command=move_D2)
    bmoveD2_window = canvas.create_window(10 + 8 * width, 9 * width, anchor=NW, window=bmoveD2)

    # prim move
    bmoveU3 = Button(text="U3", height=1, width=10, relief=RAISED, command=move_U3)
    bmoveU3_window = canvas.create_window(10 + 9.5 * width, 6.5 * width, anchor=NW, window=bmoveU3)
    bmoveL3 = Button(text="L3", height=1, width=10, relief=RAISED, command=move_L3)
    bmoveL3_window = canvas.create_window(10 + 9.5 * width, 7 * width, anchor=NW, window=bmoveL3)
    bmoveF3 = Button(text="F3", height=1, width=10, relief=RAISED, command=move_F3)
    bmoveF3_window = canvas.create_window(10 + 9.5 * width, 7.5 * width, anchor=NW, window=bmoveF3)
    bmoveR3 = Button(text="R3", height=1, width=10, relief=RAISED, command=move_R3)
    bmoveR3_window = canvas.create_window(10 + 9.5 * width, 8 * width, anchor=NW, window=bmoveR3)
    bmoveB3 = Button(text="B3", height=1, width=10, relief=RAISED, command=move_B3)
    bmoveB3_window = canvas.create_window(10 + 9.5 * width, 8.5 * width, anchor=NW, window=bmoveB3)
    bmoveD3 = Button(text="D3", height=1, width=10, relief=RAISED, command=move_D3)
    bmoveD3_window = canvas.create_window(10 + 9.5 * width, 9 * width, anchor=NW, window=bmoveD3)

    # flip

    bmovex= Button(text="x", height=3, width=5, relief=RAISED, command=move_x)
    bmovex_window = canvas.create_window(10 + 11 * width, 6.5 * width, anchor=NW, window=bmovex)
    bmovey= Button(text="y", height=3, width=5, relief=RAISED, command=move_y)
    bmovey_window = canvas.create_window(10 + 11 * width, 7.5 * width, anchor=NW, window=bmovey)
    bmovez= Button(text="z", height=3, width=5, relief=RAISED, command=move_z)
    bmovez_window = canvas.create_window(10 + 11 * width, 8.5 * width, anchor=NW, window=bmovez)

    # display and text_window
    display = Text(height=7, width=39)
    text_window = canvas.create_window(10 + 6.5 * width, 10 + .5 * width, anchor=NW, window=display)
    create_facelet_rects(width)
    update_facelet_rects()

    root.mainloop()