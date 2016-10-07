  // la funzione dist() restituisce un valore booleano TRUE se rileva un ostacolo a distanza maggiore di 30cm
  
  int dist(){

  int distMax = 30;  
  int trovato = false;       
    
  digitalWrite (triggerPort, HIGH);   // attraverso il trigger inizia a emettere onde
  delayMicroseconds(10);              // per dieci millisecondi
  digitalWrite(triggerPort,LOW);      // e si ferma

  //attraverso la funzione pulseIn acquisiamo il segnale tramite il sensore
  long duration =pulseIn(echoPort, HIGH); 


  //calcoliamo la distanza
  long int distanza = 0.036 * duration /2;                                 


//stampiamo sul monitor seriale la durata del segnale e la distanza ottenuta
//  Serial.print(" durata: ");                                               
//  Serial.println(duration);
//  Serial.print(" distanza: ");


//segnaliamo se la distanza è fuori dalla portata dello strumento
  if (duration >38000) { 
          Serial.println("fuori portata");                                 
  
  }else { 
//	   Serial.print("D")
//           Serial.print(distanza); 
//           Serial.println ("cm");
//           Serial.println (" ");
         }
         
//evitiamo una divisione per zero, sostituendo lo zero con 1000
if (duration == 0)
   duration == 1000;

//calcoliamo la distanza in centimetri   
   long int rval = microsecondsToCentimeters(duration);                    
 
 
 return rval;

}

long microsecondsToCentimeters(long microseconds)
  {
   int cmconv = 59; 
   return microseconds / cmconv;
  }
  
void muoviRand() {
  
      int j=random(0,420);
      int i=random(0,640);
 
      angX = map (i, 0, 640, 30, 150);
      angY = map (j, 0, 420, 30, 140);
      
      serX.write(angX);
      serY.write(angY);
      
      delay(50);      

}


