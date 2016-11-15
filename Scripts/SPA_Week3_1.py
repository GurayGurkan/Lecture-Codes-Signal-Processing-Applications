# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 16:45:14 2016

@author: Guray
"""
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from numpy.fft import *

fs = 500.0
M = 1000;
n = arange(M);
x = exp(1j*0.02*pi*n)

fft_of_x = fft(x)
k=arange(M)

plot(k,abs(fft_of_x))
xlim([-100 ,1100])
ylim([-10, 1200])
grid()
title('Magnitude plot of fft(x)')
xlabel('k')

figure(2)
k=hstack((arange(M/2+1),arange(-M/2+1,0)))
plot(k,abs(fft_of_x))
xlim([-600 ,600])
ylim([-10, 1200])
grid()
title('Magnitude plot of fft(x)')
xlabel('k')

figure(3)
fr = k*fs/M;
plot(fr,abs(fft_of_x))
xlim([-300 ,300])
ylim([-10, 1200])
grid()
title('Magnitude plot of fft(x)')
xlabel('Frequency (Hz)')