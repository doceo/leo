from serial import *

try:
	ardSerial = Serial('/dev/ttyACM0',9600)
except:
	print "porta seriale sbagliata"

def invia(comando):
	
	ardSerial.write(comando)
	risposta = ardSerial.readline()
	print risposta
	
