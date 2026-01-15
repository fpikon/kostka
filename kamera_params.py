from enums import *
import numpy as np

COLOR_RANGES = {
    ColorCamera.White: (
        np.array([0, 0, 200]),
        np.array([180, 40, 255])
    ),
    ColorCamera.Yellow: (
        np.array([20, 100, 100]),
        np.array([30, 255, 255])
    ),
    ColorCamera.Blue: (
        np.array([100, 150, 50]),
        np.array([140, 255, 255])
    ),
    ColorCamera.Green: (
        np.array([40, 70, 70]),
        np.array([80, 255, 255])
    ),
    ColorCamera.Red: (
        np.array([0, 120, 70]),
        np.array([10, 255, 255])
    ),
    ColorCamera.Orange: (
        np.array([10, 150, 150]),
        np.array([20, 255, 255])
    ),
}

BLACK_TRH = 60
