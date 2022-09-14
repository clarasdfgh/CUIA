import cv2
import numpy as np
import sys
import os
if os.path.exists('camara.py'):
    import camara
else:
    print("Es necesario realizar la calibración de la cámara")
    exit()

selfi = cv2.imread("selfi2.jpg")
selfih, selfiw, _ = selfi.shape
selfigris = cv2.cvtColor(selfi, cv2.COLOR_BGR2GRAY)

#instanciación del algoritmo (cv2 guarda los algoritmos en clases)
F = cv2.SIFT_create()
D = F


#index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
#search_params = dict(checks=100)

M = cv2.FlannBasedMatcher()

KPselfi = F.detect(selfigris)
KPselfi, DESCselfi = D.compute(selfigris, KPselfi)

#cv2.drawKeypoints(selfi, KPselfi, selfi, color=(0,255,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


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

            gris = cv2.cvtColor(framerecortado, cv2.COLOR_BGR2GRAY)
            KPcam, DESCcam = D.detectAndCompute(gris, None)
            coincidencias = M.knnMatch(DESCselfi, DESCcam, k=2)
            
            #KPselfi = F.detect(selfigris)
            #KPselfi, DESCselfi = D.compute(selfigris, KPselfi)
            
            good = []
            for c1, c2 in coincidencias:
                    if c1.distance < 0.5*c2.distance:
                        good.append(c1)


            frame = cv2.drawMatches(selfi, KPselfi, frame, KPcam, good, frame, matchColor=(0,255,255), flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)


            #cv.calibrationMatrixValues(cameraMatrix, imageSize, apertureWidth, apertureHeight	) ->	fovx, fovy, focalLength, principalPoint, aspectRatio

            cv2.imshow("CUIA CAM", frame)
            if cv2.waitKey(1) == ord(' '):
                final = True
        else:
            final = True
else:
    print("No se pudo acceder a la cámara.")