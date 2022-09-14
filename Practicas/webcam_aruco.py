import cv2
import numpy as np
from cv2 import aruco

DICCIONARIO = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)
lena = cv2.imread("opencv/lena.tif")
h, w, _ = lena.shape

vlena = np.array([[0,0],[w,0],[w,h],[0,h]])

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("No he podido leer el frame")
        break


    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bboxs, ids, rechazados = aruco.detectMarkers(gris, DICCIONARIO)
    
    if(ids is not None):
        aruco.drawDetectedMarkers(frame, bboxs, ids)
        for i in range(len(ids)):
            vertices = bboxs[i][0].astype(int)
            
            #cv2.line(frame, vertices[0], vertices[2], (0,0,255),4)
            #cv2.line(frame, vertices[1], vertices[3], (0,0,255),4)
            #cv2.rectangle(frame, vertices[0], vertices[2], (0,255,255), -1)
            #cv2.circle(frame, vertices[1], 30, (255,0,0), 2)
            #cv2.polylines(frame, [vertices], True, (0,255,0), 3)
            #cv2.fillConvexPoly(frame, vertices, (255,255,255),)
            cv2.putText(frame, str(ids[i][0]), vertices[1], cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
##EJERCICIO: CENTRAR EL TEXTO EN EL MARCARDOR (función ancho y alto de lo que vamos a escribir)
            
            matriz, _ = cv2.findHomography(vlena, vertices)
            warplena = cv2.warpPerspective(lena, matriz, (frame.shape[1], frame.shape[0]))
            
##EJERCICIO: ADAPTARLO PARA IMG CON CANAL ALFA
            
            #cv2.fillConvexPoly(frame, vertices, (0,0,0))
            #frame = frame + warplena
    
    cv2.imshow('WEBCAM', frame)

    if cv2.waitKey(1) == ord(' '):
        break

cap.release()
cv2.destroyWindow('WEBCAM')
