from enums import *
import numpy as np

COLOR_RANGES = {
    Color.White: (
        np.array([0, 0, 200]),
        np.array([180, 40, 255])
    ),
    Color.Yellow: (
        np.array([20, 100, 100]),
        np.array([30, 255, 255])
    ),
    Color.Blue: (
        np.array([100, 150, 50]),
        np.array([140, 255, 255])
    ),
    Color.Green: (
        np.array([40, 70, 70]),
        np.array([80, 255, 255])
    ),
    Color.Red: (
        np.array([0, 120, 70]),
        np.array([10, 255, 255])
    ),
    Color.Orange: (
        np.array([10, 150, 150]),
        np.array([20, 255, 255])
    ),
}

BLACK_TRH = 60
GAUSSIAN_BLUR = 5