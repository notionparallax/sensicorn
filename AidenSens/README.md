# S3 _(version 1)_ Documentation
This document is written for the purposes of documenting the process, hardware, software, firmware, and neccessary files needed to design and use the S3 version 1.

##Hardware
_All part datasheets can be found in Part Documentation_
###Design Decisions
Hardware is needed that can collect indoor environmental information: an "indoor weather station".
The hardware device must communicate with a raspberry pi, such that collected sensor data is sent to a server for later analysis.


####Serial Communication
USB communication was chosen as it can be powered by an RPi and is a well know/well documented serial communication method.
Digistump's (link) Digispark Pro design was used as it is open source hardware, is physically small, and uses familiar USB avr/arduino design.

####Sound Detection
Sparkfun's sound detector was chosen to sense sound pressure levels (Volume) and sound waves. Their design is open source hardware and well documented with cheap and accessible electronics components.

####Temperature Detection
A thermistor was chosen for version 1 as it is the most simple and space saving solution
The thermistor/resistor pair was unity gain buffered as an op-amp was availbe in the quad-op-amp used for sound.

####Interface
The SK6812 - An RGB LED with dedicated LED driver IC (similar to Adafruit's Neopixel) was included as a status for 

A power LED and resest button were used for testing purposes.

A 6 pogo pin was used for SPI communication with the AVR chip such that ISP bootloading was possible.

###Design Process
Eagle was used to design the hardware.
Seeed Studio's was used to manufacture and solder all S3 PCBs.

**include:** 
		-BOM 
		-prices
		-how to use Seeed 
		-links to using Eagle
		-testing of parts
		-etc.

_more info_

(Images of eagle files)

##Bootloader
Follow Digistump's [Upload a bootloader to the Pro over ISP](https://digistump.com/wiki/digispark/tutorials/proisp)
The process is essentially the same, however you must use the [correct fuse bits!!](http://electronics.stackexchange.com/questions/280993/how-to-write-bootloader-and-drivers-to-attiny167/ "A question I asked on Electronics Stack Exchange")

###Prerequisites 
You must have Arduino installed. Learn how to install Arduino and the neccessary drivers and packages for micronucleus [here](https://digistump.com/wiki/digispark/tutorials/connecting). (This will be used later for loading programs onto the S3).

For ISP I reccommend the Arduino UNO. _There are other options._

To save soldering 6 times the number of boards you wish to use, I'd reccommend using pogo pins. We have used Sparkfun's [ISP Pogo pin adapter](https://www.sparkfun.com/products/11591).

###Steps: 
1. Download the bootloader for digispark pro (micronucleus) [here](https://digistump.com/wiki/_media/digispark/tutorials/avrdude.zip "probootloader zip file".
	- Extract and place "ProBootloaderR2.hex" in your folder containing avrdude (for me - C:\Program Files (x86)\Arduino\hardware\tools\avr\bin\\). Avrdude is the executable used to bootload.
	- You will also need avrdude.conf in this folder (a version with attiny167) so that avrdude knows what chip it is communicating with.
1. You must now program the Uno such that it is an In-System Programmer (ISP).
	- In the Arduino IDE select _Tools->Programmer->AVR ISP_
	- Now select _Tools->Board->Arduino/Genuino Uno_
	- If you have more than one USB port you must also select the correct COM port for the UNO. _Tools->Port->COMX_ (for me COM6).
	- Now open the ISP program to load. _File->Examples->ArduinoISP->ArduinoISP_.
	- Select _Upload_. The Uno is now ready to bootload!	
1. Connect your SPI pins on the Uno to the correct pins, for the Uno:
	- RST to 10
	- MOSI to 11
	- MISO to 12
	- SCK to 13
	- VCC to 5V
	- GND to GND

	* **NB**: if using the Sparkfun ISP Pogo Pin Adapter, the 6 pins on the S3 do not match the pinout of the ISP adapter. See [file] to match correct pinout for ISP. If you do this incorrectly you will brick the S3.
1. _(optional)_ Connect three LEDs (using a breadboard or otherwise) for status when programming. Connect the error LED to 8 (red), programming communication LED to 7, and heartbeat (power and ISP program status) to 9. Pull down with 330 Ohm. If you do this re-upload the "ArduinISP" program to the Uno.

1. Open a terminal and change directory into you folder containing avrdude.exe, ProBooloader.hex, and avrdude.conf. For me:
		cd C:\Program Files (x86)\Arduino\hardware\tools\avr\bin
	* Connect your pogo pins to the 6 SPI pins, the power LED should light up.
	* 
		avrdude -p attiny167 -c arduino -P COM6 -b 19200 -U lfuse:w:0xff:m -U hfuse:w:0xdf:m -U efuse:w:0xfe:m -U flash:w:ProBootloaderR2.hex:i


NB: This can be done on any operating system. However do avoid attempting this on a Raspberry Pi, there has been multiple issues.

##Drivers
This is OS dependent, as is the Bootloading process.
