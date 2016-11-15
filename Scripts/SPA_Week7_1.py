# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 13:47:36 2016

@author: Guray
"""

from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from numpy.fft import *

fs = 100.0
M=20;
n=arange(M);
x= cos(.9*pi*n)
k = hstack((arange(M/2+1), arange(-M/2+1,0)));
stem(k,abs(fft(x))/M,'r')
grid(True);
ylim([-.01, .75]);
xlim([-11 ,11])
xlabel('FFT bins');
figure(2)
stem(k*fs/M,abs(fft(x))/M,'r')
grid(True);
ylim([-.01, .75]);
xlabel('Frequency (Hz)');
xlim([-55 ,55])

M=40;
n=arange(M);
x= cos(.95*pi*n)
k = hstack((arange(M/2+1), arange(-M/2+1,0)));
figure(3)
stem(k,abs(fft(x))/M,'r')
grid(True);
ylim([-.01, .75]);
xlim([-21 ,21])
xlabel('FFT bins');
figure(4)
stem(k*fs/M,abs(fft(x))/M,'r')
grid(True);
ylim([-.01, .75]);
xlabel('Frequency (Hz)');
xlim([-55 ,55])

M = 40;
n = arange(M);
x = cos(pi*n);
figure(5)
stem(x,'r')
ylim([-1.5, 1.5 ])
xlabel('samples')
xlim([-1, 41])

k = hstack((arange(M/2+1), arange(-M/2+1,0)));
figure(6)
stem(k,abs(fft(x))/M,'r')
grid(True);
ylim([-.01, 1.25]);
xlim([-21 ,21])
xlabel('FFT bins');
figure(7)
stem(k*fs/M,abs(fft(x))/M,'r')
grid(True);
ylim([-.01, 1.25]);
xlabel('Frequency (Hz)');
xlim([-55 ,55])


fs = 22050.0;
n = arange(4*fs);
t = n/fs;
x = cos(2000*pi*t*(t+2))
import sounddevice
#sounddevice.play(x,samplerate=22050)


fs = 8000.0;
n = arange(4*fs);
t = n/fs;
x = cos(2000*pi*t*(t+2))
sounddevice.play(x,samplerate=8000)
figure(8)
specgram(x, NFFT = 1000, Fs= 8000, noverlap=500)
xlabel('Time (seconds)')
ylabel('Frequency (Hz)')