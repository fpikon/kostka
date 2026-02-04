import os
import json
from enums import *

PARAM_FILE = "params.json"

DEFAULTS = {
    "BLACK_TRH": 60.,
    "GAUSSIAN_BLUR": 5.,
    "MIN_SQUARE_SIZE": 10.,
    "MAX_SQUARE_SIZE": 100.,
    "WHITE_RANGE": (
        [0, 200],
        [40, 255]
    ),
    "RED_RANGE": (
        0,
        10
    ),
    "ORANGE_RANGE": (
        10,
        20
    ),
    "YELLOW_RANGE": (
        20, 
        30
    ),
    "GREEN_RANGE": (
        40,
        80
    ),
    "BLUE_RANGE": (
        80,
        140
    )
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
    load()[key] = value
    save()