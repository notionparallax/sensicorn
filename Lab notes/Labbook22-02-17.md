# Lab book 22/02/17

# Actions



### soundADC to dBspl transform

see [this](http://electronics.stackexchange.com/questions/96205/how-to-convert-volts-in-db-spl) stack exchange post gives a good explanation of conversion from an amplified microphone signal.

I wrote some C code in the arduino IDE to do this.
Here are the functions:

```
//converts ADC pin votage to sound pressure levels
//vADC is the analogread from the "envelope pin
//gainR is the gain resistance in Ohms
double vADCtoSPLdB(double vADC, double gainR){
  double gaindB = gaindBtogainR(gainR);

  
  double vcc = 5.00;
  double adcBits = 1023.00;
  
  double pascal1 = 94; // 1 Pascal in dB
  double V = vADC*(vcc/adcBits);//0.004887586; //Volts
  double sensitivity = -40; // dB
  double sensitivityV = pow(10,sensitivity/20); //Vrms/Pa 
  
  double VdB = 20*log10(V/sensitivityV);
  //DigiUSB.println(VdB);
  double SPLdBunity = VdB + sensitivity + pascal1;
  //DigiUSB.println(SPLdBunity);
  double SPLdB = ((SPLdBunity) - (gaindB));
  if (SPLdBunity == gaindB){
    DigiUSB.println("WTF!");
  }
  //DigiUSB.println(SPLdB);
  
  return SPLdB;
}
```
k,.asdgh'.sdgh,l.kasgh