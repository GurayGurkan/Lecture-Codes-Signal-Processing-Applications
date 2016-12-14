# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 22:38:49 2016

@author: Guray
"""
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from numpy.fft import *
from scipy.signal import *

# LOWpass
b1 = firwin(3,2*2000/8000.0);
b2 = firwin(13,2*2000/8000.0);
b3 = firwin(41,2*2000/8000.0);

w, H1 = freqz(b1,1)
w, H2 = freqz(b2,1)
w, H3 = freqz(b3,1)

figure(1)
plot(w/pi,abs(H1))
hold(True)
plot(w/pi,abs(H2))
plot(w/pi,abs(H3))
legend(('N=2','N=12','N=40'))
xlabel('$\Omega / \pi$')
ylabel('|H(ejw)|')
grid(True)
title('(FIR) Lowpass filter Frequency Responses for different orders')


# HIGHpass
b1h = firwin(3,2*2000/8000.0,pass_zero=False);
b2h = firwin(13,2*2000/8000.0,pass_zero=False);
b3h = firwin(41,2*2000/8000.0,pass_zero=False);

w, H1 = freqz(b1h,1)
w, H2 = freqz(b2h,1)
w, H3 = freqz(b3h,1)

figure(2)
plot(w/pi,abs(H1))
hold(True)
plot(w/pi,abs(H2))
plot(w/pi,abs(H3))
legend(('N=2','N=12','N=40'))
xlabel('$\Omega / \pi$')
ylabel('|H(ejw)|')
grid(True)
title('(FIR) Highpass filter Frequency Responses for different orders')

# Multi-tone Application

fs = 44100.0
t = arange(3*fs) /fs
comp1 = sin(2*pi*440*t);
comp2 = sin(2*pi*3000*t);
comp3 = sin(2*pi*10000*t);
x = comp1 + comp2 + comp3
x = x /3.0 

figure(3)
subplot(4,1,1)
plot(t,x);xlim([0,0.004])
xlabel('Time (sec)');
ylabel('x');
subplot(4,1,2)
plot(t,comp1);xlim([0,0.004])
ylabel('Comp.1')
subplot(4,1,3)
plot(t,comp2);xlim([0,0.004])
ylabel('Comp.2')
subplot(4,1,4)
plot(t,comp3);xlim([0,0.004])
ylabel('Comp.3')

figure(4)
M = len(x)
fr = arange(M)*fs/M;
plot(fr,abs(fft(x))/M)
xlim([0,12000])

grid(True)
title('Spectrum of x(n)')
xlabel('Frequency (Hz)')


# Lowpass filtering
# fc = 1000 Hz, order 40 selected
b = firwin(41,2*1000/fs)

y1 = lfilter(b,1,x)
figure(5)
plot(t,x)
hold(True)
plot(t,y1)
grid(True)
xlabel('Time (seconds)')
xlim([0, 0.004])
legend(('x(n)','LP filtered'))

# Highpass filtering
# fc = 6000 Hz, order 40 selected
b = firwin(41,2*6000/fs,pass_zero=False)

y2 = lfilter(b,1,x)
figure(6)
plot(t,x)
hold(True)
plot(t,y2)
grid(True)
xlabel('Time (seconds)')
xlim([0, 0.004])
legend(('x(n)','HP filtered'))


# Bandpass filtering
# fc = [1000, 6000] Hz, order 40 selected
b = firwin(41,[2*1000/fs, 2*6000/fs],pass_zero=False)

y3 = lfilter(b,1,x)
figure(7)
plot(t,x)
hold(True)
plot(t,y3)
grid(True)
xlabel('Time (seconds)')
xlim([0, 0.004])
legend(('x(n)','BP filtered'))


