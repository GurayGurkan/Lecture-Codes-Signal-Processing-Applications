# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:53:53 2016

@author: Guray
"""

from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from numpy.fft import *

#slide 11
t = arange(11)
f = 2*t+5
plot(t,f)
ylim([0,30])
grid(True)
xlabel('Time - (sec)',fontsize=16)
ylabel('Instantaneous Frequency (Hz)',fontsize=16)
title('Plot of $ f(t) = 2t + 5 $')

#slide 13
figure(2)
fs = 100.0
t = arange(10*fs+1)/fs # 1001 samples, exactly 10 seconds.

x = sin(2*pi*t*t+10*pi*t)
plot(t,x)
ylim([-1.5, 1.5])
xlabel('Time (sec)',fontsize=16)
title('$ x(t) = sin(2\pi t^2 + 10\pi t )$',fontsize=17)

figure(3)
subplot(2,2,3)
plot(t,x)
xlim([0,1])
ylim([-1.5,1.5])
title('Interval 0 - 1 sec.',fontsize=16)

subplot(2,2,4)
plot(t,x)
xlim([9,10])
ylim([-1.5,1.5])
title('Interval 9 - 10 sec.',fontsize=16)

subplot(2,1,1)
plot(t,x)
ylim([-1.5,1.5])
title('Whole Data',fontsize=16)

x=x[:-1]
Nwin = 100
m=3
n = arange(Nwin*(m-1),m*Nwin)
win3 = x[n]
figure(4)
plot(n,win3)
title('Data in $3^{rd}$ window')
xlabel('Samples')

figure(5)
M=len(win3)
k = hstack((arange(M/2+1), arange(-M/2+1,0)))
fr = k*fs/M
plot(fr,abs(fft(win3)))
xlabel('Frequency (Hz)')
title('FFT of $3^{rd}$ window')

#3d fft
Nwin=100;
winMat = zeros((10,Nwin))
for m in range(1,11):
    n = arange(Nwin*(m-1),m*Nwin)
    winx = x[n]
    winMat[m-1,:]=abs(fft(winx))
plot(fr, transpose(winMat))
xlabel('Frequency (Hz)')
title('Overlapped plots: FFTs of each window')
ylim([0, 50])

figure(6)
specgram(x, NFFT = 100, Fs= 100, noverlap=0)
xlabel('Time (seconds)')
ylabel('Frequency (Hz)')
    
