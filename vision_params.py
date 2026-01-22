import os
import json
from enums import *

PARAM_FILE = "params.json"

DEFAULTS = {
    "BLACK_TRH": 60.,
    "GAUSSIAN_BLUR": 5.,
    "MIN_SQUARE_SIZE": 10.,
    "MAX_SQUARE_SIZE": 100.,
    "COLOR_RANGES": {
        Color.White: (
            [0, 0, 200],
            [180, 40, 255]
        ),
        Color.Yellow: (
            [20, 100, 100],
            [30, 255, 255]
        ),
        Color.Blue: (
            [100, 150, 50],
            [140, 255, 255]
        ),
        Color.Green: (
            [40, 70, 70],
            [80, 255, 255]
        ),
        Color.Red: (
            [0, 120, 70],
            [10, 255, 255]
        ),
        Color.Orange: (
            [10, 150, 150],
            [20, 255, 255]
        ),
    },
}

_settings = None

def load():
    global _settings
    if _settings is None:
        if os.path.exists(PARAM_FILE):
            with open(PARAM_FILE, "r") as f:
                _settings = json.load(f)
        else:
            _settings = DEFAULTS.copy()
    return _settings

def save():
    if _settings is None:
        return
    with open(PARAM_FILE, "w") as f:
        json.dump(_settings, f, indent=4)

def get(key):
    return load()[key]

def set(key, value):
    load()[key] = float(value)
    save()