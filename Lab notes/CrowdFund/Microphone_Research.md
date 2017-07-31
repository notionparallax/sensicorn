# Microphone
### Condenser Microphone

## Analogue vs Digital
[A very good technical article on Analogue vs digital](http://www.analog.com/media/en/technical-documentation/technical-articles/Analog-and-Digital-MEMS-Microphone-Design-Considerations-MS-2472.pdf), \*consider as reference unless otherwise mentioned.
## Analogue MEMs
- requires amplifier
[general purpose mic amp](http://au.mouser.com/Search/Refine.aspx?Keyword=MAX4465&Ns=Pricing%7c0&FS=True)
2x2 mm footprint (includes legs)-> potentially best option
needs 9 passive elements (R and C)
## Digital MEMs
[Interfacing an I2S Device to a Microcontoller](http://www.ti.com/lit/an/slaa449a/slaa449a.pdf)
### PDM
PDM most common for phones
[A good PDM mic](https://store.invensense.com/datasheets/invensense/INMP621.pdf)
[A good explanation of PDM](http://users.ece.utexas.edu/~bevans/courses/rtdsp/lectures/10_Data_Conversion/AP_Understanding_PDM_Digital_Audio.pdf)
viability:
- [maybe not](https://forum.arduino.cc/index.php?topic=398567.0)


- an interesting [project](https://curiouser.cheshireeng.com/2015/02/11/pdm-to-spl-demonstrated-in-an-lpc810/)
### I2S
[Arduino I2S Library](https://www.arduino.cc/en/Reference/)
