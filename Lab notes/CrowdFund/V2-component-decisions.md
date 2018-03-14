# V2 Component decisions

## temperature sensor
- as simple voltage divider, no low pass or anything!
- 10kOhm highest precision thermistor
- 0.1 - 1% 10kOhm resistor
- connect to 3v3 (VREF/VREG??/VDDIO/VDDIN)

## light sensor
ambient light sensor with sense resistor (10k)
e.g. NOA1212 or APDS9007 etc.
- NOA1212 (analogue)[link](http://www.mouser.com/ds/2/308/NOA1212-D-260440.pdf)
    NOA not common (relatively)
- _APDS-9007_ (analogue)[link](http://www.mouser.com/ds/2/678/V02-0512EN0-908908.pdf)
    1: $1.25
    10: $1.01
    100: $0.811
- APDS-9005
    $1.45
    10: $1.17
    100: $0.944



## Microphone
- digital mems I2S mic:
  all equally as common
  - SPH0645LM4H-B (I2S)
    1: $3.14
    10: $2.72
    25: $2.14
    100: $2.07
  - _SPK0415HM4H-B (PDM)_
    1:	$2.06
    10:	$1.77
    25:	$1.27
    100:	$1.11
  - INMP621ACEZ-R7 (PDM) huge dynamic range = 96 dB
    1: $4.58
    10: $4.13
    25: $3.21
    100: $3.09
  -

## FFC Connector
- HIROSE FH12A 18 [link](http://www.mouser.com/ds/2/185/FH12_catalog-939276.pdf)
    1: $2.21
    10: $2.00
    25: $1.80
    100: $1.72
- Molex 538-52271 18 [link](http://www.mouser.com/ds/2/276/0522712079_FFC_FPC_CONNECTORS-170485.pdf)
    1:	$1.99
    10:	$1.76
    100:	$1.13
## RGB LEDs
- WS2812 (neopixel) 5050

- mini (neopixel) 3535

- APA102-5050 (dotstar)

- APA102-2020 (dotstar)
