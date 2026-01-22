import copy
import numpy as np

from enums import *

class Cube:
    def __init__(self):
        self.__faces = []
        for color in Face:
            self.__faces.append(np.ones((3,3), dtype=Color) * color)

    def __str__(self):
        string = ""

        face_u = self.__faces[Face.U]
        for row in face_u:
            string += " " * 7
            for u in row:
                string += str(Face(u)) + " "
            string += "\n"
        string += "\n"

        for i in range(3):
            for j in range(Face.L, Face.B + 1):
                for k in self.__faces[j][i]:
                    string += str(Face(k)) + " "
                string += " "
            string += "\n"
        string += "\n"

        face_d = self.__faces[Face.D]
        for row in face_d:
            string += " " * 7
            for d in row:
                string += str(Face(d)) + " "
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

            new_face_rect = to_Face(string[i])
            if new_face_rect == -1:
                return False
            new_faces[a][b][c] = new_face_rect
            counter[new_face_rect] += 1


        if all(x == 9 for x in counter):
            self.__faces = new_faces
            return True
        else:
            return False

    def clear(self):
        self.__faces = []
        for color in Face:
            self.__faces.append(np.ones((3,3), dtype=Color) * color)


    def update_face(self, face_array):
        if len(face_array) != 3:
            return False
        if len(face_array[0]) != 3:
            return False
        middle = face_array[1][1]
        if middle == Color.Undetected:
            return False
        self.__faces[middle] = face_array
        return True

    def get_string(self):
        string = ""

        for face in self.__faces:
            for row in face:
                for i in row:
                    string += str(Face(i))

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
                    self.__rotate_face(Face.F, [Face.U, Face.D, Face.L, Face.R])
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
                    new_faces[Face.U] = self.__faces[Face.F]
                    new_faces[Face.B] = np.rot90(self.__faces[Face.U], 2)
                    new_faces[Face.D] = np.rot90(self.__faces[Face.B], 2)
                    new_faces[Face.F] = self.__faces[Face.D]
                    self.__faces = new_faces
                    self.__faces[Face.R] = np.rot90(self.__faces[Face.R], -1)
                    self.__faces[Face.L] = np.rot90(self.__faces[Face.L], 1)
                case "y":
                    new_faces[Face.F] = self.__faces[Face.R]
                    new_faces[Face.R] = self.__faces[Face.B]
                    new_faces[Face.B] = self.__faces[Face.L]
                    new_faces[Face.L] = self.__faces[Face.F]
                    self.__faces = new_faces
                    self.__faces[Face.U] = np.rot90(self.__faces[Face.U], -1)
                    self.__faces[Face.D] = np.rot90(self.__faces[Face.D], 1)
                case "z":
                    new_faces[Face.U] = np.rot90(self.__faces[Face.L], -1)
                    new_faces[Face.R] = np.rot90(self.__faces[Face.U], -1)
                    new_faces[Face.D] = np.rot90(self.__faces[Face.R], -1)
                    new_faces[Face.L] = np.rot90(self.__faces[Face.D], -1)
                    self.__faces = new_faces
                    self.__faces[Face.F] = np.rot90(self.__faces[Face.F], -1)
                    self.__faces[Face.B] = np.rot90(self.__faces[Face.B], 1)

        return True

    def __rotate_face(self, face, adj_faces = None):
        matrix = np.ones((5, 5), Color)

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