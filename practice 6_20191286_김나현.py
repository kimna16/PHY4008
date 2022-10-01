# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:27:09 2021

@author: kimna
"""

import numpy as np

class Complex(object):
    def __init__(self, real, imag):
        self.real=real
        self.imag=imag
        
    def GetData(self):
        print(str(self.real)+'+'+'('+str(self.imag)+')'+'I')
    
    def add(self, other):
        real=self.real+other.real
        imag=self.imag+other.imag
        return Complex(real, imag)
    
    def subtract(self, other):
        real=self.real-other.real
        imag=self.imag-other.imag
        return Complex(real, imag)
    
    def multiply(self, other):
        real=self.real*other.real-self.imag*other.imag
        imag=self.real*other.imag+self.imag*other.real
        return Complex(real,imag)
    
    def divide(self, other):
        real=(self.real*other.real+self.imag*other.imag)/(other.real**2+other.imag**2)
        imag=(self.imag*other.real-self.real*other.imag)/(other.real**2+other.imag**2)
        return Complex(real,imag)
    
    def polarCoordinate(self):
        r=np.sqrt(self.real**2+self.imag**2)
        theta=np.arctan(self.imag/self.real)
        print(r,theta)
    
    def power(self, exponent):
        if (exponent==1):
            return self
        elif (exponent % 1 ==0):
            other=self
            for x in range(1,exponent):
                self=self.multiply(other)
            return self
        else:
            r=np.sqrt(self.real**2+self.imag**2)
            theta=np.arctan(self.imag/self.real)
            print(str(np.power(r,exponent))+'*'+'exp('+str(exponent*theta)+'I'+')')
            
    