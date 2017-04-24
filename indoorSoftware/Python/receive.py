#/usr/bin/python
"""Written for PyUSB 1.0 (w/libusb 1.0.3)"""


from usbdevice import atmelUsbDevice
import sys
import time
import send


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

        except Exception as e:
            # TODO: Check for exception properly
            print "sreepu", e
            time.sleep(0.1)

    print val.strip()

if __name__ == "__main__":
    receive()
