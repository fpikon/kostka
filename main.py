from enums import *
import gui
from face_kostka import *
import twophase.solver as sv

"""
kostka = FaceKostka()

cube_string_org= "DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL"
cube_string = convert_strings(cube_string_org)
flag = kostka.from_string(cube_string)
print(kostka)
print("___________________")

solution = sv.solve(convert_strings(kostka.get_string(), False), 20, 5)
solution = solution.split(" ")

for move in solution:
    print(move)
    kostka.make_move(move)

print(kostka)"""

gui.start_gui()