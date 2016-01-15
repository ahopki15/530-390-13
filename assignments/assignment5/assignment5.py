#!/usr/bin/env python

import integrator as intr
import numpy as np
import matplotlib.pyplot as plt

PI = 2.*np.arcsin(1)


# For question #1
#a = 0
#b = 2*PI
#N = 10000
#h = (b-a) / (N-1)
#x = np.zeros(N)
#for i in range(N):
#  x[i] = a + i*h
#y1 = np.zeros(N)
#y2 = np.zeros(N)

#y1 = np.sin(x)
#y2 = np.sin(x)
#y3 = np.sin(2.*x)
#y4 = np.sin(8.*x)
#multi = intr.multiply(y4,y4)
#product = intr.trap_d(x,multi)
#print(product)

# For question #2
def eleven(x):
  return np.power(x,11)

def twelve(x):
  return np.power(x,12)

a = 0
b = 1
#N = 1000
 
#print(intr.trap(np.exp, a, b, N))

[x,w] = intr.gauss_leg(0,1,6)
print(intr.gauss_quad(np.exp,x,w))
