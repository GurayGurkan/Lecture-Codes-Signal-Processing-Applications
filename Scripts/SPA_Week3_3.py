# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 16:45:14 2016

@author: Guray
"""
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from numpy.fft import *

fs = 2000.0
M = 1000;
n = arange(M);
x1 = sin(0.25*pi*n);
x2 = cos(0.1*pi*n);
x3 = 0.5;

x = x1 + x2 + x3;

subplot(3,1,1)
plot(n/fs,x1)
xlim([0,0.1])
ylim([-1.5, 1.5])
title('Sinus. component')

subplot(3,1,2)
plot(n/fs,x2)
xlim([0,0.1])
ylim([-1.5, 1.5])
title('Cos. component')

subplot(3,1,3)
plot(n/fs,x)
xlim([0,0.1])
ylim([-3, 3])
title('Summation of components')

figure(2)
k = hstack((arange(0,M/2 +1),arange(-M/2+1,0)))
fr = k*fs/M;
plot(fr,abs(fft(x)))
xlabel('Frequency (Hz)')
grid()

figure(3)
plot(fr,abs(fft(x))/1000)
xlabel('Frequency (Hz)')
grid()

x_2 = x + 1.5;
figure(4)
plot(fr,abs(fft(x_2))/M)
xlabel('Frequency (Hz)')
grid()
ylim([0,2.5])