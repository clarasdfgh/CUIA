import cv2
import numpy as np
import time

lena = cv2.imread('opencv/lena.tif')

b, g, r = cv2.split(lena)

cv2.imshow('ROJO', r)
time.sleep(3)
cv2.imshow('VERDE', g)
time.sleep(3)
cv2.imshow('AZUL', b)

cv2.waitKey()
time.sleep(1)
cv2.destroyAllWindows()

