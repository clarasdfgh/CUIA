import cv2
import numpy as np

video = cv2.VideoCapture("opencv/escenario.mp4")
fps = video.get(cv2.CAP_PROP_FPS)

if not video.isOpened():
    print("No se puede abrir el fichero")
    exit()
while True:
    ret, frame = video.read()

    if not ret:
        print("No se ha podido leer el frame")
        break

    cv2.imshow('WEBCAM', frame)

    #no puede ser arbitrario, din'amico
    if cv2.waitKey(60) == ord(' '):
        break

video.release()
cv2.destroyWindow('WEBCAM')
