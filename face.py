#face


import cv2
import time
import Image
import math


def DetectFace(image, faceCascade):
 
    min_size = (20,20)
    image_scale = 2
    haar_scale = 1.1
    min_neighbors = 3
    haar_flags = 0

    width = 640
    height = 420
     
    # Allocate the temporary images
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#    print image.width
#    print image.height

    points = 0


    # Detect the faces
    faces =  faceCascade.detectMultiScale(
        	gray,
        	scaleFactor=1.1,
        	minNeighbors=5,
        	minSize=(30, 30),
        	flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    	)
    print "fuori if"
    # If faces are found
  
    for (x, y, w, h) in faces:
	    
	    
            cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0),2)
	    points=(x,y)
	    pm = ((x+x+w/2), (y+y+h/2))
            print pm
  #          grayscale = cv2.CreateImage((width, height), 8, 1)
	    cv2.imwrite("rectangle.jpg", image)
    	    cv2.imshow("face", image)

    print "prima di return"
    return points
