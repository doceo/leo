//#include <AFMotor.h>

#include <Servo.h>

int triggerPort=A3;    // Il trigger viene collegato alla porta A3 .
int echoPort = A5;     // il sensore echo viene collegato alla porta A5 .

Servo serX;
Servo serY;

String msg, oldMsg;
char messaggio[10];
//AF_DCMotor motorS(1);      // Motore sinistro collegato al pin 1 . 
//AF_DCMotor motorD(4);      // Motore destro collegato al pin 4 .

int X, angX;
int Y, angY;


void setup() {
Serial.begin(9600); // set the baud rate
  serX.attach(9);
  serY.attach(10);
  
  serX.write(90);
  serY.write(90);


}
void loop() {


        if(Serial.available()) msg = Serial.readString();

        int j=random(0,420);
        int i=random(0,640);
        

        Serial.println(j);

        Serial.println(i);

        angX = map (i, 0, 640, 30, 150);
        angY = map (j, 0, 420, 30, 140);
        serX.write(angX);
        serY.write(angY);

        Serial.println(angX);
        Serial.println(angY);
        
        delay(50);      
//        if(Serial.available()){ // only send data back if data has been sent    
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
        }
       


delay(900); // delay for 1/10 of a second
}
