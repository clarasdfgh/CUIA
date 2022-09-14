import cv2
import numpy as np
import time

opencv = cv2.imread('opencv/icono-opencv.png',cv2.IMREAD_UNCHANGED)

opencv_bgr = opencv[:, :, 0:3]
opencv_alpha = opencv[:, :, 3]

cv2.imshow('COLOR', opencv_bgr)
time.sleep(3)
cv2.imshow('ALPHA', opencv_alpha)

cv2.waitKey()
time.sleep(1)
cv2.destroyAllWindows()

