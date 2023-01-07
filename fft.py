import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

def create_y(ff,tvec):
    return np.sin(2 * np.pi * ff * tvec)/ff

def upsaw(t):
    y = np.sin(2 * np.pi * 0 * t)
    for i in range(1,100,2):
        y+=create_y(i,t)
        y-=create_y(i+1,t)
    return y

def downsaw(t):
    y = np.sin(2 * np.pi * 0 * t)
    for i in range(1,100):
        y+=create_y(i,t)
    return y
        
def high_square(t):
    y = np.sin(2 * np.pi * 0 * t)
    for i in range(1,100,2):
        y+=create_y(i,t)
    return y

def low_square(t):
    y = np.sin(2 * np.pi * 0 * t)
    for i in range(1,100,2):
        y-=create_y(i,t)
    return y

Fs = 1e4                         # sampling rate
Ts = 1.0/Fs                      # sampling interval
t = np.arange(0,4,Ts)            # time vector
ff = 5                          # frequency of the signal

y = high_square(t)

plt.subplot(2,1,1)
plt.plot(t,y,'k-')
plt.xlabel('time')
plt.ylabel('amplitude')

plt.subplot(2,1,2)
n = len(y)                       # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
freq = frq[range(int(n/2))]           # one side frequency range

Y = np.fft.fft(y)/n              # fft computing and normalization
Y = Y[range(int(n/2))]

plt.plot(freq, abs(Y), 'r-')
plt.xlabel('freq (Hz)')
plt.ylabel('|Y(freq)|')

plt.show() 