# Microcontroller Research
## Conclusions
An ARM Cortex Based board is the best option, it allows for superior data analysis and smaller form factor (and thus price) as it can interface with a digital mems mic, minimising microphone external components.

**The SAMD21** (ARM Cortex M0+) is a popular atmel MCU used in multiple Maker boards, and is the cheapest of the SAM Family. It comes in multiple packages, with multiple pins and interfaces.
It has massive support from the Arduino community, with use in the Arduino IDE, and libraries for simple object oriented coding (no C thanks).

Some issues with the SAMD21: It is 3.3V logic, **MORE**


## AVR
[Pro Mini vs Micro](https://arduino.stackexchange.com/questions/4906/all-the-differences-between-arduinos-pro-mini-pro-micro)
## ARM Cortex
- SAM3N based board: [Digikey](https://www.digikey.com/product-detail/en/microchip-technology/ATSAM3N1AB-AU/ATSAM3N1AB-AU-ND/3128688) and [Mouser](http://au.mouser.com/_/?Keyword=AT91SAM&FS=True&Ns=Pricing|0)
- [Datasheet](http://www.mouser.com/ds/2/268/11011s-1065298.pdf)

- [SAM C](http://au.mouser.com/search/Refine.aspx?Keyword=168359589&Ns=Pricing%7c0&FS=True&Ntk=P_MarCom)

- [LPC812](http://au.mouser.com/Search/Refine.aspx?Keyword=LPC812)
-

### SAM family
#### SAMD21 (ARM M0+)
- Arduino Zero
- Arduino MKR1000
- Arduino M0 Pro
- Arduino M0
- Arduino Tian
- Adafruit Feather M0
- Adafruit Circuit Playground Express

#### SAM3N (ARM M3)
- Arduino Due


#### A Comparison

|ARM CORE|SAM devices|Price (AUD)| Stocked| # I/O|
|---|---|---|---|---|
|M0| SAM D | 1.1 - 4.6 | non - active| 22 - 52 |
|M0+ | SAM C, SAM D | 2.3 - 5 |non - active | 26 - 52 |
| M3 | SAM3N | 2.8 - 4.7 | non | 34 - 79 |
| M4 (M3 but with DSP) | |

\*non = non-stocked, this means there is a significant lead time of the components

\*active = stocked with generally no lead time



[Choosing ARM core](https://www.silabs.com/documents/public/white-papers/Which-ARM-Cortex-Core-Is-Right-for-Your-Application.pdf)
## Look into
### V-USB vs Driver specific
### Real time OS/need for an OS
An OS may be useful rather than direct hardware
[ChibiOS](https://en.wikipedia.org/wiki/ChibiOS/RT)
it is compatible with megaAVR
freeRTOS (probably too heavy)

[a comparison of open source OSs](https://en.wikipedia.org/wiki/Comparison_of_open-source_operating_systems )
### USB specific
application specific AVR (USB)

### Communication protocols
multi threading
multi tasking
scheduling
queues/priority

CAN bus (Controller Area Network)

## TIME STAMP raspberry-pi-setup
[RT Clock for <$1 AUD](http://au.mouser.com/search/Refine.aspx?Keyword=187530542&Ns=Pricing%7c0&FS=True&Ntk=P_MarCom)
SAMD21 has inbuilt
