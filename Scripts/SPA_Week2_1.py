# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:46:59 2016

@author: Guray
"""

from numpy import *
from matplotlib import *
from matplotlib.pyplot import *

fs = 60.0;
n = arange(fs); # 60 samples
fr = 3.0;
euler = exp (1j*2*pi*fr*(n/fs));
plot(real(euler));
hold(True)
plot(imag(euler),'r'); # red plotting
title("Real and Complex Parts of Euler")
legend(("Real","Complex"));
grid(True);
ylim([-2, 2]);
show()