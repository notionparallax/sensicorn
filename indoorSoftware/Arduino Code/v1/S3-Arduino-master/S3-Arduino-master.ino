#include <Adafruit_NeoPixel.h>
#include <DigiUSB.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif


//define constants
#define PIN_ANALOG_SOUND 5
#define PIN_ANALOG_TEMP 3
#define SERIESRESISTOR 10000
#define PIN             10
#define NUMPIXELS      1

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

//Initialise variable and inbuilt functions
double envelope = 0;
int oldEnvelope = 0;
double sound = 0;
int temperatureADC = 0;
double temperature = 0;

void setup() {
  #if defined (__AVR_ATtiny85__)
      if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
  #endif
  pixels.begin();
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
    
//All things temperature
  /*
  pixels.setPixelColor(0, pixels.Color(125,0,125)); // Moderately bright green color.
  pixels.show(); // This sends the updated pixel color to the hardware.
  DigiUSB.delay(500); // Delay for a period of time (in milliseconds).
  */
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

  // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
  pixels.setPixelColor(NUMPIXELS-1, pixels.Color(5,50,75)); // Moderately bright green color.
  pixels.show(); // This sends the updated pixel color to the hardware.
  DigiUSB.delay(500); // Delay for a period of time (in milliseconds).
  
}



