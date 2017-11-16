/*
 * Sx3 arduino master code
 *
 * Created: 22.02.2017 2:30:00
 *  Author: Aiden Ray
 *  
 *  TO DO:
 *    - add newline condition for for loops 
 *    - handle invalid syntax and inputs
 *    - clean up loop() (convert to function??)
 *  Use python send.py and receive.py to change led 
 *  > python send.py n700042 receive.py
 *  and sensors:
 *  > python send.py t
 *  > python receive.py
 */ 

#include <WS2812.h>
#include <DigiUSB.h>
#include <string.h>

//define constants
#define PIN_ANALOG_SOUND    7   //Analogue pin is # ADC7
#define PIN_ANALOG_ENVELOPE 2   //Analogue pin is # ADC2
#define PIN_ANALOG_TEMP     3   //Analogue pin is # ADC3
#define PIN_WS2812          10  //Digital in for MISO is 10

#define SIZEOFINSTR         7  //Size of input array 6 for 2 by 2 to select colour (hex), 
                                //1 for command select (e.g. bright purple = nff00ff,
#define NUMLEDS             1   //Number of LEDS, potentially needed for v2
#define BUFFERSIZE          64  //DO NOT CHANGE UNLESS CHANGED IN digiusb.h
                                //Size of USB buffer in which data is read from                                
#define DELAYTIME           10  //delay time in milliseconds
#define NUMPRINT            3   //number of analogue values to print (nd thus average)

#define SERIESRESISTOR      10000

//Initialise variable and inbuilt functions
double  envelope        = 0;
int     oldEnvelope     = 0;
double  sound           = 0;
int     temperatureADC  = 0;
double  temperature     = 0;
int     bInt            = 0; //placeholder for byte concatenation
int     printCnt        = 0;


WS2812 LED(NUMLEDS);        // define LED
cRGB value;                 // define LED structure variable
int i;                      //index variable
char cmd[SIZEOFINSTR];      //command character string
byte cmdb[SIZEOFINSTR - 1]; //command string as bytes to convert from hex to decimal

void setup() {
  LED.setOutput(PIN_WS2812); // Digital Pin 10
  DigiUSB.begin();
  pinMode(PIN_ANALOG_SOUND,INPUT);
  pinMode(PIN_ANALOG_TEMP,INPUT);
}

//  maps char string of hex value pairs to the RGB number
// and assigns to cRGB values
// e.g. given a char string of the form [n|F|F|0|0|3|C] == n, R = 255, G = 0, B = 100 
void npWrite(cRGB value, char * cmd){
        
    //convert strings to bytes data type
    for (i = 1; i < SIZEOFINSTR; i++){
      if (cmd[i] >= '0' && cmd[i] <= '9') {
           cmdb[i-1] = byte(cmd[i] - '0');    
           //DigiUSB.println(cmdb[i-1]);
       } else if (cmd[i] >= 'a' && cmd[i] <= 'f') {
           cmdb[i-1] = byte(cmd[i] - 'a' + 10);
           //DigiUSB.println(cmd[i] - 'a' + 10);
       } else if (cmd[i] >= 'A' && cmd[i] <= 'F') {
           cmdb[i-1] = byte(cmd[i] - 'A' + 10);
           //DigiUSB.println(cmd[i] - 'A  ' + 10);
       } else {
           i = -1; // getting here is bad: it means the character was invalid ************ HANDLE THIS BETTER
           break;
       }  
    } 

    if(i == -1){
      
    } else {
      // bit shift (moves binary values to correct bin place
      cmdb[0] = cmdb[0] << 4;
      cmdb[2] = cmdb[2] << 4;
      cmdb[4] = cmdb[4] << 4;
      //convert to integer and assign to colours
      bInt = cmdb[0] + cmdb[1];
      value.r = bInt;
      
      bInt = cmdb[2] + cmdb[3];
      value.g = bInt;
  
      bInt = cmdb[4] + cmdb[5];
      value.b = bInt;
        
    }
    LED.set_crgb_at(0, value); // Set value at LED found at index 0
    LED.sync(); // Sends the value to the LED
    
}

//declare reset function @ address 0
//
void(* resetFunc) (void) = NULL; 

void loop() {
    
    if(DigiUSB.available()){//DigiUSB.tx_remaining() == BUFFERSIZE) {
      //DigiUSB.println();
      //DigiUSB.println("nc");
      for(i = 0; i < SIZEOFINSTR; i++){
        cmd[i] = DigiUSB.read();
        
      }
      //DigiUSB.println(cmd);
      if(cmd[0] == 't'){
        for(i = 0; i < NUMPRINT; i++){
          temperatureADC = analogRead(PIN_ANALOG_TEMP ); //corresponds to P3
          DigiUSB.print(temperatureADC);
          DigiUSB.println("t");
        }
        printCnt++;
      } else if(cmd[0] == 'e') { 
        for(i = 0; i < NUMPRINT; i++){
          envelope = analogRead(PIN_ANALOG_ENVELOPE);
          DigiUSB.print(envelope);
          DigiUSB.print("e   ");
          DigiUSB.delay(10);
        }
        DigiUSB.println();
        printCnt++;
      } else if(cmd[0] == 's') {
        for(i = 0; i < NUMPRINT; i++){
          sound = analogRead(PIN_ANALOG_SOUND);
          DigiUSB.print(sound);
          DigiUSB.print("s   ");
          DigiUSB.delay(10);
        }
        DigiUSB.println();
        printCnt++;
      } else if (cmd[0] == 'n'){        
         if(DigiUSB.available()){
           DigiUSB.print("-");
           npWrite(value, cmd);
           DigiUSB.print("+");
           //clear cmd
           cmd[0] = '\0';
           printCnt = 0;
         }
      } else if (cmd[0] == 'r'){
          resetFunc();
      } else if(DigiUSB.tx_remaining() != 0){
          DigiUSB.println();
      }
    }
    
    //clear cmd on NUMPRINTth read
    if(printCnt >= NUMPRINT){
        cmd[0] = '\0';
        printCnt = 0;
    }
    
    
    DigiUSB.delay(DELAYTIME);

}

