#!/usr/bin/python


import subprocess
from face import *
from movimento import *
from seriale import °
#import window
 
#----------
# M A I N
#----------


capture = cv.CaptureFromCAM(0)
faceCascade = cv.Load("/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml")

distHold = 0

while (cv.WaitKey(15)==-1):
    img = cv.QueryFrame(capture)
    face = DetectFace(img, faceCascade)
    
    if face:
		print "ciao!"
		
		#il vettore face in quarta posizione (indice 3) contiene il la lunghezza della diagonale
		dist = face[3]
		#print dist
	
		#ricaviamo l'ascissa del punto medio, così da far ruotare il servo motore dell'assex 
		assex = mov_or(face[2][0])
		print assex
		
		#inviamo alla porta seriale l'ascissa del punto medio
		invia(assex)
		
		if (dist < distHold - 9):
			print "stai andando via!"
		
		distHold = dist
		
cv.ReleaseCapture(capture)
