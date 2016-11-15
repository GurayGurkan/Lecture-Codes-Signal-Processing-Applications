# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 16:45:14 2016

@author: Guray
"""
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
from numpy.fft import *


M = 500;
n = arange(M);
x = sin(0.4*pi*n);

u100=exp(1j*2*pi*100*n/M)
u400=exp(-1j*2*pi*100*n/M);

p1=sum(x*conjugate(u100))
p2=sum(x*conjugate(u400))

print p1,p2

A = fft(x)

print A[100],A[400]