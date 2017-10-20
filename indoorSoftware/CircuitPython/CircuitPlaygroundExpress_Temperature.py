# CircuitPlaygroundExpress_Temperature
# reads the on-board temperature sensor and prints the value

import adafruit_thermistor
import board
import time
from analogio import AnalogIn

thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 11371.93, 10000, 25, 3950)
analogin = AnalogIn(board.LIGHT)

while True:
    print("Temperature is: {} C Lux is: {}".format(thermistor.temperature,analogin.value))

    time.sleep(0.25)
