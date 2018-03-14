import array
import digitalio
import pulseio
import board
import adafruit_irremote
import time

VOLUMEUP = bytearray(b'*L\x02\x80\xe8j')
VOLUMEDOWN = bytearray(b'*L\x02\x88\xe8b')
remote = adafruit_irremote.GenericTransmit((3350, 1675), (460, 1300), (460, 400), 465)

left = digitalio.DigitalInOut(board.LEFT_BUTTON)
right = digitalio.DigitalInOut(board.RIGHT_BUTTON)
left.switch_to_input(pull=digitalio.DigitalInOut.Pull.DOWN)
right.switch_to_input(pull=digitalio.DigitalInOut.Pull.DOWN)
with pulseio.PWMOut(board.REMOTEOUT, frequency=38000, duty_cycle=2 ** 15) as pwm:
    pulse = pulseio.PulseOut(pwm)
    while True:
        if left.value:
            remote.transmit(pulse, VOLUMEUP)
        if right.value:
            remote.transmit(pulse, VOLUMEDOWN)
