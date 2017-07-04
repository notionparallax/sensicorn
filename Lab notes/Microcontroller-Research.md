# Microcontroller Research
It's time to get real and write it all in C (f%$@ off IDE)

## TIME STAMP raspberry-pi-setup
[RT Clocl for <$1 AUD](http://au.mouser.com/search/Refine.aspx?Keyword=187530542&Ns=Pricing%7c0&FS=True&Ntk=P_MarCom)

## AVR
[Pro Mini vs Micro](https://arduino.stackexchange.com/questions/4906/all-the-differences-between-arduinos-pro-mini-pro-micro)
## ARM Cortex
- SAM3N based board: [Digikey](https://www.digikey.com/product-detail/en/microchip-technology/ATSAM3N1AB-AU/ATSAM3N1AB-AU-ND/3128688) and [Mouser](http://au.mouser.com/_/?Keyword=AT91SAM&FS=True&Ns=Pricing|0)
- [Datasheet](http://www.mouser.com/ds/2/268/11011s-1065298.pdf)

- [SAM C](http://au.mouser.com/search/Refine.aspx?Keyword=168359589&Ns=Pricing%7c0&FS=True&Ntk=P_MarCom)

- [LPC812](http://au.mouser.com/Search/Refine.aspx?Keyword=LPC812)
-

### SAM family
|ARM CORE|SAM devices|Price (AUD)| Stocked| # I/O|
|---|---|---|---|---|
|M0| SAM D | 1.1 - 4.6 | non - active| 22 - 52 |
|M0+ | SAM C | 2.3 - 5 |non - active | 26 - 52 |
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
