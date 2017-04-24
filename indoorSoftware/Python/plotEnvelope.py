import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

'''
Create an array of samples from sound text file
'''
with open('soundTest.txt') as soundFile:
  sound = [ int(i) for i in soundFile ]

sound = np.array(sound)
'''
Plot the original data (linspace so downsampled is on sample scale)
'''
plt.close('all')
plt.figure(1)
plt.title('Sound Envelope.')
t = np.linspace(0,120,len(sound)) #recored for approx 2 mins
plt.plot(t,sound)

'''
Downsample signal by a factor of 30, i.e. take every 30th sample
'''
downsample = 5
sound2 = signal.decimate(sound,downsample)
t = np.linspace(0,120,len(sound2))
plt.plot(t,sound2)

downsample = 30
sound3 = signal.decimate(sound,downsample)
t = np.linspace(0,120,len(sound3))
plt.plot(t,sound3)

plt.show()
