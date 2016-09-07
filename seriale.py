from serial import *

ardSerial = Serial('/dev/ttyACM0',9600)

def invia(comando):
	
	ardSerial.write(comando)
	risposta = ardSerial.readline()
	print risposta
	
