import gui
import cv2
import kamera
from cube import Cube
from threading import Thread

kostka = Cube()

gui.start_gui(kostka)

cv2.destroyAllWindows()