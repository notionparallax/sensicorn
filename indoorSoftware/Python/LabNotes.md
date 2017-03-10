## Lab Notes

with a 0.15 second timing at n1e0a82 (step every 10),
fail with error message:

```
Traceback (most recent call last):
  File "test.py", line 33, in <module>
    send.send("n" + val + "\n")
  File "C:\Users\aiden\Documents\BVN\GitHub\sensicorn\indoorSoftware\Python\send.py", line 26, in send
    theDevice.write(ord(c))
  File "C:\Users\aiden\Documents\BVN\GitHub\sensicorn\indoorSoftware\Python\usbdevice.py", line 60, in write
    [])  # ignored
  File "C:\Users\aiden\Documents\BVN\GitHub\sensicorn\indoorSoftware\Python\usbdevice.py", line 80, in _transfer
    value)
  File "C:\Python27\lib\site-packages\usb\core.py", line 1043, in ctrl_transfer
    self.__get_timeout(timeout))
  File "C:\Python27\lib\site-packages\usb\backend\libusb0.py", line 593, in ctrl_transfer
    timeout
  File "C:\Python27\lib\site-packages\usb\backend\libusb0.py", line 431, in _check
    raise USBError(errmsg, ret)
usb.core.USBError: [Errno None] libusb0-dll:err [control_msg] sending control message failed, win error: A device attached to the system is not functioning.
```
