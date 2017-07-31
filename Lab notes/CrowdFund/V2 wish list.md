# V2 wish list
two neopixels, an atmega, temperature, sound, light, humidity*, pressure* (potentially wind).

light and temperature separate from rest of board.

potentially multi layer for multiple clocks, and analogue.

pi zero chord for extension out, potentially a pi-camera

2MHz and 16MHz clocks, two oscillators, or 16 MHz divided

thermistor with 1% tolerances.

on board temperature for thermistor offset.




- atmega
  - 328P
  - 328M

## Sensors
- [DIGITAL HUMIDITY, PRESSURE AND TEMPERATURE SENSOR](http://au.mouser.com/ProductDetail/Bosch-Sensortec/BME280/?qs=sGAEpiMZZMsF1ODjcwEocB0teEbUEBlMe2ty%252bXJvNLw%3D)
  -  2.5 × 2.5 mm² x 0.93 mm
  - humidity
    - Response time 1 s
    - Accuracy tolerance ±3 % relative humidity
    - Hysteresis ±1% relative humidity
  - PRESSURE
    - RMS Noise 0.2 Pa, equiv. to 1.7 cm
    - Offset temperature coefficient ±1.5 Pa/K, equiv. to ±12.6 cm at 1 °C temperature change
  - temperature
    - AT 25 °C ±0.5 °C
    - AT 0…65 °C ±1.0
  - Typical application
    - Context awareness, e.g. skin detection, room change detection
    - Fitness monitoring / well-being
    - Warning regarding dryness or high temperatures
    - Measurement of volume and air flow
    - Home automation control
    - control heating, venting, air conditioning (HVAC)
    - Internet of things
    - GPS enhancement (e.g. time-to-first-fix improvement, dead reckoning, slope detection)
    - Indoor navigation (change of floor detection, elevator detection)
    - Outdoor navigation, leisure and sports applications
    - Weather forecast
    - Vertical velocity indication (rise/sink speed)
- [BME680](https://www.letscontrolit.com/forum/viewtopic.php?t=2067)
  -  25$
  - GAS (VOC) TEMP PRESSURE HUMIDITY
    - [Air Quality indoors by EPA](https://www.epa.gov/indoor-air-quality-iaq/volatile-organic-compounds-impact-indoor-air-quality)
  - [API](https://github.com/BoschSensortec/BME680_driver)


- Digital mems microphone (2.80!!!!!)
  - http://www.mouser.com/ds/2/218/-746191.pdf
  - [analogue vs digital MEMS microphones](http://www.analog.com/media/en/technical-documentation/technical-articles/Analog-and-Digital-MEMS-Microphone-Design-Considerations-MS-2472.pdf)
  -  [I2S mic](http://www.mouser.com/ds/2/218/-746171.pdf)

- light Sensors
  - pi zero camera chord
    - maybe as camera

- [geomagnetic sensor](http://www.mouser.com/ds/2/783/BST-BMM150-DS001-01-786480.pdf)


## Shopping list
- [Atmega 328M]()
- [Pressure sensor module](http://www.auselectronicsdirect.com.au/arduino-pressure-sensor-module-bmp280?gclid=CjwKEAjwl9DIBRCG_e3DwsKsizsSJADMmJ11tKfxi0ezAvWRC9rwPqejMBrH5LOwPU1thV7f3B-ybBoCjWLw_wcB) [OR](https://www.pakronics.com.au/products/adafruit-bmp280-i2c-or-spi-barometric-pressure-altitude-sensor-ada2651?utm_medium=cpc&utm_source=googlepla&variant=5684028801&gclid=CjwKEAjwl9DIBRCG_e3DwsKsizsSJADMmJ11S97aky4vGhfehQ7hGct_5uqy4YmQ6ba3Q63BrHTQCRoCQWDw_wcB)
