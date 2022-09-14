import cv2
import numpy as np
import time

lena = cv2.imread('opencv/lena.tif')

lena_hsv = cv2.cvtColor(lena, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(lena_hsv)

cv2.imshow('TONO', h)
time.sleep(3)
cv2.imshow('SATURACION', s)
time.sleep(3)
cv2.imshow('VALOR', v)
time.sleep(3)

cv2.waitKey()
cv2.destroyAllWindows()
