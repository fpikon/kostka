from enum import IntEnum


class Face(IntEnum):
    """Twarze kostki"""
    U = 0
    L = 1
    F = 2
    R = 3
    B = 4
    D = 5

    def __str__(self):
        return str(self.name)

class Color(IntEnum):
    """Kolory kostki"""
    White = 0
    Green = 1
    Red = 2
    Blue = 3
    Orange = 4
    Yellow = 5
    Undetected = 6

    def __str__(self):
        return str(self.name)

def to_Face(s):
    face = -1
    match s.upper():
        case "U":
            face = Face.U
        case "L":
            face = Face.L
        case "F":
            face = Face.F
        case "R":
            face = Face.R
        case "B":
            face = Face.B
        case "D":
            face = Face.D
    return face