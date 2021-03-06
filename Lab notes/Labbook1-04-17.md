
# Software flashing  attiny167 from RPi with avrdude
## abstract
I am trying to flash a program onto an attiny167
(already bootloaded with the [micronucleus bootloader](https://github.com/micronucleus/micronucleus))
with a Raspberry Pi via avrdude and USB.


## Background
I have 50 Raspberry Pi 3B's connected to an amazon server collecting data.

I have 50 custom attiny167 based USB sensor PCBs which I will connect to the Pis
via USB ([see this previous issue for more detail](http://electronics.stackexchange.com/questions/280993/how-to-write-bootloader-and-drivers-to-attiny167?noredirect=1&lq=1))
It is a struggle to access and connect each device (especially 50 of them),
and I thus need to be able to reflash a program to them via the commandline of an RPi.

I have bootloaded them all from my windows 10 machine and can flash any program via USB.

 ### RPis
 I have flashed programs from the RPi with an Arduino Uno, both with the IDE and avrdude.
 Arduino and avrdude are installed and working (installed both with apt-get).

 The RPi can run an already flashed program, with reading and writing
 possible from the USB device.
 When plugged in the device is viewed by the lsusb command for 5 seconds.
 The pre-flashed program then runs and lsusb shows no device:

 **`lsusb` immediately after device is plugged into port**
 ```
 pi@raspberrypi:/usr/bin $ lsusb
 Bus 001 Device 005: ID 046d:c077 Logitech, Inc.
 Bus 001 Device 006: ID 413c:2011 Dell Computer Corp. Multimedia Pro Keyboard
 Bus 001 Device 004: ID 413c:1005 Dell Computer Corp. Multimedia Pro Keyboard Hub
 Bus 001 Device 007: ID 16d0:0753 MCS Digistump DigiSpark
 Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. SMSC9512/9514 Fast Ethernet Adapter
 Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp.
 Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
  ```
 **`lsusb` ~5 seconds after device is plugged into port**
 ```
 pi@raspberrypi:/usr/bin $ lsusb
 Bus 001 Device 005: ID 046d:c077 Logitech, Inc.
 Bus 001 Device 006: ID 413c:2011 Dell Computer Corp. Multimedia Pro Keyboard
 Bus 001 Device 004: ID 413c:1005 Dell Computer Corp. Multimedia Pro Keyboard Hub
 Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. SMSC9512/9514 Fast Ethernet Adapter
 Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp.
 Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
 ```

 #### udev rules
I have followed the
[tutorial for udev rules by digistump](http://digistump.com/wiki/digispark/tutorials/linuxtroubleshooting)
and placed the file at /etc/udev/rules.d/49-micronucleus.rules

UDEV of [tinseey](https://www.pjrc.com/teensy/49-teensy.rules) (similar to bootloaded micronucleus for attiny167)
```
ViD: 16c0
PiD: 04[789B]?

```
UDEV given by tutorial:
```
ViD: 16d0
PiD: 0753
```
---
- udev rules were incorrect? changed from 16d0 and 0753 to 16c0,05df
- place udev rules in /lib/udev/rules.d/49-micronucleus.rules
- try differnt VID and PID
- - purpose of udev rules
---
I do not fully understand the reason for the udev rules




 ### AVR Device

[this post](http://www.raspberry-pi-geek.com/Archive/2014/03/Adding-analog-input-to-the-Pi-using-the-Digispark/(offset)/2)
hints it may not be possible,
however this issue may have been resolved, as I am using an attiny167 (rather than an 85),
and the Pi does not reboot on the USB being plugged in.

`dmesg`
```
[ 9820.701327] usb 1-1.2: new low-speed USB device number 7 using dwc_otg
[ 9820.803813] usb 1-1.2: New USB device found, idVendor=16d0, idProduct=0753
[ 9820.803838] usb 1-1.2: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[ 9825.208851] usb 1-1.2: USB disconnect, device number 7
[ 9828.001334] usb 1-1.2: new low-speed USB device number 8 using dwc_otg
[ 9833.081359] usb 1-1.2: device descriptor read/64, error -110
[ 9833.271389] usb 1-1.2: device descriptor read/64, error -71
[ 9833.461352] usb 1-1.2: new low-speed USB device number 9 using dwc_otg
[ 9833.541349] usb 1-1.2: device descriptor read/64, error -71
[ 9833.731352] usb 1-1.2: device descriptor read/64, error -71
[ 9833.921349] usb 1-1.2: new low-speed USB device number 10 using dwc_otg
[ 9834.341388] usb 1-1.2: device not accepting address 10, error -71
[ 9834.421361] usb 1-1.2: new low-speed USB device number 11 using dwc_otg
[ 9834.841371] usb 1-1.2: device not accepting address 11, error -71
[ 9834.841480] usb 1-1-port2: unable to enumerate USB device

```


## Arduino IDE
``` avr-g++ error```
install of json file
no serial port shown vs Arduin UNO ttyACM0
on windows it is com 6
`which avr-g++`: /usr/bin/avr-g++

## avrdude
```C:\Program Files (x86)\Arduino\hardware\tools\avr\bin>avrdude -p attiny167 -c arduino -P COM6 -b 19200 -U lfuse:w:0xff:m -U hfuse:w:0xdf:m -U efuse:w:0xfe:m -U flash:w:ProBootloaderR2.hex:i```

```
'which avrdude': /usr/bin.avrdude
```

The Pis are update periodically with a crontab and shell script
on start up

## Serial port
```
usr/bin/avrdude -p attiny167 -c arduino -C /etc/avrdude.conf -b 19200 -P [not sure] -U flash:w:[MyHexFile.ino.hex]:i
```
serial appears with uno and ttyACMO in /dev, not for the AVR device

I have updated the configuration file `avrdude.conf` to include the attiny167,
as I did with my windows 10 machine.
## other heading
prefereably I would continue using the micronucleus as the bootloader as USB compatibility is essential.
However, if you think there is a more suitable bootloader (optiboot?)
I would consider changing.

---
Question
