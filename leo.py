#!/usr/bin/python


import subprocess
from face import *
#from movimento import *
from seriale import *
#import window
from serverThread.py import *


#----------
# M A I N
#----------

#avviamo il thread che in autonomia gestisce il server che si mette in ascolto di input
server = startThread(None)


capture = cv.CaptureFromCAM(0)
faceCascade = cv.Load("/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml")

distHold = 0

while (cv.WaitKey(15)==-1):
    img = cv.QueryFrame(capture)
    face = DetectFace(img, faceCascade)
    
    if face:
		print "ciao!"
		
		#il vettore face in quarta posizione (indice 3) contiene il 
		#la lunghezza della diagonale
		dist = face[3]
		#print dist
		
		print face[2]

		#il servo motore dell'assex 
#		rotazione = gira(face[2])
#		print rotazione
		
		#inviamo alla porta seriale le coordinate del punto medio
		invia(str(face[2]))
		
		if (dist < distHold - 9):
			print "stai andando via!"
		
		distHold = dist
		
		if(server.getValue()):
		
			invia(str(askThread(server)))
		
server.stop()
cv.ReleaseCapture(capture)
