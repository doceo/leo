
#include <Servo.h>

Servo serX;

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
