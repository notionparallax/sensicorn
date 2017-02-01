#include <WS2812.h>
#include <DigiUSB.h>



#define PIN 10
int incomingByte; //variable to read incoming DigiUSB data

WS2812 LED(1); // 1 LED
  
cRGB value;

void setup() {
  LED.setOutput(10); // Digital Pin 10
   // initialize DigiUSB communication:
  DigiUSB.begin();
}

void loop() {
  // see if there's incoming DigiUSB data:
  if (DigiUSB.available() > 0) {
    // read the oldest byte in the DigiUSB buffer:
    incomingByte = DigiUSB.read();
    // each station has three stages - green/yellow/red
    // each stage of each station has its own letter code

    //station_1 green
    if (incomingByte == 'A') {
      value.b = 255; value.g = 0; value.r = 0; // RGB Value -> Blue
      LED.set_crgb_at(0, value); // Set value at LED found at index 0      
      }

    //station_1 yellow
    if (incomingByte == 'B') {
      value.b = 0; value.g = 255; value.r = 0; // RGB Value -> Blue
      LED.set_crgb_at(0, value); // Set value at LED found at index 0      
      }

    //station_1 red
    if (incomingByte == 'C') {
      value.b = 0; value.g = 0; value.r = 255; // RGB Value -> Blue
      LED.set_crgb_at(0, value); // Set value at LED found at index 0      
      }

    //station_2 green
    if (incomingByte == 'D') {
      value.b = 255; value.g = 255; value.r = 0; // RGB Value -> Blue
      LED.set_crgb_at(0, value); // Set value at LED found at index 0      
      }

    //station_2 yellow
    if (incomingByte == 'E') {
      value.b = 255; value.g = 255; value.r = 255; // RGB Value -> Blue
      LED.set_crgb_at(0, value); // Set value at LED found at index 0      
      }

    //station_2 red
    if (incomingByte == 'F') {
      value.b = 255; value.g = 0; value.r = 255; // RGB Value -> Blue
      LED.set_crgb_at(0, value); // Set value at LED found at index 0      
      }
  }

  LED.sync(); // Sends the value to the LED
  //DigiUSB.delay(500);
  DigiUSB.refresh();
}
