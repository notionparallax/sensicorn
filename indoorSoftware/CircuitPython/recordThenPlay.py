import board
import audioio
import audiobusio
import digitalio
import time
import array
import math

buf = bytearray(8000)

print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("recording", time.monotonic())
trigger = digitalio.DigitalInOut(board.A1)
trigger.switch_to_output(value = True)
with audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA) as mic:
    mic.record(buf, len(buf))
trigger.value = False
print("done recording", time.monotonic())

for i in buf[:10]:
    print(i)
print(min(buf), max(buf))
time.sleep(0.1)

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value = True)
trigger.value = True

length = 16000 // 440
b = array.array("H", [0] * length)
for i in range(length):
    b[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15 - 1) + (2 ** 15))

print(b)
with audioio.AudioOut(board.SPEAKER, b) as sample:
    sample.play(loop=True)
    time.sleep(1)
    sample.stop()

trigger.value = False

time.sleep(1)

trigger.value = True
print("playback", time.monotonic())
with audioio.AudioOut(board.SPEAKER, buf) as speaker:
    speaker.frequency = 8000
    speaker.play()
    while speaker.playing:
        pass

trigger.value = False
