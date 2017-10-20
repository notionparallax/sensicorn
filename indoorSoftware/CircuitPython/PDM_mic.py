# record PDM mic to SPI memory
import audiobusio
import board

# Prep a buffer to record into. The array interface doesn't allow for
# constructing with a set size so we append to it until we have the size
# we want.
b = array.array("H")
for i in range(200):
    b.append(0)
with audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, bit_depth=16) as mic:
    mic.record(b, len(b))
