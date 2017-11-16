# Temperature and Humidity (and Pressure)

## Conclusions
Using better design (wheatstone bridge, precise resistors) and a higher bit ADC (the 12-bit SAMD21) we can get enough *temperature* precision with a **Thermistor***.

If Humidity is needed:
HDC1010, but $$$
## Options
- [MCP9808](http://au.mouser.com/Search/Refine.aspx?Keyword=MCP9808) (~$1.80) digital, temp

- [BME 280](http://au.mouser.com/Search/Refine.aspx?Keyword=BME280) (~$9.70) digital, pressure, temp and humidity

- [**thermistor**](https://littlebirdelectronics.com.au/products/thermistor-10k) ($0.142) analogue, temp
- [HTU20D](http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=HPC202_5&DocType=Data+Sheet&DocLang=English) (~$6.00) temp+-0.3C and humidity +-3% I2C

- [SHT-31D (similar to DHT)](http://au.mouser.com/Search/Refine.aspx?Keyword=SHT31-D)($9.25) digital, temp hum

- [Si7021](http://au.mouser.com/Search/Refine.aspx?Keyword=Si7021) (~$6.00) Precision Temp (+-0.4degC) and Humidity (+-3%) digital
- [TMP107](http://au.mouser.com/Search/Refine.aspx?Keyword=TMP107) (~$5.00) precision temp, digital
- [TMP102](http://au.mouser.com/_/?Keyword=TMP102&FS=True)(~$2.00) temp
- [LM234](http://au.mouser.com/Search/Refine.aspx?Keyword=LM234%5c)(~$1.50) temp analogue, constant current source for thermistor
- [LM334](http://au.mouser.com/Search/Refine.aspx?Keyword=LM334D)(~$1.25) temp analogue, constant curent source for thermistor
- [**Si7006**](http://www.mouser.com/ds/2/368/Si7006-A20-736785.pdf)(~$3.00) +-5%RH, +-1 degC
- [**HDC1010**](http://au.mouser.com/Search/Refine.aspx?Keyword=HDC1010)(~4.00) +- 2%RH +-0.2degC, I2C, 2 mm x 1.6 mm footprint
- [MCP9701](http://au.mouser.com/Search/Refine.aspx?Keyword=MCP9701) ($0.357, +-2degC)
- 
## Temp Tutorials
[Precise thermistor (5mK)](https://pa1ejo.wordpress.com/2014/07/25/how-to-build-a-5-milli-kelvin-thermometer-with-an-arduino/)
[underwater temp sensors](https://edwardmallon.wordpress.com/2016/06/09/better-thermistor-readings-with-an-arduino-series-resistors-aref/)
## Pressure
- why? [read this](http://blog.titan-air.com/blog/under-pressure-is-building-air-pressure-really-important)
- potentially more important than humidity
- [indoor air quality](https://www.epa.gov/indoor-air-quality-iaq/fundamentals-indoor-air-quality-buildings)

Sensors:
- MPL3115A2

---

[A good discussion/pointers on thermistors](https://www.reddit.com/r/arduino/comments/5krql4/whats_the_difference_between_1k_10k_and_100k/)
[Wheatstone bridge for thermistor](http://www.ti.com/lit/ml/slyp163/slyp163.pdf)
