# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:50:29 2016

@author: Guray
"""

from numpy import *
from matplotlib import *
from matplotlib.pyplot import *


fs = 100.0;
M = 400;
n = arange(M);
u4 = exp(1j*2*pi*4*n/fs);
u8 = exp(1j*2*pi*8*n/fs);
plot(n/fs, real(u4));
hold(True);
grid(True);
plot(n/fs, imag(u4),'r');
ylim([-3,3])
legend(("Real","Imag"));
xlabel("time - seconds");
title("u_4(n) for f_s=100 Hz, M=400");

figure(num=2);
plot(n/fs, real(u8));
hold(True);
grid(True);
plot(n/fs,imag(u8),'r');
title("u_8(n) for f_s=100 Hz, M=400");
ylim([-3,3]); xlabel("time - seconds");
legend(("Real","Imag"));
show()