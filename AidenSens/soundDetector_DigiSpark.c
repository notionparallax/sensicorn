//Digispark USB/Serial communication
//Run this in DigiSpark edited* Arduino IDE
#include <DigiUSB.h>


#define PIN_ANALOG_IN 5
 int envelope = 0;
 int oldEnvelope = 0;


void setup() {
  DigiUSB.begin();
  pinMode(PIN_ANALOG_IN,INPUT);
}

void loop() {
 
  

  envelope = analogRead(0); //corresponds to P2
  
  if (envelope != oldEnvelope)  {
    //print value
    DigiUSB.println(envelope);
      //for graphing
/*    if(envelope < 20) {
      DigiUSB.println(" ");
    } else if( (envelope >= 20) && (envelope < 30) ) {
      DigiUSB.println(".");
    } else if( (envelope >= 30) && (envelope < 40) ) {
      DigiUSB.println("..");
    } else if( (envelope >= 40) && (envelope < 50) ) {
      DigiUSB.println("...");
    } else if( (envelope >= 50) && (envelope < 60) ) {
      DigiUSB.println("....");
    } else if( (envelope >= 60) && (envelope < 70) ) {
      DigiUSB.println(".....");
    } else if( (envelope >= 70) && (envelope < 80) ) {
      DigiUSB.println("......");
    } else if( (envelope >= 80) && (envelope < 90) ) {
      DigiUSB.println(".......");
    } else if( (envelope >= 90) && (envelope < 100) ) {
      DigiUSB.println("........");
    } else {
      DigiUSB.println(".........");
  
    }*/
  }

  oldEnvelope = envelope;
  
  // pause for 0.1 seconds
  DigiUSB.delay(10);
}
