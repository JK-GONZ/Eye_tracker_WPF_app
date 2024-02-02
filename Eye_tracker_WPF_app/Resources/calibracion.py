#################################################################
#                                                               #
#               Jorge Enrique González Gonzalo                  #
#                                                               #
#################################################################

#################################################################
#   Python 3.10.8                                               #
#	• Programa de calibración:									#
#		Funcionamiento:											#
#			Lanza la aplicacion en la que se reconocen los ojos	#
#			y el maximo recorrido de la persona que va a usar	#
#			la aplicación, guarda las coordenadas del			#
#			reconocimiento en un archivo .csv y analiza los		#
#			resultados para dejar reflejado en el archivo		#
#			unicamente los valores maximos y minimos			#
#																#
#		Entradas del programa:									#
# 			--shape-predictor: 									#
#				shape_predictor_68_face_landmarks.dat			#
#																#
#		Salidas del programa:									#
#			Archivo .csv en el que aparecen las coordenadas		#
#			maximas y minimas del movimiento del usuario en		#
#			ambos ejes, x e y.									#
#																#
#################################################################


############################ IMPORTS ############################
# Se usa para lo de la distancia eclideana
from scipy.spatial import distance as dist

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

# Tratamiento de ficheros .csv y .json
import csv
import json

# Para conseguir la anchura y altura de la pantalla del dispositivo
from win32api import GetSystemMetrics





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


# Ancho de la pantalla
ancho = GetSystemMetrics(0)
# Alto de la pantalla
alto = GetSystemMetrics(1)




# Define dos constantes, una para la relacion de aspecto medio
# para indicar el pestañeo y la segunda constante es el numero
# de cuadros donde los marcos del ojo debe estar por debajo del 
# umbral
with open('..\..\..\Resources\config.json', 'r+') as archivo_json:
	datos_json = json.load(archivo_json)
	#print(datos_json["Configuracion"]["cuadros_consecutivos"])
	EYE_AR_THRESH = datos_json["relacion_de_aspecto_pestaneo"]
	EYE_AR_CONSEC_FRAMES = datos_json["cuadros_consecutivos"]
	tiempoEjecucion = datos_json["tiempo_ejecucion"]
	archivo_json.close()


# Inicia el contador de cuadros y el total de pestañeos
COUNTER = 0
TOTAL = 0

# Iniciando el detector de cara de dlib (HOG-based) y cargando el
# predictor de puntos de referencia faciales
print("[INFO] Cargando el predictor de puntos de referencia faciales...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("..\..\..\Resources\shape_predictor_68_face_landmarks.dat")



# toma los índices de los puntos de referencia faciales para la izquierda y derecha
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]



# inicia el hilo de transmisión de video
print("[INFO] Iniciando hilo de transmisión de video...")
vs = cv2.VideoCapture(0)


time.sleep(1.0)

pyautogui.moveTo(round(ancho/2), round(alto/2))


inicio = time.time()
diferencia = 0.0
# FICHERO DE COORDENADAS
with open('..\..\..\Resources\coordenadas.csv', 'wt', newline='') as archivo_csv:
	writer_csv = csv.writer(archivo_csv)
	# bucle para recorrer fotogramas de la transmisión de vídeo
	# durante el tiempo especifico
	while diferencia < float(tiempoEjecucion):
		
		_, frame1 = vs.read()
		frame2 = cv2.flip(frame1, 1)
		frame = cv2.resize(frame2, (ancho, alto))
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# detecta rostros en el fotograma de escala de grises
		rects = detector(gray, 0)

		# bucle para la deteccione de rostros
		for rect in rects:
			# determina los puntos de referencia faciales para la región de la cara
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)
			# extrae las coordenadas de los ojos izquierdo y derecho, luego usa las 
			# coordenadas para calcular la relación de aspecto de los ojos para ambos ojos
			leftEye = shape[lStart:lEnd]
			rightEye = shape[rStart:rEnd]
			leftEAR = eye_aspect_ratio(leftEye)
			rightEAR = eye_aspect_ratio(rightEye)
			# media de la relacion de aspecto de ambos ojos
			ear = (leftEAR + rightEAR) / 2.0
			# Calcule el casco convexo para el ojo izquierdo y derecho, 
			# luego visualice cada uno de los ojos.
			leftEyeHull = cv2.convexHull(leftEye)
			rightEyeHull = cv2.convexHull(rightEye)
			cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
			cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
			
			# verifiqua si la relación de aspecto del ojo está por debajo del umbral 
			# de parpadeo y, de ser así, incrementa el contador de fotogramas de 
			# parpadeo
			if ear < float(EYE_AR_THRESH):
				COUNTER += 1
			# de lo contrario, la relación de aspecto del ojo 
			# no está por debajo del umbral de parpadeo
			else:
            # si los ojos estuvieron cerrados durante un número 
            # suficiente de tiempo incrementa el número total de parpadeos
				if COUNTER >= int(EYE_AR_CONSEC_FRAMES):
					TOTAL += 1
					pyautogui.click()

				puntoMedioIzq = [round((leftEye[0][0]+leftEye[3][0])/2) , round((leftEye[0][1]+leftEye[3][1])/2)]
				puntoMedioDech = [round(((rightEye[0][0])+rightEye[3][0])/2), round((rightEye[0][1]+rightEye[3][1])/2)]

				X = round((puntoMedioDech[0]+puntoMedioIzq[0])/2)
				Y = round((puntoMedioDech[1]+puntoMedioIzq[1])/2)

				centro = [X, Y]

				# Para calibrar
				writer_csv = csv.writer(archivo_csv)
				writer_csv.writerow(centro)

				pyautogui.moveTo(centro[0], centro[1])
				COUNTER = 0
			# dibuja el número total de parpadeos en el marco junto con la 
			# relación de aspecto del ojo calculada para el marco
			cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			width  = vs.get(cv2.CAP_PROP_FRAME_WIDTH)   
			height = vs.get(cv2.CAP_PROP_FRAME_HEIGHT)

		# Centro de la ventana
		cv2.circle(frame, (round(ancho/2), round(alto/2)), 1, (0, 255, 0), 2)

		cv2.rectangle(frame, (round(ancho*0.25), round(alto*0.40)), (round(ancho*0.75), round(alto*0.60)), (255, 0, 0), 0)
		cv2.namedWindow("Frame" , cv2.WND_PROP_FULLSCREEN)
		cv2.setWindowProperty("Frame" ,
					cv2.WND_PROP_FULLSCREEN,
					cv2.WINDOW_FULLSCREEN)
		cv2.imshow('Frame', frame)
		key = cv2.waitKey(1) & 0xFF
		fin = time.time()
		diferencia = fin-inicio
		
		if key == ord("q") or key == 27:
			break
archivo_csv.close()

with open('..\..\..\Resources\coordenadas.csv', 'r+') as archivo_csv:
	file_reader = csv.reader(archivo_csv)
	X_max = 0
	X_min = ancho
	Y_max = 0
	Y_min = alto
	for i in file_reader:
		if int(i[0]) < X_max:
			if int(i[0]) < X_min:
				X_min = int(i[0])
		else: 
			X_max = int(i[0])
		
		if int(i[1]) < Y_max:
			if int(i[1]) < Y_min:
				Y_min = int(i[1])
		else: 
			Y_max = int(i[1])
	archivo_csv.close()

Coordenadas = [X_max, X_min, Y_max, Y_min]
with open("..\..\..\Resources\coordenadas_max_min.csv", "wt", newline="") as archivo_coor:
	writer_csv = csv.writer(archivo_coor)
	writer_csv.writerow(Coordenadas)
	archivo_coor.close()


cv2.destroyAllWindows()