# Trouble with the SAMD21 Xplained board
I bought an atmel ARM Cortex M0+ chip to test for our S3 v2.

The SAMD21 seemed bare bones and relatively straight forward.

## Software requirements
AFter installing the appropriate software in the Arduino IDE by following [these instructions](https://github.com/AtmelUniversityFrance/atmel-samd21-xpro-boardmanagermodule/wiki/GettingStarted:-SAMD21-Xplained-Pro) from Github.

file->Preferences->"Additional Board Managers", then Paste [this](https://github.com/AtmelUniversityFrance/atmel-samd21-xpro-boardmanagermodule/releases/download/v0.3.0/package_atmel-samd21-xpro-boardmanagermodule_0.3.0_index.json)

Tools->Board->Board Manager

install "_Arduino SAMD Boards_, then "_Atmel SAMD21 Xplained-pros_"

## Initial tests
Blinky is to the hardware/MCU world what Hello World is to software world.

Using the Blink example, and changing to pin 13
```
// the setup function runs once when you press reset or power the board
void setup(void)
{
  // initialize digital pin 13 as an output.
  pinMode(PIN_LED_13, OUTPUT);
}

// the loop function runs over and over again forever
void loop(void)
{
  digitalWrite(PIN_LED_13, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(PIN_LED_13, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
}
```
Pin PB01 maps to analogue pin A1

## Serial and Analogue
```
int analogPin0 = A0;
                       // outside leads to ground and +3V3
int val = 0;           // variable to store the value read



void setup()

{

  Serial.begin(57600);          //  setup serial

}



void loop()

{
  analogReadResolution(12);
  analogRead(analogPin1);    // read the input pin
  val = analogRead(analogPin1);
  Serial.println(val);             // debug value
  delay(10);

}
```

## variants.cpp
go into C:\Program Files (x86)\Arduino\portable\packages\atmel-samd21-xpros\hardware\samd\0.3.0\variants\atmel_samd21_xpro_v1\variant.cpp
and edit variants.cpp to select the function of a pin
