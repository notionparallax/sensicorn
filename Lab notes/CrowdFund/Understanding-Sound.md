# Understanding Sound

# _**TO DO!!**_
- measure some valuable sound info
  - correct gain (definitely hardware)
  - sampling rate
- implement breathing
- software select delay value
- upload data to AWS
- time??

## Electronics

## Units and Calibration

## Empirical
at maximum gain (1 MOhm), voltage less than 1V (around 200 mV, max 600)

## Tested code
```

//converts resistance gain to gain in decibels
double gaindBtogainR(double gainR){
  //iRes the input resistor (constant in our case)
  //gainR is the feedback gain in which we can change
  //measure with multimeter
  double iRes = 1000; //1 kOhm
  gainR = gainR/iRes;
  double gaindB = 20*log10(gainR);
  //DigiUSB.print(gaindB);
  //DigiUSB.println("gain");

  return gaindB;
}

//converts ADC pin votage to sound pressure levels
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
```

## References and links

[Github "How can I calculate audio dB level"](http://stackoverflow.com/questions/2445756/how-can-i-calculate-audio-db-level)
