import numpy as np
import cv2


def hsv(r, g, b):
    r2 = r / 255
    g2 = g / 255
    b2 = b / 255

    cRedMax = np.max(r)
    cGreenMax = np.max(g)
    cBlueMax = np.max(b)

    cRedMin = np.max(r)
    cGreenMin = np.max(g)
    cBlueMin = np.max(b)

    cMax = np.max((cRedMax,
                   cBlueMax,
                   cRedMax))

    cMin = np.min((cRedMin,
                   cGreenMin,
                   cBlueMin))

    variation = cMax - cMin




image = cv2.imread("../imagens/frutas.png")
blue, green, red = cv2.split(image)
hsv(red,green,blue)
