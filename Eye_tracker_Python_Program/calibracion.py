#################################################################
#                                                               #
#               Jorge Enrique González Gonzalo                  #
#                                                               #
#################################################################

#################################################################
#   Python 3.9.7                                                #
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
# 			Ninguna por ahora									#
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

# Tratamiento de ficheros .csv
import csv

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


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="Direccion del predictor de puntos de referencia faciales")
args = vars(ap.parse_args())


# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold
EYE_AR_THRESH = 0.20
EYE_AR_CONSEC_FRAMES = 5
# initialize the frame counters and the total number of blinks
COUNTER = 0
TOTAL = 0

# Iniciando el detector de cara de dlib (HOG-based) y cargando el
# predictor de puntos de referencia faciales
print("[INFO] Cargando el predictor de puntos de referencia faciales...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])



# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]



# start the video stream thread
print("[INFO] Iniciando hilo de transmisión de video...")
vs = cv2.VideoCapture(0)


time.sleep(1.0)

pyautogui.moveTo(round(ancho/2), round(alto/2))


inicio = time.time()
# FICHERO DE COORDENADAS
diferencia = 0.0
with open('coordenadas.csv', 'w', newline='') as archivo_csv:
	writer_csv = csv.writer(archivo_csv)
	# loop over frames from the video stream
	# while True:
	while diferencia < 15.0 :
		
		_, frame1 = vs.read()
		frame2 = cv2.flip(frame1, 1)
		frame = cv2.resize(frame2, (ancho, alto))
		#frame = imutils.resize(frame, width=450)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# detect faces in the grayscale frame
		rects = detector(gray, 0)

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

				centro = [X, Y]

				# Para calibrar
				writer_csv = csv.writer(archivo_csv)
				writer_csv.writerow(centro)

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
			
			#print("Puntos medios: \nIzq= " + f'{leftEye[0]}' + f'{leftEye[3]}' + " \nDech= " + f'{rightEye[0]}' + f'{rightEye[3]}')

		cv2.circle(frame, (round(ancho/2), round(alto/2)), 1, (0, 255, 0), 2)
		# show the frame
		# cv2.rectangle(frame, (250, 200), (390, 280), (255, 0, 0), 0)
		cv2.rectangle(frame, (round(ancho*0.25), round(alto*0.40)), (round(ancho*0.75), round(alto*0.60)), (255, 0, 0), 0)
		cv2.namedWindow("Frame" , cv2.WND_PROP_FULLSCREEN)    
		cv2.setWindowProperty("Frame" ,
					cv2.WND_PROP_FULLSCREEN,
					cv2.WINDOW_FULLSCREEN)
		cv2.imshow('Frame', frame)
		key = cv2.waitKey(1) & 0xFF
		fin = time.time()
		diferencia = fin-inicio
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break

with open('coordenadas.csv', 'r+') as archivo_csv:
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

Coordenadas = [X_max, X_min, Y_max, Y_min]
with open("coordenadas_max_min.csv", "wt", newline="") as archivo_coor:
	writer_csv = csv.writer(archivo_coor)
	writer_csv.writerow(Coordenadas)


print("X_max: " + f'{X_max}' + " | X_min: " + f'{X_min}' + " | Y_max: " + f'{Y_max}' + " | Y_min: " + f'{Y_min}')

# do a bit of cleanup
text = "Calibración completada correctamente"
print(text)
cv2.destroyAllWindows()