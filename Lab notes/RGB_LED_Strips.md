# Dot Star Strips

## Software requirements
### Arduino: adafruit dotstar library
For Arduino use
[Download with this link](https://github.com/adafruit/Adafruit_DotStar/archive/master.zip)

### Python library
For Pi/Linux use
[Download here](https://github.com/adafruit/Adafruit_DotStar_Pi/archive/master.zip)


## Wiring and Connections
SPI bus

## Power
- avoid brown out by power tapping:
  add a power tap every meter or so

- Power capacitor

- Level shifter if diectly conencting to Pi logic (3.3V logic) (potentially unnecessary)
### power required
60 mA per LED, constant 5V
I_total = {60e-3 x Num LEDs} Amps

P_required = 5V x I_total.

Num LEDs = 3 x 60 (RGB) + 120 (white)
         = 300 LEDs

Therefore for 300 LEDs

I_total = 18 A
P_required = 5 x 18 = 90 Watts
