#!/usr/bin/python

import subprocess
from face import *
#from movimento import *
from seriale import *
#import window
from serverThread import *
"""
libreria picamera e picamera.array servono a acquisire dalla webcam un formato array di tipo nunpy per essere trattato da openCV 
"""
from picamera.array import PiRGBArray
from picamera import PiCamera

import time
import cv2

#----------
# M A I N
#----------

"""
questa funzionalita non ancora attiva lancia un server che si mette in ascolto sulla porta 9000
server = startThread(None)
"""


camera = PiCamera()
camera.resolution =(640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))

time.sleep(0.1)
	
faceCascade = cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml")

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
# grab the raw NumPy array representing the image, then initialize the timestamp
# and occupied/unoccupied text
        image = frame.array
    
	cv2.imshow("Frame", image)
	cv2.imwrite("frame.jpg", image)
 
	# clear the stream in preparation for the next frame
        rawCapture.truncate(0)

	# dentro questo ciclo dobbiamo andare a richiamare la funzione face
	
        print "visualizzo immagine e richiamo funzione"

        face = DetectFace(image, faceCascade)


        if face:
        	print "ciao!"
		
		#stampa a monitor le coordinate del punto medio del volto
        	print face

		#inviamo alla porta seriale, quindi ad arduino, le coordinate del punto medio
                try:
                        invia(str(face[2]))
		
		#controlla il thread del server se ha ricevuto un input esterno
                        if(server.getValue()):
		
                                invia(str(askThread(server)))
                except:
                        print "nessun arduino collegato"

#chiude il server in ascolto
#server.stop()


