/*
 * Sx3 arduino master code
 *
 * Created: 22.02.2017 2:30:00
 *  Author: Aiden Ray
 */ 

#include <WS2812.h>
#include <DigiUSB.h>
#include <string.h>

//define constants
#define PIN_ANALOG_SOUND 7
#define PIN_ANALOG_ENVELOPE 2
#define PIN_ANALOG_TEMP 3
#define PIN_WS2812 10
#define SIZEOFINSTR 10
#define NUMLEDS 1
#define BUFFERSIZE 64
#define DELAYTIME 10
#define NUMPRINT 4

#define SERIESRESISTOR 10000

//Initialise variable and inbuilt functions
double envelope = 0;
int oldEnvelope = 0;
double sound = 0;
int temperatureADC = 0;
double temperature = 0;

WS2812 LED(NUMLEDS); // 1 LED
	
cRGB value;

int i;
char cmd;

void setup() {
	LED.setOutput(PIN_WS2812); // Digital Pin 10
  DigiUSB.begin();
  pinMode(PIN_ANALOG_SOUND,INPUT);
  pinMode(PIN_ANALOG_TEMP,INPUT);
}

double Thermister(int RawADC) {  //Function to perform the fancy math of the Steinhart-Hart equation
  double Temp;
  int R = 10000;
  double Aone = 0.003354016;
  double Bone = 0.0002569850;
  double Cone = 0.000002620131;
  double Done = 0.00000006383091;
   Temp = log((5500)*((1024/RawADC) - 1));
   //Temp = 1 / (Aone + (Bone*Temp) + (Cone * Temp*Temp) + (Done*Temp*Temp* Temp) );
   Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp ))* Temp );
  
  Temp = Temp - 273.15;              // Convert Kelvin to Celsius
  
  return Temp;
}

void loop() {
	


  temperatureADC = analogRead(PIN_ANALOG_TEMP ); //corresponds to P3
  //temperature = Thermister(temperatureADC); 
  sound = analogRead(PIN_ANALOG_SOUND);
  envelope = analogRead(PIN_ANALOG_ENVELOPE);
  
  
  
    if(DigiUSB.tx_remaining() == BUFFERSIZE) {
      cmd = DigiUSB.read();
      
      
      DigiUSB.println(cmd);
      if(cmd == 't'){
        for(i = 0; i < NUMPRINT; i++){
          DigiUSB.print(temperatureADC);
          DigiUSB.println("t\t");
        }
      } else if(cmd == 'e') { 
        for(i = 0; i < NUMPRINT; i++){
          DigiUSB.print(envelope);
          DigiUSB.println("e\t");
        }
      } else if(cmd == 's') {
        for(i = 0; i < NUMPRINT; i++){
          DigiUSB.print(sound);
          DigiUSB.println("s");
        }
      } 
      if (cmd == 'n'){
        value.b = 0; value.g = 75; value.r = 150; // RGB Value ->  pink
        LED.set_crgb_at(0, value); // Set value at LED found at index 0
        LED.sync(); // Sends the value to the LED        

      } else if (cmd == 'p'){
        value.b = 150; value.g = 0; value.r = 75; // RGB Value ->  pink
        LED.set_crgb_at(0, value); // Set value at LED found at index 0
        LED.sync(); // Sends the value to the LED        

      } else {
        DigiUSB.println(cmd);
      }
    }
    
    //clear cmd
    cmd = '1';
    
    DigiUSB.delay(DELAYTIME);
	  //DigiUSB.refresh();
  //}

}

