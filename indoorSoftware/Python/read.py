#/usr/bin/python
"""
Written for PyUSB 1.0 (w/libusb 1.0.3)

Includes functionality to retrieve string descriptors

Author: follower@rancidbacon.com

Version: 20091021

Assumes 'UsbStreamDemo1.pde' is loaded on Arduino and
LEDs are present on pins 11, 12 and 13.
"""

# import usb  # 1.0 not 0.4
import sys
import time
from usbdevice import atmelUsbDevice


def read():
    print "reading"
    try:
        theDevice = atmelUsbDevice(idVendor=0x16c0,
                                   idProduct=0x05df)

        print "Found: 0x%04x 0x%04x %s %s" % (theDevice.idVendor,
                                              theDevice.idProduct,
                                              theDevice.productName,
                                              theDevice.manufacturer)
    except:
        pass
    max_val = 0
    while True:
    # for i in range(1,1000):
        try:
            theDevice = atmelUsbDevice(idVendor=0x16c0,
                                       idProduct=0x05df)
            try:
                # sys.stdout.write(type(theDevice.read()))
                val = theDevice.read()
                if val > max_val:
                    max_val = val
                eq = "|" * int(val * 0.6)
                print(eq)

                # sys.stdout.flush()
            except:
                # TODO: Check for exception properly
                time.sleep(0.5)

        except:
            # TODO: Check for exception properly
            time.sleep(1)


if __name__ == "__main__":
    read()
