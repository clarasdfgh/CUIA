import cv2
import numpy as np
import time
import sys
import os
if os.path.exists('camara.py'):
    import camara
else:
    print("Es necesario realizar la calibración de la cámara")
    exit()


net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000_fp16.caffemodel")
#net = cv2.dnn.readNetFromTensorflow("deep/opencv_face_detector_uint8.pb", "deep/opencv_face_detector.pbtxt")


max_imagenes =  100
donde = "train_color"
quien = "rocio"

objetivoW = 224
objetivoH = 224
prop = objetivoW / objetivoH

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if cap.isOpened():
    frameh = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    framew = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    final = False
    n = 0

    t = time.time()
    while not final:
        ret, frame = cap.read()
        if ret:
            blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104., 117., 123.], False, False)
            net.setInput(blob)
            detections = net.forward()
            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.7:
                    startX = int(framew * detections[0, 0, i, 3])
                    startY = int(frameh * detections[0, 0, i, 4])
                    endX = int(framew * detections[0, 0, i, 5])
                    endY = int(frameh * detections[0, 0, i, 6])
                    w = endX - startX
                    h = endY - startY
                    if w/h > prop:
                        nuevah = int(w / prop)
                        startY -= int((nuevah - h) / 2)
                        endY = startY + nuevah
                    elif w/h < prop:
                        nuevaw = int(h * prop)
                        startX -= int((nuevaw - w) / 2)
                        endX = startX + nuevaw
                    frame = cv2.resize(frame[startY:endY, startX:endX], (objetivoW, objetivoH))
                    cv2.imshow("CUIA", frame)
                    if time.time() - t > 1:
                        fichero = "{0:s}/{1:s}/{2:02d}.jpg".format(donde, quien, n)
                        cv2.imwrite(fichero, frame)
                        print(fichero)
                        n = n + 1
                        t = time.time()
        if n == max_imagenes or cv2.waitKey(1) == ord(' '):
            final = True
    else:
        final = True
else:
    print("No se pudo acceder a la cámara.")