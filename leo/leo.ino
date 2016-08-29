#include <AFMotor.h>

#include <Servo.h>

int triggerPort=A3;    // Il trigger viene collegato alla porta A3 .
int echoPort = A5;     // il sensore echo viene collegato alla porta A5 .

Servo serX;

AF_DCMotor motorS(1);      // Motore sinistro collegato al pin 1 . 
AF_DCMotor motorD(4);      // Motore destro collegato al pin 4 .



void setup() {
Serial.begin(9600); // set the baud rate
serX.attach(9);

}
void loop() {

if(Serial.available()){ // only send data back if data has been sent
   	
	// read the incoming data
	char comando = Serial.read();

	// risponde positivamente alla ricezione
  	if (comando) Serial.println("ack"); 
  	
	
	serX.write(comando); 

}
delay(100); // delay for 1/10 of a second
}
