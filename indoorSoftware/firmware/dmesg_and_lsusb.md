`lsusb`
```
pi@raspberrypi:/usr/bin $ lsusb
Bus 001 Device 005: ID 046d:c077 Logitech, Inc. 
Bus 001 Device 006: ID 413c:2011 Dell Computer Corp. Multimedia Pro Keyboard
Bus 001 Device 004: ID 413c:1005 Dell Computer Corp. Multimedia Pro Keyboard Hub
Bus 001 Device 007: ID 16d0:0753 MCS Digistump DigiSpark
Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. SMSC9512/9514 Fast Ethernet Adapter
Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

pi@raspberrypi:/usr/bin $ lsusb
Bus 001 Device 005: ID 046d:c077 Logitech, Inc. 
Bus 001 Device 006: ID 413c:2011 Dell Computer Corp. Multimedia Pro Keyboard
Bus 001 Device 004: ID 413c:1005 Dell Computer Corp. Multimedia Pro Keyboard Hub
Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. SMSC9512/9514 Fast Ethernet Adapter
Bus 001 Device 002: ID 0424:9514 Standard Microsystems Corp. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

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
usr/bin/avrdude -p attiny167 -c arduino -C /etc/avrdude.conf -b 19200 -P [not sure] -U flash:w:[MyHexFile.ino.hex]:i

error message arduino IDE
```

/home/pi/Downloads/arduino-1.8.1/arduino-builder -dump-prefs -logger=machine -hardware /home/pi/Downloads/arduino-1.8.1/hardware -hardware /home/pi/.arduino15/packages -tools /home/pi/Downloads/arduino-1.8.1/tools-builder -tools /home/pi/Downloads/arduino-1.8.1/hardware/tools/avr -tools /home/pi/.arduino15/packages -built-in-libraries /home/pi/Downloads/arduino-1.8.1/libraries -libraries /home/pi/Arduino/libraries -fqbn=digistump:avr:digispark-tiny -ide-version=10801 -build-path /tmp/arduino_build_279218 -warnings=none -prefs=build.warn_data_percentage=75 -prefs=runtime.tools.micronucleus.path=/home/pi/.arduino15/packages/digistump/tools/micronucleus/2.0a4 -prefs=runtime.tools.avr-gcc.path=/home/pi/.arduino15/packages/arduino/tools/avr-gcc/4.8.1-arduino5 -verbose /home/pi/sensicorn/sensicorn/indoorSoftware/Arduino Code/neopixel_simple/neopixel_simple.ino
/home/pi/Downloads/arduino-1.8.1/arduino-builder -compile -logger=machine -hardware /home/pi/Downloads/arduino-1.8.1/hardware -hardware /home/pi/.arduino15/packages -tools /home/pi/Downloads/arduino-1.8.1/tools-builder -tools /home/pi/Downloads/arduino-1.8.1/hardware/tools/avr -tools /home/pi/.arduino15/packages -built-in-libraries /home/pi/Downloads/arduino-1.8.1/libraries -libraries /home/pi/Arduino/libraries -fqbn=digistump:avr:digispark-tiny -ide-version=10801 -build-path /tmp/arduino_build_279218 -warnings=none -prefs=build.warn_data_percentage=75 -prefs=runtime.tools.micronucleus.path=/home/pi/.arduino15/packages/digistump/tools/micronucleus/2.0a4 -prefs=runtime.tools.avr-gcc.path=/home/pi/.arduino15/packages/arduino/tools/avr-gcc/4.8.1-arduino5 -verbose /home/pi/sensicorn/sensicorn/indoorSoftware/Arduino Code/neopixel_simple/neopixel_simple.ino
Using board 'digispark-tiny' from platform in folder: /home/pi/.arduino15/packages/digistump/hardware/avr/1.6.7
Using core 'tiny' from platform in folder: /home/pi/.arduino15/packages/digistump/hardware/avr/1.6.7
Detecting libraries used...
"/home/pi/.arduino15/packages/arduino/tools/avr-gcc/4.8.1-arduino5/bin/avr-g++" -c -g -Os -w -fno-exceptions -ffunction-sections -fdata-sections  -w -x c++ -E -CC -mmcu=attiny85 -DF_CPU=16500000L -DARDUINO=10801 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR  "-I/home/pi/.arduino15/packages/digistump/hardware/avr/1.6.7/cores/tiny" "-I/home/pi/.arduino15/packages/digistump/hardware/avr/1.6.7/variants/digispark" "/tmp/arduino_build_279218/sketch/neopixel_simple.ino.cpp" -o "/dev/null"
Generating function prototypes...
"/home/pi/.arduino15/packages/arduino/tools/avr-gcc/4.8.1-arduino5/bin/avr-g++" -c -g -Os -w -fno-exceptions -ffunction-sections -fdata-sections  -w -x c++ -E -CC -mmcu=attiny85 -DF_CPU=16500000L -DARDUINO=10801 -DARDUINO_AVR_DIGISPARK -DARDUINO_ARCH_AVR  "-I/home/pi/.arduino15/packages/digistump/hardware/avr/1.6.7/cores/tiny" "-I/home/pi/.arduino15/packages/digistump/hardware/avr/1.6.7/variants/digispark" "/tmp/arduino_build_279218/sketch/neopixel_simple.ino.cpp" -o "/tmp/arduino_build_279218/preproc/ctags_target_for_gcc_minus_e.cpp"
fork/exec /home/pi/.arduino15/packages/arduino/tools/avr-gcc/4.8.1-arduino5/bin/avr-g++: no such file or directory
Error compiling for board Digispark (Default - 16.5mhz).

```
