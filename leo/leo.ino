
#include <Servo.h>

int triggerPort=A3;    // Il trigger viene collegato alla porta A3 .
int echoPort = A5;     // il sensore echo viene collegato alla porta A5 .

int distanza;

Servo serX;
Servo serY;

String msg, oldMsg;
char messaggio[10];

int X, angX;
int Y, angY;

boolean go = false;

void setup() {
Serial.begin(9600); // set the baud rate

  serX.attach(9);
  serY.attach(10);
  
  serX.write(90);
  serY.write(90);

  serX.writeMicroseconds(700);
  serY.writeMicroseconds(700);

}
void loop() {


  if(Serial.available()) {
    
    msg = Serial.readString();
    if(msg.equals("start")){
      go = true;
      }
    if(msg.equals("stop")){
      go = false;
      }
    }
   

  if (go == true) muoviRand();
   
  if (msg!=oldMsg) {

      Serial.print(msg);
      Serial.println("  ack"); 
      msg.toCharArray(messaggio, 10);
      
      sscanf (messaggio,"(%d, %d)", &X, &Y);

      angX = map (X, 0, 640, 30, 150);
      angY = map (Y, 0, 420, 60, 130);
      
      serX.write(angX);
      serY.write(angY);
  
      delay(3000);
      oldMsg=msg;
      
      distanza = dist();
      Serial.println("D.");
      Serial.print(distanza);      
  }
       


//delay(900); // delay for 1/10 of a second
}
