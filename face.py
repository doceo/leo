#face

# http://www.lucaamore.com/?p=638


import cv
import time
import Image
import math


def DetectFace(image, faceCascade):
 
    min_size = (20,20)
    image_scale = 2
    haar_scale = 1.1
    min_neighbors = 3
    haar_flags = 0
 
    # Allocate the temporary images
    grayscale = cv.CreateImage((image.width, image.height), 8, 1)
#    print image.width
#    print image.height

    points = 0

    smallImage = cv.CreateImage(
            (
                cv.Round(image.width / image_scale),
                cv.Round(image.height / image_scale)
            ), 8 ,1)
 
    # Convert color input image to grayscale
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)
 
    # Scale input image for faster processing
    cv.Resize(grayscale, smallImage, cv.CV_INTER_LINEAR)
 
    # Equalize the histogram
    cv.EqualizeHist(smallImage, smallImage)
 
    # Detect the faces
    faces = cv.HaarDetectObjects(
            smallImage, faceCascade, cv.CreateMemStorage(0),
            haar_scale, min_neighbors, haar_flags, min_size
        )
 
    # If faces are found
    if faces:
        for ((x, y, w, h), n) in faces:
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
	    
        cv.Rectangle(image, pt1, pt2, cv.RGB(255, 0, 0), 5, 8, 0)
        grayscale = cv.CreateImage((image.width, image.height), 8, 1)
    
    cv.ShowImage("computer vision", image)     
    return points
