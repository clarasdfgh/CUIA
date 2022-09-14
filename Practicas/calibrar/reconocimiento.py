import cv2
import numpy as np
import camara

#img   = cv2.imread("figuras.jpg")
#ULTIMA PARTE DE LA CLASE: DETECTAR CON EL BILLAR, EL RESTO ES CON LAS FIGURAS
img   = cv2.imread("billar.jpg")

gris  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, bn = cv2.threshold(gris, 200, 255, cv2.THRESH_BINARY)

#PRIMERA PARTE DE LA CLASE: HARRIS (+circulos centroids)
#harris = cv2.cornerHarris(bn, blockSize=5, ksize=15, k=0.01)
#harris = cv2.dilate(harris, None)
#_, harris = cv2.threshold(harris, 0.01*harris.max(), 255, cv2.THRESH_BINARY)
#harris = np.uint8(harris)
#_, _, _, centroids = cv2.connectedComponentsWithStats(harris)

#SEGUNDA PARTE DE LA CLASE: CORNERS (+circulos corners)
#corners = cv2.goodFeaturesToTrack(bn, maxCorners=80, qualityLevel=0.001,
#            minDistance=20, useHarrisDetector=True, k=0.01)

#TERCERA PARTE DE LA CLASE: CONTORNO
#poli, _ = cv2.findContours(bn, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#for p in poli:
    #1:
    #cv2.drawContours(img, [p], 0, (255,0,0), 3)
    
    #2:
    #vertices = cv2.approxPolyDP(p, 0.009*cv2.arcLength(p, True), True)
    #cv2.polylines(img, [vertices], True, (255,0,0), len(vertices))
    
    #3: rectángulo
    #x, y, w, h = cv2.boundingRect(p)
    #cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)
    
    #4: rectángulo área mínima
    #mar = cv2.minAreaRect(p)
    #box = cv2.boxPoints(mar)
    #box = box.astype(int)
    #cv2.polylines(img, [box], True, (255,0,0), len(box))
    
    #5: círculo
    #(x,y),r = cv2.minEnclosingCircle(p)
    #x = int(x)
    #y = int(y)
    #r = int(r)
    #cv2.circle(img, (x,y), r, (255,0,0), 2)

#CIRCULOS
#for c in corners:
#    x = c[0][0].astype(int)
#    y = c[0][1].astype(int)
#    cv2.circle(img, (x,y), 6, (0,255,0), 2) 

#ULTIMA PARTE DE LA CLASE: DETECTAR EN IMG DEL BILLAR - un poco pocho
circulos = cv2.HoughCircles(bn, cv2.HOUGH_GRADIENT, dp=1.5, minDist=100, param1=50, param2=30)
            
for c in circulos:
    x, y, r = c[0].astype(int)
    cv2.circle(img, (x,y), r, (255,0,0), 2)

cv2.imshow("IMAGEN", img)
#cv2.imshow("IMAGEN2", bn)
#cv2.imshow("IMAGEN3", harris)
cv2.waitKey()
