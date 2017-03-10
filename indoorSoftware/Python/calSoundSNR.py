"""Send lots of commands to the S^3."""
import receive
import send
import sys


def two_hex(intVal):
    """Convert int to simple hex."""
    return str(hex(intVal)[2:])


def sixChar(r, g, b):
    """Take 3 ints and return a value like BADA55."""
    r = two_hex(r).rjust(2, "0")
    g = two_hex(g).rjust(2, "0")
    b = two_hex(b).rjust(2, "0")
    return "{}{}{}".format(r, g, b)


def get_temp():
    """Ask for a value from the thermistor."""
    send.send("t")
    send.send("t")
    send.send("t")
    receive.receive()

def get_envelope():
    """Ask for a value for the envelope value."""
    send.send("e")
    send.send("e")
    send.send("e")
    receive.receive()


def get_sound():
    """Ask for a value for the sound frequency value."""
    send.send("s")
    send.send("s")
    send.send("s")
    receive.receive()


sys.stdout.flush()
while(True):
    get_envelope()
    
"""for i in range(0, 250, 50):
    for j in range(0, 250, 50):
        for k in range(0, 250, 50):
            val = sixChar(i, j, k)
            send.send("n" + val + "\n")
            get_temp()"""