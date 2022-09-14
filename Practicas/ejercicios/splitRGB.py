import cv2
import numpy as np
import time as t

lena = cv2.imread('opencv/lena.tif')

#Para este ejercicio en realidad no nos hace falta split, porque split siempre
#mostrará una imagen en escala de grises. Lo que realmente queremos es 
#suprimir los dos canales que no nos interesan:

#b, g, r = cv2.split(lena)

#Los canales son B->0, G->1, R->2

b = lena.copy()
b[:, :, 1] = 0
b[:, :, 2] = 0

g = lena.copy()
g[:, :, 0] = 0
g[:, :, 2] = 0

r = lena.copy()
r[:, :, 0] = 0
r[:, :, 1] = 0

cv2.imshow('AZUL', b)
t.sleep(2)
cv2.imshow('VERDE', g)
t.sleep(2)
cv2.imshow('ROJO', r)
t.sleep(2)

cv2.waitKey(0)
cv2.destroyAllWindows()



