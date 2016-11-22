#face

# http://www.lucaamore.com/?p=638


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
	    print "dentro for"
            # the input to cv.HaarDetectObjects was resized, so scale the
            # bounding box of each face and convert it to two CvPoints
            pt1 = (int(x * image_scale), int(y * image_scale))
            pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
	    
	    
	    #definisco il punto medio e la distanza (non affidabile ancora)
            ptm = ((pt1[0]+pt2[0])/2 ,(pt1[1]+pt2[1])/2)
            dist = math.sqrt((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)
            dist = int(dist)
		#costruisco una tupla di tuple con gli elementi costruiti
        
            points = (pt1, pt2, ptm, dist)
	    
            cv2.rectangle(image, pt1, pt2, (255, 0, 0),2)
  #          grayscale = cv2.CreateImage((width, height), 8, 1)
	    cv2.imshow("rectangle", image)
    
    cv2.imshow("computer vision", image)     
   

    print "prima di return"
    return points
