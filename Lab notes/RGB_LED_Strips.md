# Dot Star Strips

## Software requirements
### Arduino: adafruit dotstar library
For Arduino use
[Download with this link](https://github.com/adafruit/Adafruit_DotStar/archive/master.zip)

### Python library
For Pi/Linux use
[Download here](https://github.com/adafruit/Adafruit_DotStar_Pi/archive/master.zip)


## Hardware and Wiring
SPI bus
### Arduino Pro mini
- 3.3V power ay 8 MHz
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

### Future Consideration
Wifi networking
remote reset
PCBs

## References and Links
[Adafruit Dotstar tutorial](https://learn.adafruit.com/adafruit-dotstar-leds/overview)
[Neopixel LED curtain (adafruit)](https://learn.adafruit.com/1500-neopixel-led-curtain-with-raspberry-pi-fadecandy/overview)
[Adafruit dotstar Pi painter](https://learn.adafruit.com/dotstar-pi-painter/raspberry-pi-setup)
