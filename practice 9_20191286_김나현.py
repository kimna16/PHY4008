#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:41:56 2021

@author: misari_buljumeok
"""

#1
import scipy.special as sp
import numpy as np
import matplotlib.pyplot as pl
import math

hist1=pl.hist(1.5+0.2*np.random.poisson(3.2,10000),12,density=True)
#a
phi=np.random.rand(10000)
hist1=pl.hist(1.5+0.2*np.sqrt(2.)*sp.erfinv(2.*phi-1.),100,density=True)

#b-1
hist=pl.hist(np.random.randn(10000),100,density=True,cumulative=True)
x_vec=np.linspace(min(hist[1]),max(hist[1]),100)
g_vec=hist[0]
p_inv=lambda g: np.interp(g,g_vec,x_vec)
hist=pl.hist(p_inv(np.random.rand(1000)),100,density=True,cumulative=True)

#2
n_tot=10000
r=1.

x_random,y_random=-1+2*np.random.rand(2,n_tot)

x_inside,y_inside=x_random[x_random**2+y_random**2<r**2],y_random[x_random**2+y_random**2<r**2]
x_outside,y_outside=x_random[x_random**2+y_random**2>r**2],y_random[x_random**2+y_random**2>r**2]

area=len(x_inside)/n_tot*(2*r)**2
print('MC area:',area)