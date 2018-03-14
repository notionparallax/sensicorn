# V2 PCB Design Checklist


## Temperature
which configuration of thermistor

accuracy and power of current sense resistor

supply current to thermistor? (lower is better for reducing self-heating)

build a low pass filter (mostly 50 Hz noise)

## Sound

## Light
NOA1212 vs photoresistor

accuracy of current sense resisotr
build NOA1212
## ATSAMD21
### Program bootloader
### Cleaning of Power signal
- voltage regulator (is there a cleaner alternative?)
- how clean do I want it?
- power required?
### Clock
find smallest
how accurate does it need to be?

### shifting placement of pins for better routing?

### Serial Wire Debugger (SWD)
SWDIO & SWCLK pins/pads
_Do we want this?_


## Structural Design

what shape?

## PCB Design
Placement order:
1. Sensors
2. MCU (45°?)
3. Crystal oscillator
4. Neopixels/RGB LEDs
5. USB and pinout
6. iterate
7. auto placement!
8. iterate

Routing:
- Analogue
- digital
- ground plane: split star for analogue and digital
- x
- pinout
- autorouting
##
