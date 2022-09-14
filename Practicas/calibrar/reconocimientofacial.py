import cv2
import numpy as np
import sys
import os
if os.path.exists('camara.py'):
    import camara
else:
    print("Es necesario realizar la calibración de la cámara")
    exit()

haar_cara = cv2.CascadeClassifier("haar/")
haar_ojos = cv2.CascadeClassifier("haar/haarcascade_eye.xml")
haar_sonrisas = cv2.CascadeClassifier("haar/")


cap = cv2.VideoCapture(0)
if cap.isOpened():
    hframe = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    wframe = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("Tamaño del frame de la cámara: ", wframe, "x", hframe)

    matrix, roi = cv2.getOptimalNewCameraMatrix(camara.cameraMatrix, camara.distCoeffs, (wframe,hframe), 1, (wframe,hframe))
    roi_x, roi_y, roi_w, roi_h = roi

    final = False
    while not final:
        ret, framebgr = cap.read()
        if ret:
            # Aquí procesamos el frame
            framerectificado = cv2.undistort(framebgr, camara.cameraMatrix, camara.distCoeffs, None, matrix)
            framerecortado = framerectificado[roi_y : roi_y + roi_h, roi_x : roi_x + roi_w]
            frame = framerecortado
            frameh = roi_h
            framew = roi_w

            gris = cv2.cvt2Color(frame, cv2.COLOR_BGR2GRAY)

            caras = haar_cara.detectMultiScale(gris, 1.1, 5)
            for cx, cy, cw, ch in caras:
                cv2.rectangle(frame, (cx,cy),(cx+cw,cy+ch),(255,0,0),2)

                ojos = haar_ojo.detectMultiScale(gris[cy:cy+ch,cx:cx+cw], 1.1, 5)
                for ox, oy, ow, oh in ojos:
                    cv2.circle(frame, (cx+ox+ow//2, cy+oy+oh//2), (ow+oh)//4,(0,255,0),2)

                sonrisas = haar_sonrisas.detectMultiScale(gris[cy:cy+ch,cx:cx+cw], 1.1, 5)
                for sx, sy, sw, sh in ojos:
                    cv2.rectangle(frame, (cx+sx, cy+sy), (cx+sx+sw,cy+sy+sh)//4,(0,0,255),2)
            
            cv2.imshow("CUIA CAM", frame)
            if cv2.waitKey(1) == ord(' '):
                final = True
        else:
            final = True
else:
    print("No se pudo acceder a la cámara.")
