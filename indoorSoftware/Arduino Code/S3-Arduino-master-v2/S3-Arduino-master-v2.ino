/*
 * light_ws2812 example
 *
 * Created: 07.03.2014 12:49:30
 *  Author: Matthias Riegler
 */ 

#include <WS2812.h>
#include <DigiUSB.h>

//define constants
#define PIN_ANALOG_SOUND 5
#define PIN_ANALOG_TEMP 3
#define SERIESRESISTOR 10000

//Initialise variable and inbuilt functions
double envelope = 0;
int oldEnvelope = 0;
double sound = 0;
int temperatureADC = 0;
double temperature = 0;

WS2812 LED(1); // 1 LED
	
cRGB value;

void setup() {
	LED.setOutput(10); // Digital Pin 10
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
   Temp = log(((10240000/RawADC) - 10000));
   //Temp = 1 / (Aone + (Bone*Temp) + (Cone * Temp*Temp) + (Done*Temp*Temp* Temp) );
   Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp ))* Temp );
  
  Temp = Temp - 273.15;              // Convert Kelvin to Celsius
  
  return Temp;
}

void loop() {
	value.b = 50; value.g = 75; value.r = 0; // RGB Value -> Blue
	LED.set_crgb_at(0, value); // Set value at LED found at index 0
	LED.sync(); // Sends the value to the LED



  temperatureADC = analogRead(3); //corresponds to P3
  temperature = Thermister(temperatureADC);

  

  DigiUSB.print(temperature);
  DigiUSB.print("\t");
  //Volume unit?
  envelope = analogRead(2); //corresponds to P5
  DigiUSB.print(envelope);

  DigiUSB.print("\t");
  sound = analogRead(4);
  DigiUSB.println(sound);
  
	DigiUSB.delay(500); // Wait 500 ms
	

}

