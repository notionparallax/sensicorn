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
		- BOM 
		- prices
		- how to use Seeed 
		- links to using Eagle
		- testing of parts
		- etc.

_more info_

(Images of eagle files)

##Bootloader
Follow Digistump's [Upload a bootloader to the Pro over ISP](https://digistump.com/wiki/digispark/tutorials/proisp)
The process is essentially the same, however you must use the [correct fuse bits!!](http://electronics.stackexchange.com/questions/280993/how-to-write-bootloader-and-drivers-to-attiny167/ "A question I asked on Electronics Stack Exchange")

###Prerequisites 
You must have Arduino installed. Learn how to install Arduino and the neccessary drivers and packages for micronucleus [here](http://digistump.com/wiki/digispark/tutorials/connectingpro). (This will be used later for loading programs onto the S3).

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
	* run the following command, (the com port is the USB port for your Uno, see tools->Port to see which one)
		avrdude -p attiny167 -c arduino -P COM6 -b 19200 -U lfuse:w:0xff:m -U hfuse:w:0xdf:m -U efuse:w:0xfe:m -U flash:w:ProBootloaderR2.hex:i
	* you should see the following output, often the RGB LED will light green

		```C:\Program Files (x86)\Arduino\hardware\tools\avr\bin>avrdude -p attiny167 -c arduino -P COM6 -b 19200 -U lfuse:w:0xff:m -U hfuse:w:0xdf:m -U efuse:w:0xfe:m -U flash:w:ProBootloaderR2.hex:i```

	<pre>
	avrdude: AVR device initialized and ready to accept instructions

	Reading | ################################################## | 100% 0.02s

	avrdude: Device signature = 0x1e9487 (probably t167)
	avrdude: NOTE: "flash" memory has been specified, an erase cycle will be performed
	         To disable this feature, specify the -D option.
	avrdude: erasing chip
	avrdude: reading input file "0xff"
	avrdude: writing lfuse (1 bytes):

	Writing | ################################################## | 100% 0.03s

	avrdude: 1 bytes of lfuse written
	avrdude: verifying lfuse memory against 0xff:
	avrdude: load data lfuse data from input file 0xff:
	avrdude: input file 0xff contains 1 bytes
	avrdude: reading on-chip lfuse data:

	Reading | ################################################## | 100% 0.02s

	avrdude: verifying ...
	avrdude: 1 bytes of lfuse verified
	avrdude: reading input file "0xdf"
	avrdude: writing hfuse (1 bytes):

	Writing | ################################################## | 100% 0.06s

	avrdude: 1 bytes of hfuse written
	avrdude: verifying hfuse memory against 0xdf:
	avrdude: load data hfuse data from input file 0xdf:
	avrdude: input file 0xdf contains 1 bytes
	avrdude: reading on-chip hfuse data:

	Reading | ################################################## | 100% 0.02s

	avrdude: verifying ...
	avrdude: 1 bytes of hfuse verified
	avrdude: reading input file "0xfe"
	avrdude: writing efuse (1 bytes):

	Writing | ################################################## | 100% 0.04s

	avrdude: 1 bytes of efuse written
	avrdude: verifying efuse memory against 0xfe:
	avrdude: load data efuse data from input file 0xfe:
	avrdude: input file 0xfe contains 1 bytes
	avrdude: reading on-chip efuse data:

	Reading | ################################################## | 100% 0.02s

	avrdude: verifying ...
	avrdude: 1 bytes of efuse verified
	avrdude: reading input file "ProBootloaderR2.hex"
	avrdude: writing flash (16384 bytes):

	Writing | ################################################## | 100% 0.04s

	avrdude: 16384 bytes of flash written
	avrdude: verifying flash memory against ProBootloaderR2.hex:
	avrdude: load data flash data from input file ProBootloaderR2.hex:
	avrdude: input file ProBootloaderR2.hex contains 16384 bytes
	avrdude: reading on-chip flash data:

	Reading | ################################################## | 100% 0.04s

	avrdude: verifying ...
	avrdude: 16384 bytes of flash verified

	avrdude: safemode: Fuses OK (E:FE, H:DF, L:FF)

	avrdude done.  Thank you.
	</pre>

NB: This process can be done on any operating system. However do avoid attempting to flash a bootloader on a Raspberry Pi, there has been multiple issues, this is the same with any flashing (including code [i.e from arduino IDE]).

##Drivers
This is OS dependent, as is the Bootloading process.
See Digispark [Connecting Pro](http://digistump.com/wiki/digispark/tutorials/connectingpro/) for a guide.

###Windows




##Arduino code


###Neopixel
Our RGB LED is the WS2812B or SK6812RGB.

Do not use [Adafruit_Neopixel library](https://github.com/adafruit/Adafruit_NeoPixel)
This library consumes too much RAM and thus cannot be used concurrently with the DigiUSB library.
Use the [WS2812 Arduino library](https://github.com/cpldcpu/light_ws2812) (#include <WS2812.h>)


##Reading data from USB
- **_ID Vendor_**  is **0x16c0** or 5824 in decimal
- **_ID Product_** is **0x05df** or 1503 in decimal

###Current options
* Use **receive.exe and send.exe** to pipe to text
	- problem with receive only streaming for a short amount of time
	- _edit c++_ code to fix this
	- cannot compile as _make_ dependencies are not met
* Use **DigiUSB.exe**
	- can stream for any amount of time
	- problem with using scroll library -> cannot pipe to file
	- _edit c++_ code to fix
	- cannot compile as _make_ dependencies are not met
* Rubygem
	- Not attempted


### Solution
Downloading DigisparkExamplePrograms from github on RPi
with the appropriate arduino code flashed onto the USB run python "read.py"
	<pre>	sudo python read.py </pre>

##Writing to Neopixel
Using WS2812 and DigiUSB library (see S3-write_np.ino in Arduin Code folder) The 
###Too many sheep not enough RAM

Cannot write to neopixel with DigiUSB library and adafruit_Neopixel library as they seem to be incompatible, potentially a RAM problem. 

See this [github issue](https://github.com/digistump/DigisparkExamplePrograms/issues/4) for detail.







	