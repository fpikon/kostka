from enum import IntEnum


class Color(IntEnum):
    """Kolory kostki"""
    U = 0
    L = 1
    F = 2
    R = 3
    B = 4
    D = 5

class ColorCamera(IntEnum):
    """Kolory kostki z kamery"""
    White = 0
    Green = 1
    Red = 2
    Blue = 3
    Orange = 4
    Yellow = 5
    Undetected = 6

def str_ColorCamera(num):
    str = ""
    match num:
        case ColorCamera.White:
            str += "White"
        case ColorCamera.Green:
            str += "Green"
        case ColorCamera.Red:
            str += "Red"
        case ColorCamera.Blue:
            str += "Blue"
        case ColorCamera.Orange:
            str += "Orange"
        case ColorCamera.Yellow:
            str += "Yellow"
        case ColorCamera.Undetected:
            str += "Undetected"

    return str