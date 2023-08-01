#################################################################
#                                                               #
#               Jorge Enrique González Gonzalo                  #
#                                                               #
#################################################################

#################################################################
#   Python 3.9.7                                                #
#	• Programa de seguimiento ocular para el uso de aplicacion:	#
#		Funcionamiento:											#
#			Lanza la aplicacion de calibración en caso de ser	#
#			la primera ejecucion o en caso de que el usuario	#
#			lo desee, despues de tener los puntos maximos y		#
#			minimos del movimiento del usuario se ajustan		#
#			las coordenadas para leerlas desde la webcam y		#
#			mover los pixeles correspondientes al tamaño de la	#
#			pantalla. Despues se lanza el programa en el que	#
# 			el usuario dispondra de diferentes funciones y 		#
#			juegos												#
#																#
#		Entradas del programa:									#
# 			-p -> Predictor de puntos de referencia faciales	#
#																#
#		Salidas del programa:									#
#			Ninguna, solo mueve el raton por la pantalla		#
#																#
#################################################################



############################ IMPORTS ############################
# Se usa para lo de la distancia eclideana
from scipy.spatial import distance as dist
import numpy as np

# Deteccion de rasgos faciales
from imutils import face_utils

# Personalizacion de paramentros de lanzamiento
import argparse

# Tiempo
import time

# Movimiento del cursor
import pyautogui

# Reconocimiento de los ojos y temas relacionados
import dlib
import cv2

# Tratamiento de ficheros .csv
import csv

# Para conseguir la anchura y altura de la pantalla del dispositivo
from win32api import GetSystemMetrics

# Para dar color a las salidas del terminal
from colorama import init, Fore, Back, Style

import subprocess



print(Fore.GREEN+"[######################## SEPARADOR ########################]\n"+Fore.RESET)
print(Fore.LIGHTBLACK_EX+"[################### INICIO DEL PROGRAMA ###################]\n"+Fore.RESET)

# Iniciar Colorama en windows
init()


########################### CONSTANTES ##########################

# Define dos constantes, una para la relacion de aspecto medio
# para indicar el pestañeo y la segunda constante es el numero
# de cuadros donde los marcos del ojo debe estar por debajo del 
# umbral
EYE_AR_THRESH = 0.20
EYE_AR_CONSEC_FRAMES = 5

# Inicia el contador de cuadros y el total de pestañeos
COUNTER = 0
TOTAL = 0



####################### VARIABLES GLOBALES ######################


# VARIABLE BOOLEANA PARA SELECCIÓN DE LA RESOLUCIÓN
# EN LA QUE SE BASARÁ EL PROGRAMA
# opcion = 0 -> Resolucion de 16:9
# opcion = 1 -> Resolucion de 4:3
opcion = 0

# ANCHO DE LA PANTALLA NATIVA DEL DISPOSITIVO
ancho = GetSystemMetrics(0)
print(Fore.CYAN+f"[INFO] Ancho de la pantalla: {ancho}"+Fore.RESET)
# ALTO DE LA PANTALLA NATIVA DEL DISPOSITIVO
alto = GetSystemMetrics(1)
print(Fore.CYAN+f"[INFO] Alto de la pantalla: {alto}"+Fore.RESET)

# RELACIÓN DE ASPECTO DE LA PANTALLA NATIVA DEL DISPOSITIVO
relacion_de_aspecto = ancho/alto


# FICHERO DE COORDENADAS MAXIMAS Y MINIMAS

try:
    archivo_csv = open('./coordenadas_max_min.csv', 'r')
    lector_csv = csv.reader(archivo_csv)
except FileNotFoundError:
    subprocess.run('py ./calibracion.py -p ./shape_predictor_68_face_landmarks.dat', shell=True)
    archivo_csv = open('./coordenadas_max_min.csv', 'r+')
    lector_csv = csv.reader(archivo_csv)




# COORDENADAS OBTENIDAS DEL FICHERO
X_max, X_min, Y_max, Y_min = next(lector_csv)

region_efectiva = (int(X_max)-int(X_min), int(Y_max)- int(Y_min))

# Dimensiones de la webcam (Dependiendo la resolucion de la pantalla)
# CAMBIO DE VALOR A LA VARIABLE BOOLEANA PARA EL FUNCIONAMIENTO DEL PROGRAMA
if relacion_de_aspecto == 1.7777777777777777: # Relacion de aspecto es igual a 16:9
	opcion = 0
	print(Fore.CYAN+"[INFO] Relacion de aspecto = 16:9"+Fore.RESET)
elif relacion_de_aspecto == 1.3333333333333333: # Relacion de aspecto es igual a 4:3
	opcion = 1
	print(Fore.CYAN+"[INFO] Relacion de aspecto = 4:3"+Fore.RESET)


WEBCAM = region_efectiva
# Dimensiones de la pantalla de destino
PANTALLA_DESTINO = (ancho, alto)



# Contruye y fija los argumentos de entrada del programa
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help=Fore.RED+"Direccion del predictor de puntos de referencia faciales"+Fore.RESET)
args = vars(ap.parse_args())



# Iniciando el detector de cara de dlib (HOG-based) y cargando el
# predictor de puntos de referencia faciales
print(Fore.CYAN+"[INFO] Cargando el predictor de puntos de referencia faciales..."+Fore.RESET)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])




# FUNCION "eye_aspecto_radio"
# 	Su uso es para calcular la relacion de aspecto del ojo para
#	luego usarlo para detectar los pestañeos
def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])
	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])
	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)
	# return the eye aspect ratio
	return ear




# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]



# start the video stream thread
print(Fore.CYAN+"[INFO] Iniciando hilo de transmisión de video...\n"+Fore.RESET)
vs = cv2.VideoCapture(0)






# COMPROBACIÓN DE COORDENADAS MAXIMAS Y MINIMAS DEL FICHERO
# "coordenadas_max_min.csv" generado en "calibracion.py"
print(Fore.GREEN+"[######################## SEPARADOR ########################]\n"+Fore.RESET)
print(Fore.BLUE+f"[INFO] Coordenadas maximas y minimas = X_max: {X_max} | X_min: {X_min} | Y_max: {Y_max} | Y_min: {Y_min}\n"+Fore.RESET)







# FUNCION "obtener_valores_calibracion_inversa":
# Funcion para obtener los valores de escala para cambiar coordenadas
# de 1920x1080 a la region efectiva
# Parametros:
#		pantalla_640x360: Tupla de las coordenadas maximas de la webcam
#		pantalla_1920x1080: Tupla de las coordenadas maximas de la pantalla
def obtener_valores_calibracion_1920(pantalla_640x360, pantalla_1920x1080):
    # Coordenadas máximas y mínimas en la pantalla de 640x360
    x_min_640, y_min_640 = 0, 0
    x_max_640, y_max_640 = pantalla_640x360

    # Coordenadas máximas y mínimas en la pantalla de 1920x1080
    x_min_1920, y_min_1920 = 0, 0
    x_max_1920, y_max_1920 = pantalla_1920x1080

    # Calcular las escalas y desplazamientos inversos
    escala_x_inv = (x_max_640 - x_min_640) / (x_max_1920 - x_min_1920)
    escala_y_inv = (y_max_640 - y_min_640) / (y_max_1920 - y_min_1920)

    desplazamiento_x_inv = x_min_640 - x_min_1920 * escala_x_inv
    desplazamiento_y_inv = y_min_640 - y_min_1920 * escala_y_inv

    return escala_x_inv, escala_y_inv, desplazamiento_x_inv, desplazamiento_y_inv

# Obtener los valores de calibración inversos
escala_x_inv, escala_y_inv, desplazamiento_x_inv, desplazamiento_y_inv = obtener_valores_calibracion_1920(WEBCAM, PANTALLA_DESTINO)



# FUNCION PARA OBTENER FACTORES DE ESCALA DE COORDENADAS DE region_efectiva A 1920x1080
def obtener_valores_calibracion_region_efectiva(region_efectiva, pantalla_1920x1080):
	# Coordenadas máximas y mínimas en la pantalla de region_efectiva
	x_min_efectiva, y_min_efectiva = 0, 0
	x_max_efectiva, y_max_efectiva = region_efectiva

	# Coordenadas máximas y mínimas en la pantalla de 1920x1080
	x_min_1920, y_min_1920 = 0, 0
	x_max_1920, y_max_1920 = pantalla_1920x1080

	# Calcular las escalas y desplazamientos necesarios para reescalar las coordenadas
	escala_x = (x_max_1920 - x_min_1920) / (x_max_efectiva - x_min_efectiva)
	escala_y = ((y_max_1920 - y_min_1920) / (y_max_efectiva - y_min_efectiva))

	# print(f"escala x: {escala_x} | escala y: {escala_y}")

	desplazamiento_x = x_min_1920 - x_min_efectiva * escala_x
	desplazamiento_y = y_min_1920 - y_min_efectiva * escala_y

	# print(f"desplazamiento x: {desplazamiento_x} | desplazamiento y: {desplazamiento_y}")
	
	return escala_x, escala_y, desplazamiento_x, desplazamiento_y



# FUNCION "reescalar_coordenadas":
# Se usa para aplicar los factores de escala y desplazamientos
# a las coordenadas introducidas.
# PARAMETROS:
#		x -> Coordenada en x que se quiere escalar
#		y -> Coordenada en y que se quiere escalar
#		escala_x -> Factor de escalado en el eje x
#		escala_y -> Factor de escalado en el eje y
#		desplazamiento_x -> Desplazamiento en el eje x
#		desplazamiento_y -> Desplazamiento en el eje y
#
# Devuelve una tupla de coordenadas (x,y), ya escaladas
def reescalar_coordenadas(x, y, escala_x, escala_y, desplazamiento_x, desplazamiento_y):
    # Reescalar las coordenadas inversamente y aplicar el desplazamiento inverso
    nueva_x = int(x * escala_x + desplazamiento_x)
    nueva_y = int(y * escala_y + desplazamiento_y)

    return nueva_x, nueva_y



# ESCALA Y DESPLAZAMIENTO PARA EL CAMBIO DE LA REGION EFECTIVA A 1920x1080
escala_x_nueva, escala_y_nueva, desplazamiento_x_nueva, desplazamiento_y_nueva = obtener_valores_calibracion_region_efectiva(WEBCAM, PANTALLA_DESTINO)



print(Fore.GREEN+"[######################## SEPARADOR ########################]\n"+Fore.RESET)


pyautogui.FAILSAFE = False


# loop over frames from the video stream
while True:

    # grab the frame from the threaded video file stream, resize
    # it, and convert it to grayscale
    # channels)
    _, frame1 = vs.read()
    frame2 = cv2.flip(frame1, 1)
    frame = cv2.resize(frame2, WEBCAM)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale frame
    rects = detector(gray, 0)

    # print(f"X_max: {X_max} | X_nueva_max: {X_nueva_max} | Y_max: {Y_max} | Y_nueva_max: {Y_nueva_max} | X_min: {X_min} | X_nueva_min: {X_nueva_min} | Y_min: {Y_min} | Y_nueva_min: {Y_nueva_min}")


    # loop over the face detections
    for rect in rects:
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        # extract the left and right eye coordinates, then use the
        # coordinates to compute the eye aspect ratio for both eyes
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        # average the eye aspect ratio together for both eyes
        ear = (leftEAR + rightEAR) / 2.0
        # compute the convex hull for the left and right eye, then
        # visualize each of the eyes
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        # check to see if the eye aspect ratio is below the blink
        # threshold, and if so, increment the blink frame counter
        if ear < EYE_AR_THRESH:
            COUNTER += 1
		# otherwise, the eye aspect ratio is not below the blink
		# threshold
        else:
			# if the eyes were closed for a sufficient number of
			# then increment the total number of blinks
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                TOTAL += 1
                pyautogui.click()
            # reset the eye frame counter
            puntoMedioIzq = [round((leftEye[0][0]+leftEye[3][0])/2) , round((leftEye[0][1]+leftEye[3][1])/2)]
            #print("Punto medio I: " + f'{puntoMedioIzq}')
            #cv2.circle(frame, puntoMedioIzq, 1, (0, 255, 0), 1)
            puntoMedioDech = [round(((rightEye[0][0])+rightEye[3][0])/2), round((rightEye[0][1]+rightEye[3][1])/2)]

            X = round((puntoMedioDech[0]+puntoMedioIzq[0])/2)
            Y = round((puntoMedioDech[1]+puntoMedioIzq[1])/2)

            x_destino, y_destino = reescalar_coordenadas(X, Y, escala_x_nueva, escala_y_nueva, desplazamiento_x_nueva, desplazamiento_y_nueva)

            centro = [x_destino, y_destino]

            print("Centro: " + f'{centro}')

            pyautogui.moveTo(centro[0], centro[1])
            COUNTER = 0
        # draw the total number of blinks on the frame along with
        # the computed eye aspect ratio for the frame
        cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        width  = vs.get(cv2.CAP_PROP_FRAME_WIDTH)   
        height = vs.get(cv2.CAP_PROP_FRAME_HEIGHT)  

    # Centro de la ventana que muestra la cam al tamaño de la region efectiva
    cv2.circle(frame, (round(WEBCAM[0]/2), round(WEBCAM[1]/2)), 1, (0, 255, 0), 1)

    # Muestra la ventana
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # Si se presiona la 'q' o el 'esc' se sale del bucle
    if key == ord("q") or key == 27:
        break
# do a bit of cleanup
cv2.destroyAllWindows()
print(Fore.CYAN+"[INFO] El programa ha finalizado con exito"+Fore.RESET)