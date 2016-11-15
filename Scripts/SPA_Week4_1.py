# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:53:53 2016

@author: Guray
"""

from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from numpy.fft import *

fs=100.0;
n = arange(.5*fs)
t = n/fs
phi1 = 20.0*pi*t; 
phi2 = phi1 +.5*pi;
x=sin(phi1); #to be used later
y=sin(phi2); #to be used later
plot(t,phi1);
grid(True)
hold(True)
plot(t,phi2,'r')
legend(('$\phi_1 (t)$','$ \phi_2(t)$'));
xlabel('Time -Seconds');
ylabel('Radians');
title('Time vs. Insant. Phases')

# diff(x) usage
x = 5*ones((10))
print ' x = ', x

dx = diff(x)
print 'dx = ',dx

print 'Length of  x(n) is ', len(x)
print 'Length of dx(n) is ', len(dx)
#----------------------------------

ang_inst1 = diff(phi1);
ang_inst2 = diff(phi2);
t2=t[:-1] # omit the last element of t
figure(2)
plot(t2, ang_inst1)
hold(True)
plot(t2, ang_inst2,'r')
ylim([0,1 ])
grid(True)
legend(('$\omega_1 (t)$','$\omega_2 (t)$'))
xlabel('Time -Seconds');
ylabel('Radians (???)');

figure(3)
ang_inst1 = ang_inst1*fs
ang_inst2 = ang_inst2*fs
plot(t2, ang_inst1)
hold(True)
plot(t2, ang_inst2,'r')
grid(True)
ylim([0,100])
legend(('$\omega_1 (t)$','$\omega_2 (t)$'))
xlabel('Time -Seconds');
ylabel('Radians');

#---------------------
fs=100.0;
n = arange(fs)
t = n/fs
phi1 = 20.0*pi*t; 
phi2 = 20.0*pi*t*t
x = sin(phi1); #to be used later
y = sin(phi2); #to be used later
figure(4)
plot(t,phi1);
grid(True)
hold(True)
plot(t,phi2,'r')
legend(('$\phi_1 (t)$','$ \phi_2(t)$'));
xlabel('Time -Seconds');
ylabel('Radians');
title('Time vs. Instantaneous Phases')

figure(5)

ang_inst1 = diff(phi1)*fs;
ang_inst2 = diff(phi2)*fs;
t2=t[:-1] 

plot(t2, ang_inst1)
hold(True)
plot(t2, ang_inst2,'r')
grid(True)
legend(('$\omega_1 (t)$','$\omega_2 (t)$'))
ylabel('Rad/s')
xlabel('Time -Seconds');
title('Time vs. Instantaneous Angular Freqs.')

# Inst. Frequencies...
freq_inst1 = ang_inst1 / (2*pi)
freq_inst2 = ang_inst2 / (2*pi)

figure(6)
plot(t2, freq_inst1)
hold(True)
plot(t2, freq_inst2,'r')

grid(True)
legend(('$ f_1 (t) $','$ f_2 (t) $'))
ylim([0,20])
title('Instantaneous Frequencies')
ylabel('Hertz')
xlabel('Time (Sec)')

# NON-linear inst. freq.
from sounddevice import *
fs = 8000.0
n = arange(0,2*fs)
t = n/fs
f_inst = 1000 + 50*sin(4*pi*t)
figure(7)
plot(t,f_inst)
xlabel('Time-seconds')
grid(True)
ylabel('Frequency (Hz)')
x = sin(2000*pi*t-25*cos(4*pi*t))
play(x,samplerate=8000)

# ------------
figure(8)
fs=8000.0;
n=arange(2*fs)
t=n/fs;
phi2 = 2*pi*1000*t-100*cos(2*pi*10*t);
f_inst=diff(phi2)*fs/(2*pi);
t2=t[:-1];
plot(t2,f_inst);
ylim([-100, 2100]);
