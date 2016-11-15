# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 19:36:46 2016

@author: Guray
"""

from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from numpy.fft import *
from sounddevice import *



fs=8000.0
t = arange(3*fs)/fs
x1 = sin(2*pi*880*t)
play(x1, samplerate=8000)
x2 = exp(-10*t);
tone = x1*x2
play(tone,samplerate=8000)
figure(1)
plot(t,x2)
xlabel('Time (sec)')
title('Decay function')
xlim([0, 1])
grid(True)
figure(2)
plot(t,tone)
title('Generated decaying tone')
grid(True)
xlim([0,1])


fs = 8000.0;
R = .4*fs ; # echo delay in samples
alfa = .1 ;
num = hstack((1, zeros((R-1)),alfa))
denum = 1;
figure(3)
stem(num);
axis([-200 ,3400, 0 ,1.5]);
xlabel("n (samples)");
ylabel("Amplitude");
title("Impulse response of single echo filter")

from scipy.signal import *

y = lfilter(num, denum, tone)
figure(4)
plot(t,y)
xlabel("Time (sec)")
title("Output of single echo filter")
grid(True)
axis([-.1, 3.1, -1.2 ,1.2])

# Single echo: Frequency Domain

w = linspace(0, 2*pi,1000)
R = 8
alfa = 0.8
H = 1 + alfa*exp(-1j*w*R)
figure(5)
plot(w/pi,sqrt(H*conjugate(H)))
xlabel("$ \Omega _N $ (x pi) ")
title("Magnitude response of single echo filter")

# Using freqz()

b = hstack((1,zeros((R-1)),alfa))
a = 1
w, H = freqz(b,a) # calculation,
figure(6)
plot(w/pi, abs(H))
xlabel("$ \Omega _N $ (x pi) ")

# Slide 35

fs=44100.0
R = int(0.25*fs)
alfa = 0.4
b = hstack((1,zeros((R-1)),alfa))
w = linspace(0, 2*pi/2000, 1000) # almost 0 - 22 Hz with 1000 elements
H = 1 + alfa*exp(-1j*w*R)
fr = w*fs/(2*pi)
figure(7)
plot(fr, abs(H))
xlabel('Frequency (Hz)')
ylim([0,2])
grid(True)
# Multiple Echo

fs = 8000.0 ;
N = 5;
alpha = 0.4;
R = int(0.5*8000);
b2= hstack((1, zeros((R*N-1)),-power(alpha, N)))
a2= hstack((1,zeros((R-1)), -alpha));

# --- filtering
y2 = lfilter(b2,a2,tone)
figure(8)
plot(t,y2)
xlabel('Time (sec)')
play(y2,samplerate = 8000)


# frequency response
fs = 8000.0
w = linspace(0, 2*pi/1000, 2000) # 0 - 8 Hz with 1000 elements
H2 = (1 - power(alpha, N)*exp(-1j*R*N*w))/(1 -alpha*exp(-1j*R*w))
figure(9)
plot(w*fs/(2*pi), abs(H2))
title("Multiple Echo Filter: R=4000,alpha=0.4,fs=8000 Hz,N=5")
xlabel('Frequency (Hz)')
ylim([0,2])
grid(True)
ylabel('|H(e$^{jw}$)|')