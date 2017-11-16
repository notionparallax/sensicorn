import board
import pulseio
ir_read = pulseio.PulseIn(board.IR_RX, maxlen=100, idle_state=True)

#Press remote control button with it facing the IR receiver.
# Now copy the value out to an array object in a specific 16-bit format:
import array
on_command = array.array('H', [ir_read[x] for x in range(len(ir_read))])

#Finally create a PWM output and PulseOut object to play back the on command above:
# ir_led = pulseio.PWMOut(board.D11, frequency=38000, duty_cycle=2**15) #output LED at 38kHz and 50% Duty cycle
# ir_send = pulseio.PulseOut(ir_led)
# ir_send.send(on_command)
