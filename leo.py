#!/usr/bin/python

import subprocess
from face import *
#from movimento import *
from seriale import *
#import window
from serverThread.py import *

#libreria picamera e picamera.array servono a acquisire dalla webcam un formato array di tipo nunpy per essere trattato da openCV 
from picamera.array import PiRGBArray
from picamera import PiCamera

#----------
# M A I N
#----------

#inizializzo una variabile per scegliere il tipo di acquisizione, se attiva la piCamera deve essere su "True"
piCam = True

#avviamo il thread che in autonomia ascolta possibili input esterni. i client di test sono nella cartella /client
server = startThread(None)

if piCam:
	camera = PiCamera()
	rawCapture = PiRGBArray(camera)
 
	# allow the camera to warmup
	time.sleep(0.1)
 
# grab an image from the camera
	camera.capture(rawCapture, format="bgr")
	capture = rawCapture.array
else:
	capture = cv.CaptureFromCAM(0)
	
faceCascade = cv.Load("/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml")

while (cv.WaitKey(15)==-1):
    img = cv.QueryFrame(capture)
    face = DetectFace(img, faceCascade)
    
    if face:
		print "ciao!"
		
		#stampa a monitor le coordinate del punto medio del volto
		print face[2]

		#inviamo alla porta seriale, quindi ad arduino, le coordinate del punto medio
		invia(str(face[2]))
		
		#controlla il thread del server se ha ricevuto un input esterno
		if(server.getValue()):
		
			invia(str(askThread(server)))

#chiude il server in ascolto
server.stop()
cv.ReleaseCapture(capture)
