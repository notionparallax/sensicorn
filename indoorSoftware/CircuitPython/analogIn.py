import analogio
from board import *

pin = analogio.AnalogIn(A8)
print(pin.value)
pin.deinit()
