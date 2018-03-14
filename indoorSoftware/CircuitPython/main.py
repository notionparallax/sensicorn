import audiobusio
import board
import array

# Prep a buffer to record into
b = bytearray(200)
with audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA) as mic:
    print(mic)
