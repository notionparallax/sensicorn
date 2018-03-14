import board
import digitalio
import time

led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT
while True:
  led.value = True
  time.sleep(0.1)
  led.value = False
  time.sleep(0.1)
