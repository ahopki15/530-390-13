#!/usr/bin/env python
import numpy as np
import assignment4

N =  64.
N2 = N * 2 
A = np.zeros(N2)
B = np.zeros(N2)

for i in range (round(6.*N/10.)):
  if i < round(N/10):
    A[2*i] = 1
    A[2*i+1] = 0
  if   i > round(4.*N/10.):
    B[2*i] = 1
    B[2*i+1] = 0

#print(A)
#print(B)

corr=assignment4.correlation(A,B)

corr = corr * N  / 10

print(corr)
