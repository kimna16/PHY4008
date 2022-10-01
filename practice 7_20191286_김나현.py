# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:38:10 2021

@author: kimna
"""

import numpy as np
import matplotlib.pyplot as pl
import scipy.optimize as op

def func(x):
    return (x-0.5)*(x-0.3)*(x+0.5)


def bracket_zero(f, x1, x2, n_tries=50, epsilon=0.1):
    i=0
    while f(x1)*f(x2)>=0 and i<n_tries:
        x1=x1*(1+epsilon)
        x2=x2*(1-epsilon)
        i+=1
    
    success=False
    if f(x1)*f(x2)<0:
        success=True
        
    return x1, x2, success
 
x_zeros=[]    
for x_try in np.linspace(-1,1,10):
   x1, x2, success=bracket_zero(func,x_try,x_try)
   if success:
    x_zero=op.bisect(func,x1,x2)
    x_zeros.append(x_zero)

pl.scatter(x_zeros, func(np.array(x_zeros)))
print(x1, x2, success)
   
x_vec=np.linspace(-0.75,0.75,100)
y_vec=func(x_vec)
pl.plot(x_vec, y_vec)
pl.plot([-1,1],[0,0])

x_guess=0.5
result=op.minimize(func,x_guess)
print(result)

x_min=result.x
pl.scatter([x_min],[func(x_min)])

x_guess=-0.5
result=op.minimize(lambda x:-func(x),x_guess)
print(result)

x_max=result.x
pl.scatter([x_max],[func(x_max)])



def local_minima(x_vec,f):
    minima=[]
    for n in range(len(x_vec))[1:-1]:
        f_vec=[f(xi) for xi in x_vec[n-1:n+2]]
        if f_vec[1]<=f_vec[2] and f_vec[1]<=f_vec[0]:
            minima.append(x_vec[n])      
    return minima

def approximate_zeros(x_vec,f):
    zeros=[]
    for n in range(len(x_vec))[:-1]:
        f_vec=[f(xi) for xi in x_vec[n:n+2]]
        if f_vec[0]*f_vec[1]<=0:
            zeros.append(x_vec[n:n+2])         
    return zeros


approximate_zeros=approximate_zeros(x_vec,func)
zeros=[]
for x_guess in approximate_zeros:
    zeros.append(op.bisect(func,*x_guess))
    
print(zeros)

pl.scatter(zeros,func(np.array(zeros)))
    