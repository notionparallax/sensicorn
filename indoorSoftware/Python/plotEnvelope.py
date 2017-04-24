import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# soundFile = open("soundTest.txt")
# sound = soundFile.read()
# print(sound)

with open('soundTest.txt') as soundFile:
  sound = [ int(i) for i in soundFile ]
sound = array(sound)
plt.figure(1)
plt.title('Sound Envelope.')
plt.plot(sound)
plt.show()
