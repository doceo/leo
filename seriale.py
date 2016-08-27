from serial import *

ardSerial = Serial('/dev/ttyACM0',9600)

def invia(comando):
	
	risposta = 0
	
	while (risposta!='ack'):
		ardSerial.write(comando)
		risposta = ardSerial.readline()
		print risposta
		
