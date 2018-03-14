# Networking V2 and Security
[good breakdown](https://www.rs-online.com/designspark/eleven-internet-of-things-iot-protocols-you-need-to-know-about)
## WiFi
Using a Raspberry Pi or WiFi breakout, each S3 transfers data serially to the WiFi module which periodically uploads data.

__Problems:__
- WiFi will most likely _bottleneck_, with potential loss of data, or slowing of WiFi for other uses.
- Sending a _control signal_ (e.g. RGB LED)
- _Time synchronisation_

Frequencies: 2.4GHz and 5GHz bands
Range: Approximately 50m
Data Rates: 600 Mbps maximum, but 150-200Mbps is more typical, depending on channel frequency used and number of antennas (latest 802.11-ac standard should offer 500Mbps to 1Gbps)

## RF comms
- [NRF24L01](https://www.sparkfun.com/datasheets/Components/SMD/nRF24L01Pluss_Preliminary_Product_Specification_v1_0.pdf) ~$5
- [RFM69HCW](https://learn.sparkfun.com/tutorials/rfm69hcw-hookup-guide) ~$7
## USB (Ben explain)
[this?](http://www.usb-over-network.com/usb-over-network.html)

## Bluetooth
Frequency: 2.4GHz (ISM)
Range: 50-150m (Smart/BLE)
Data Rates: 1Mbps (Smart/BLE)
## Infrared

## ZigBee
most reliable, but most expensive
Frequency: 2.4GHz
Range: 10-100m
Data Rates: 250kbps

## Z-Wave
Frequency: 900MHz (ISM)
Range: 30m
Data Rates: 9.6/40/100kbit/s

## 6LowPAN
Frequency: (adapted and used over a variety of other networking media including Bluetooth Smart (2.4GHz) or ZigBee or low-power RF (sub-1GHz)
Range: N/A
Data Rates: N/A

## Thread
Frequency: 2.4GHz (ISM)
Range: N/A
Data Rates: N/A

## Sigfox
Frequency: 900MHz
Range: 30-50km (rural environments), 3-10km (urban environments)
Data Rates: 10-1000bps


## Neul
Frequency: 900MHz (ISM), 458MHz (UK), 470-790MHz (White Space)
Range: 10km
Data Rates: Few bps up to 100kbps

## LoRaWAN

Frequency: Various
Range: 2-5km (urban environment), 15km (suburban environment)
Data Rates: 0.3-50 kbps
## Considerations and Benefits
Low Loading of internet comms

Control signal (sending to modules) RGB LED

Time synchronisation

Real time data and communication

Security (e.g. SSL)
