# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import *
from matplotlib import *
from matplotlib.pyplot import *

n = arange(50)
fs = 50.0
t = n/fs
x = 2*sin(2*pi*2*t) + 3
plot(t,x)
xlabel('Time (seconds)')
grid()
title('x(t)')
ylim([0,6])

