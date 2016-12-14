# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 19:36:46 2016

@author: Guray
"""

from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from numpy.fft import *
from scipy.signal import *
#from sounddevice import *

# --- Slide 11
w = linspace(0,2*pi,100);
H = exp(1j*w) - exp(1j*0.4*pi)
magH = sqrt(H*conjugate(H)) #or 
magH = abs(H)
plot(w/pi,magH)
title("Magnitude Plot of single zero filter" )
grid(True)
xlabel("$\Omega / \pi $")

# ------------------

w = linspace(0,2*pi,100);
H2= (exp(1j*w) - exp(1j*0.4*pi))*(exp(1j*w) - exp(-1j*0.4*pi))
magH2 = abs(H2)
figure(2)
plot(w/pi,magH2)
w_2, H2_2 = freqz([1, -2*cos(0.4*pi),1], 1)
figure(3)
plot(w_2/pi, abs(H2_2))
title("Magnitude Plot of double zero filter" )
grid(True)
xlabel("$\Omega / \pi $")


# additional zero at pi

b = convolve([1, -2*cos(0.4*pi),1],[1,1]);
a = [0, 0, 0, 1]
w, H3 = freqz(b,a)
figure(4)
plot(w/pi, abs(H3))
grid(True)
xlabel("$\Omega / \pi $")
title("Magnitude Plot of triple zero filter" )


# POLES

w=linspace(0,2*pi,100);
H = 1/(exp(1j*w) - 0.95*exp(1j*0.2*pi))
magH=abs(H)
figure(5)
plot(w/pi,magH)
xlabel("$\Omega / \pi $")
title("Magnitude plot of single pole filter" )

H2=  1/((exp(1j*w)-.95*exp(1j*0.2*pi))*(exp(1j*w)-.95*exp(-1j*0.2*pi)))
figure(6)
plot(w/pi,abs(H2))
figure(7)
w2, H3 = freqz([0 ,0 ,1],[1, -1.9*cos(0.2*pi), power(.95,2)])
plot(w2/pi,abs(H3))

# impulse response
x = hstack((1,zeros(99)))
b = [0 ,0 ,1];
a = [1, -1.9*cos(0.2*pi), power(.95,2)];
h = lfilter(b,a,x)
figure(8)
plot(h,'-or')
xlabel("Samples")
grid(True)