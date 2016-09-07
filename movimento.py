#!/usr/bin/python
# al momento rimane non utilizzata
# ma lasciamo in stand by questo modulo per il futuro

def gira(pm):

		fineX = 640
		inizioX = int(fineX/10)
		passoX = inizioX
	
		fineY = 480
		inizioY = int(fineY/10)    
		inizioY
		passoY = inizioY
    
		col = 1;
		rig = 1;
	
		print pm
	
		for i in range (0, fineX, passoX):
		
			if(pm[0] < i):
				break
			col=col+1

		for j in range (0, fineY, passoY):
		
			if(pm[1] < j):
				break
			rig=rig+1
        
		asseXY=(rig, col)
	
		return asseXY
