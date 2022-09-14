import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#Escalado de imágenes
opencv = cv2.imread('opencv/icono-opencv.png', cv2.IMREAD_UNCHANGED)
mosca = cv2.resize(opencv, None, fx=0.3, fy=0.3)

#Superposición de imágenes con transparencia y traslación
fg   = mosca[:, :, 0:3]
hfg, wfg, _ = fg.shape

alfa = mosca[:, :, 3]
afla = 255 - alfa

alfa = cv2.cvtColor(alfa, cv2.COLOR_GRAY2BGR) / 255
afla = cv2.cvtColor(afla, cv2.COLOR_GRAY2BGR) / 255


if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()
while True:
    ret, frame = cap.read()

    bg   = frame
    hbg, wbg, _ = bg.shape

    if not ret:
        print("No he podido leer el frame")
        break
    
    x = 10
    y = 10

    mezcla = frame
    mezcla[y:y+hfg, x:x+wfg] = mezcla[y:y+hfg, x:x+wfg]*afla + fg*alfa

    cv2.imshow('WEBCAM', mezcla)

    if cv2.waitKey(1) == ord(' '):
        break

cap.release()
cv2.destroyWindow('WEBCAM')
