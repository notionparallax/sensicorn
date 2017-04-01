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
