import cv2
import numpy as np
from matplotlib import pyplot as plt

def eventoraton(evento, x, y, flags, params):
    if evento == cv2.EVENT_LBUTTONUP:
        print("H: ", framehsv[y,x,0])
        print("S: ", framehsv[y,x,1])
        print("V: ", framehsv[y,x,2])
        print("")

lena = cv2.imread('opencv/lena.tif')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()
    
#obtener tamaño de la webcam para tamaño de img de fondo
ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fondo = cv2.resize(lena, (ancho,alto))
    
#gestión eventos ratón - definimos la ventana previamente pq si no da error (intenta trabajar sobre algo que no existe)
cv2.namedWindow("WEBCAM")
cv2.setMouseCallback("WEBCAM", eventoraton)


while True:
    ret, frame = cap.read()

    if not ret:
        print("No he podido leer el frame")
        break

    framehsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )
    h, s, v = cv2.split(framehsv)
    
    #mascara background y convertirla en imagen de tres bandas - luego difuminado - luego foreground
    mbg = cv2.inRange(framehsv, (10, 140, 120), (20, 255, 255))
    mascarabg = cv2.merge((mbg, mbg, mbg))
    
    mascarabg = cv2.GaussianBlur(mascarabg, (11,11), 0)
    
    mascarafg = cv2.bitwise_not(mascarabg)
    
    fg = cv2.bitwise_and(frame,mascarafg)
    bg = cv2.bitwise_and(fondo,mascarabg)
    
    frame = cv2.bitwise_or(fg,bg)

    cv2.imshow('WEBCAM', frame)

    if cv2.waitKey(1) == ord(' '):
        break

cap.release()
cv2.destroyWindow('WEBCAM')
