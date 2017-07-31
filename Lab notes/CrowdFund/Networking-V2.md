# Networking V2

## WiFi
Using a Raspberry Pi or WiFi breakout, each S3 transfers data serially to the WiFi module which periodically uploads data.

__Problems:__
- WiFi will most likely _bottleneck_, with potential loss of data, or slowing of WiFi for other uses.
- Sending a _control signal_ (e.g. RGB LED)
- _Time synchronisation_

## RF comms
- [NRF24L01](https://www.sparkfun.com/datasheets/Components/SMD/nRF24L01Pluss_Preliminary_Product_Specification_v1_0.pdf) ~$5
- [RFM69HCW](https://learn.sparkfun.com/tutorials/rfm69hcw-hookup-guide) ~$7
## USB (Ben explain)
[this?](http://www.usb-over-network.com/usb-over-network.html)

## Bluetooth

## Infrared

## XBee
most reliable, but most expensive

## Considerations and Benefits
Low Loading of internet comms

Control signal (sending to modules) RGB LED

Time synchronisation

Real time data and communication

Security (e.g. SSL)
