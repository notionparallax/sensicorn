# /usr/bin/python
# -*- coding: utf-8 -*-
"""
Written for PyUSB 1.0 (w/libusb 1.0.3)

Includes functionality to retrieve string descriptors

Author: follower@rancidbacon.com

Version: 20091021


***
Assumes 'S3-Server-Master.ino' is loaded on Sx3

Further extended by Ben Doherty and Aiden Ray 2017
"""

# import usb  # 1.0 not 0.4
from usbdevice import atmelUsbDevice
import sys
import time


def ensure_end(a_string, end):
    if a_string.endswith(end):
        return a_string
    else:
        return "{}\n".format(a_string)


def read():
    print "reading"
    try:
        theDevice = atmelUsbDevice(idVendor=0x16c0,
                                   idProduct=0x05df)

        # It would be:
        #print "Found: 0x{idVendor:04x} 0x{idProduct:04x} {productName} {manufacturer}".format(**theDevice)
        # If it were a dictionary. I don't have my s×3 on me to check
        print "Found: 0x%04x 0x%04x %s %s" % (theDevice.idVendor,
                                              theDevice.idProduct,
                                              theDevice.productName,
                                              theDevice.manufacturer)
    except:
        pass

    while True:
        try:
            theDevice = atmelUsbDevice(idVendor=0x16c0,
                                       idProduct=0x05df)
            try:
                sys.stdout.write(chr(theDevice.read()))
                sys.stdout.flush()
            except:
                # TODO: Check for exception properly
                time.sleep(0.5)

        except:
            # TODO: Check for exception properly
            time.sleep(1)


def send(args):
    """Send a command to the sensicorn stampeed stick."""
    try:
        theDevice = atmelUsbDevice(idVendor=0x16c0, idProduct=0x05df)
    except:
        sys.exit("No DigiUSB Device Found")

    if args:
        user_input = ensure_end(args, "\n")
        print args
    else:
        exit("No data to send")

    for c in user_input:
        theDevice.write(ord(c))


def receive():
    time.sleep(.2)

    try:
        theDevice = atmelUsbDevice(idVendor=0x16c0, idProduct=0x05df)
    except:
        sys.exit("No DigiUSB Device Found")

    val = ""
    while True:
        try:
            lastChar = chr(theDevice.read())
            if(lastChar == "\n"):
                break
            # sys.stdout.write(lastChar)
            val += lastChar
            sys.stdout.flush()

        except:  # Exception as e:
            # TODO: Check for exception properly
            # print "sreepu", e
            time.sleep(0.1)

    print val.strip()


if sys.argv[1] == "read":
    read()
elif sys.argv[1] == "receive":
    receive()
elif sys.argv[1] == "send":
    try:
        args = sys.argv[2]+"\n"
    except Exception as e:
        args = "BADA55"
    send(args)
else:
    print "You've got things muddled."
