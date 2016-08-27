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
		
		dist = face[3]
		
		#print dist
		assex = mov_or(face[2][0])
		print assex
		invia(assex)
		
		if (dist < distHold - 9):
			print "stai andando via!"
		
		distHold = dist
		
cv.ReleaseCapture(capture)
