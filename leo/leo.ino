//#include <AFMotor.h>

#include <Servo.h>

int triggerPort=A3;    // Il trigger viene collegato alla porta A3 .
int echoPort = A5;     // il sensore echo viene collegato alla porta A5 .

Servo serX;
Servo serY;

String msg;
char messaggio[10];
//AF_DCMotor motorS(1);      // Motore sinistro collegato al pin 1 . 
//AF_DCMotor motorD(4);      // Motore destro collegato al pin 4 .

int X, angX;
int Y, angY;


void setup() {
Serial.begin(9600); // set the baud rate
serX.attach(9);
serY.attach(10);

}
void loop() {


if(Serial.available()){ // only send data back if data has been sent
   	
	// read the incoming data
	msg = Serial.readString();

	// risponde positivamente alla ricezione
  	if (msg) {
  	  Serial.print(msg);
  	  Serial.println("  ack"); 
          msg.toCharArray(messaggio, 10);
          
          sscanf (messaggio,"(%d, %d)", &X, &Y);
 
          angX = map (X, 0, 640, 0, 180);
          angY = map (Y, 0, 420, 0, 180);
          
	  serX.write(angX);
	  serY.write(angY);         
      }
}
delay(100); // delay for 1/10 of a second
}
