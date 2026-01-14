import copy
import numpy as np

from enums import *

class FaceKostka:
    def __init__(self):
        self.__faces = []
        for color in Color:
            self.__faces.append(np.ones((3,3), dtype=np.int8)*color)

    def __str__(self):
        string = ""

        face_u = self.__faces[Color.U]
        for row in face_u:
            string += " " * 7
            for u in row:
                string += str(u) + " "
            string += "\n"
        string += "\n"

        for i in range(3):
            for j in range(Color.L, Color.B + 1):
                for k in self.__faces[j][i]:
                    string += str(k) + " "
                string += " "
            string += "\n"
        string += "\n"

        face_d = self.__faces[Color.D]
        for row in face_d:
            string += " " * 7
            for d in row:
                string += str(d) + " "
            string += "\n"

        return string

    def from_string(self, string):
        length = len(string)

        new_faces = copy.deepcopy(self.__faces)

        if length != 6 * 9:
            return False

        counter = [0, 0, 0, 0, 0, 0]

        for i in range(length):
            a = i // 9
            b = (i - 9 * a) // 3
            c = (i - 9 * a) % 3

            match string[i]:
                case "U":
                    new_faces[a][b][c] = Color.U
                    counter[Color.U] += 1
                case "L":
                    new_faces[a][b][c] = Color.L
                    counter[Color.L] += 1
                case "F":
                    new_faces[a][b][c] = Color.F
                    counter[Color.F] += 1
                case "R":
                    new_faces[a][b][c] = Color.R
                    counter[Color.R] += 1
                case "B":
                    new_faces[a][b][c] = Color.B
                    counter[Color.B] += 1
                case "D":
                    new_faces[a][b][c] = Color.D
                    counter[Color.D] += 1

        if all(x == 9 for x in counter):
            self.__faces = new_faces
            return True
        else:
            return False

    def clear(self):
        self.__faces = []
        for color in Color:
            self.__faces.append(np.ones((3,3), dtype=np.int8)*color)

    def get_string(self):
        string = ""

        for face in self.__faces:
            for row in face:
                for i in row:
                    match i:
                        case Color.U:
                            string += "U"
                        case Color.L:
                            string += "L"
                        case Color.F:
                            string += "F"
                        case Color.R:
                            string += "R"
                        case Color.B:
                            string += "B"
                        case Color.D:
                            string += "D"

        return string

    def make_move(self, move_str):
        length = len(move_str)
        if length != 2 and length != 1:
            return False
        if length == 2:
            num_moves = int(move_str[1])
        else:
            num_moves = 1

        what_move = move_str[0]

        for _ in range(num_moves):
            new_faces = copy.deepcopy(self.__faces)
            match what_move:
                case "U":
                    self.make_move("x3")
                    self.make_move("F")
                    self.make_move("x")
                case "L":
                    self.make_move("y3")
                    self.make_move("F")
                    self.make_move("y")
                case "F":
                    self.__rotate_face(Color.F, [Color.U, Color.D, Color.L, Color.R])
                case "R":
                    self.make_move("y")
                    self.make_move("F")
                    self.make_move("y3")
                case "D":
                    self.make_move("x")
                    self.make_move("F")
                    self.make_move("x3")
                case "B":
                    self.make_move("y2")
                    self.make_move("F")
                    self.make_move("y2")
                case "x":
                    new_faces[Color.U] = self.__faces[Color.F]
                    new_faces[Color.B] = np.rot90(self.__faces[Color.U], 2)
                    new_faces[Color.D] = np.rot90(self.__faces[Color.B], 2)
                    new_faces[Color.F] = self.__faces[Color.D]
                    self.__faces = new_faces
                    self.__faces[Color.R] = np.rot90(self.__faces[Color.R], -1)
                    self.__faces[Color.L] = np.rot90(self.__faces[Color.L], 1)
                case "y":
                    new_faces[Color.F] = self.__faces[Color.R]
                    new_faces[Color.R] = self.__faces[Color.B]
                    new_faces[Color.B] = self.__faces[Color.L]
                    new_faces[Color.L] = self.__faces[Color.F]
                    self.__faces = new_faces
                    self.__faces[Color.U] = np.rot90(self.__faces[Color.U], -1)
                    self.__faces[Color.D] = np.rot90(self.__faces[Color.D], 1)
                case "z":
                    new_faces[Color.U] = np.rot90(self.__faces[Color.L], -1)
                    new_faces[Color.R] = np.rot90(self.__faces[Color.U], -1)
                    new_faces[Color.D] = np.rot90(self.__faces[Color.R], -1)
                    new_faces[Color.L] = np.rot90(self.__faces[Color.D], -1)
                    self.__faces = new_faces
                    self.__faces[Color.F] = np.rot90(self.__faces[Color.F], -1)
                    self.__faces[Color.B] = np.rot90(self.__faces[Color.B], 1)

        return True

    def __rotate_face(self, face, adj_faces = None):
        matrix = np.ones((5, 5), np.int8) * -1

        matrix[1:4, 1:4] = self.__faces[face]
        if adj_faces:
            matrix[0, 1:4] = self.__faces[adj_faces[0]][2, :]
            matrix[4, 1:4] = self.__faces[adj_faces[1]][0, :]
            matrix[1:4, 0] = self.__faces[adj_faces[2]][:, 2]
            matrix[1:4, 4] = self.__faces[adj_faces[3]][:, 0]

        matrix = np.rot90(matrix, -1)

        self.__faces[face] = matrix[1:4, 1:4]
        if adj_faces:
            self.__faces[adj_faces[0]][2, :] = matrix[0, 1:4]
            self.__faces[adj_faces[1]][0, :] = matrix[4, 1:4]
            self.__faces[adj_faces[2]][:, 2] = matrix[1:4, 0]
            self.__faces[adj_faces[3]][:, 0] = matrix[1:4, 4]

def convert_strings(string, from_twophase = True):
    new_string = ""
    if len(string) != 6 * 9:
        return False
    if from_twophase is True:
        new_string += string[0:9]
        new_string += string[36:45]
        new_string += string[18:27]
        new_string += string[9:18]
        new_string += string[45:54]
        new_string += string[27:36]
    else:
        new_string += string[0:9]
        new_string += string[27:36]
        new_string += string[18:27]
        new_string += string[45:54]
        new_string += string[9:18]
        new_string += string[36:45]

    return new_string