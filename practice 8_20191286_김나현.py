# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:54:48 2021

@author: kimna
"""

import numpy as np
from scipy.integrate import simps, trapz
import matplotlib.pyplot as pl

def f(x):
    return x**2

fig,ax = pl.subplots(1,1)

x=np.arange(0,9,0.01)
y=f(x)
ax.plot(y,x,'k-')

xstep = np.arange(0,10,3)
area=trapz(y,x)
print(area)
ax.fill_between(f(xstep), 0, xstep)

area=simps(y,x)
print(area)

pl.show()
