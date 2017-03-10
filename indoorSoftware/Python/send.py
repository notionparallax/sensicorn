#/usr/bin/python
""" Written for PyUSB 1.0 (w/libusb 1.0.3)"""

import sys
from usbdevice import atmelUsbDevice

try:
    args = sys.argv[1]+"\n"
except Exception as e:
    args = "BADA55"

def send(args=args):
    """Send a command to the sensicorn stampeed stick."""
    try:
        theDevice = atmelUsbDevice(idVendor=0x16c0, idProduct=0x05df)
    except:
        sys.exit("No DigiUSB Device Found")

    try:
        user_input = args
        print args
    except:
        exit("No data to send")

    for c in user_input:
        theDevice.write(ord(c))


if __name__ == "__main__":
    send()
