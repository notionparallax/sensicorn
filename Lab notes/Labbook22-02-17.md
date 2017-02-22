# Lab book 22/02/17

## Actions
### Server style implementation
Today I have cracked the issue with writing to digiUSB for the neopoxel/WS2812
An error occured where more than 1 write (change colour) would crash the Sx3


### problem along the way
While attempting this Arduino crashed, and wouldn't reopen. 
A Java error appeared when I ran `Arduino_debug.exe`
```
Loading configuration...
Initializing packages...
Preparing boards...
java.io.FileNotFoundException: C:\Users\aiden\AppData\Roaming\Arduino15\preferences.txt (Access is denied)
    at java.io.FileOutputStream.open0(Native Method)
    at java.io.FileOutputStream.open(FileOutputStream.java:270)
    at java.io.FileOutputStream.(FileOutputStream.java:213)
    at java.io.FileOutputStream.(FileOutputStream.java:162)
    at processing.app.legacy.PApplet.createWriter(PApplet.java:574)
    at processing.app.PreferencesData.save(PreferencesData.java:115)
    at processing.app.Base.(Base.java:343)
    at processing.app.Base.guardedMain(Base.java:226)
    at processing.app.Base.main(Base.java:137)
java.lang.RuntimeException: Couldn't create a writer for C:\Users\aiden\AppData\Roaming\Arduino15\preferences.txt
    at processing.app.legacy.PApplet.createWriter(PApplet.java:586)
    at processing.app.PreferencesData.save(PreferencesData.java:115)
    at processing.app.Base.(Base.java:343)
    at processing.app.Base.guardedMain(Base.java:226)
    at processing.app.Base.main(Base.java:137)
```

I found [this](https://forum.arduino.cc/index.php?topic=167553.60) Arduino forum, and following brillo's solution I deleted prefences.txt and Arduino opened! phew.



### soundADC to dBspl transform

see [this](http://electronics.stackexchange.com/questions/96205/how-to-convert-volts-in-db-spl) stack exchange post gives a good explanation of conversion from an amplified microphone signal.

I wrote some C code in the arduino IDE to do this.
Here are the functions:

```
//function converts resistance gain to gain in decibels
double gaindBtogainR(double gainR){
  //iRes the input resistor (constant in our case)
  //gainR is the feedback gain in which we can change
  //gainR = Rf, iRes = Ri, arithmetic gain = Rf/Ri
  //measure with multimeter
  double iRes = 1000; //1 kOhm
  gainR = gainR/iRes;
  double gaindB = 20*log10(gainR);
  //DigiUSB.println(gaindB);
  return gaindB;
}
```

```
//function converts ADC pin votage to sound pressure levels
//vADC is the analogread from the "envelope pin
//gainR is the gain resistance in Ohms
double vADCtoSPLdB(double vADC, double gainR){
  double gaindB = gaindBtogainR(gainR);

  
  double vcc = 5.00;
  double adcBits = 1023.00;
  
  double pascal1 = 94; // 1 Pascal in dB
  double V = (1/(2*sqrt(2)))*vADC*(vcc/adcBits);//0.004887586; //convert from adc to volts rms
  double sensitivity = -40; // dB
  double sensitivityV = pow(10,sensitivity/20); //Vrms/Pa 
  
  double VdB = 20*log10(V/sensitivityV);
  //DigiUSB.println(VdB);
  double SPLdBunity = VdB + sensitivity + pascal1 + 20*log10((vcc/2)/sensitivityV);
  //DigiUSB.println(SPLdBunity);
  double SPLdB = ((SPLdBunity) - (gaindB));
  if (SPLdBunity == gaindB){
    DigiUSB.println("WTF!");
  }
  //DigiUSB.println(SPLdB);
  
  return SPLdB;
}
```

call functions in "main" (in IDE in void loop)

```
  double vADC = analogRead(PIN_ANALOG_SOUND);
  double gainR = 916000; //465 kOhm

  double SPLdB = vADCtoSPLdB(vADC, gainR);
  DigiUSB.println(SPLdB);
  DigiUSB.delay(500); // Wait X ms
```
I've added 2.5V (in dB) with '+ 20*log10((vcc/2)/sensitivityV)'
this is pretty bad science as the value calculated previously seems to be offset by that exact amount.

There is some logic in it however, have a read on the answer to [this](http://electronics.stackexchange.com/questions/57824/how-do-i-get-5v-for-loud-noise-0v-for-silence-from-electret-microphone-or-oth)
IT IS ALSO A VERY GOOD EXPLANATION OF THE ANALOG ELECTRONCICS WITH
It is also a very good explanation of analogue electronics with **excellent graphics**.

### digiscope: graphing in real time
I edited some python code to graph the sound.
See in /indoorSoftware/Python/Digiscope.py

Seems to offset by 10 and potentially not as sensitive to instantaneuos peak noise.

### Using blink(1)
Resources: A [post](https://digistump.com/board/index.php?topic=1194.0) asking about the viability, it's insightful.
           The blink(1) [github repo](https://github.com/todbot/blink1). It's massive! I need to have a very good long read
           Blink(1) [website](https://blink1.thingm.com/)




### future version
thermistor anmometer or hotwiring for wind
