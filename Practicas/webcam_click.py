import cv2
import numpy as np
from matplotlib import pyplot as plt

def eventoraton(evento, x, y, flags, params):
    if evento == cv2.EVENT_LBUTTONUP:
        print("H: ", framehsv[y,x,0])
        print("S: ", framehsv[y,x,1])
        print("V: ", framehsv[y,x,2])
        print("")


#crear la ventana en la que vamos a representar la gráfica
#crea una ventana en la que habrá 1 fila con 3 columnas (gráficas)
#devuelve 2 cosas: la ventana, y un vector con los "controladores" de cada una de las gráficas
histograma, (axH, axS, axV) = plt.subplots(1, 3)

plt.ion() 		#Modo interactivo, para que la ventana se muestre y el programa siga
plt.show()		#Muestra todos los plots que tengamos

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()
    
    
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
    

    
    
    
    #1er arg: imagen, 2o arg: bandas, 3er arg: máscara, 4o arg: tam, 5o: rango
    histoh = cv2.calcHist([framehsv], [0], None, [180], [0,180])
    histos = cv2.calcHist([framehsv], [1], None, [256], [0,256])
    histov = cv2.calcHist([framehsv], [2], None, [256], [0,256])
    
    #Primero borrar los datos del anterior frame
    axH.clear()
    axV.clear()
    axS.clear()
    
    axH.set_title("HUE") #comprobar si clear borra el título o no
    axV.set_title("VALUE")
    axS.set_title("SATURATION")
    
    axH.plot(histoh)
    axV.plot(histov)
    axS.plot(histos)
	
    histograma.canvas.flush_events() #redibujar histograma, interactividad

    cv2.imshow('WEBCAM', frame)

    if cv2.waitKey(1) == ord(' '):
        break

cap.release()
cv2.destroyWindow('WEBCAM')
