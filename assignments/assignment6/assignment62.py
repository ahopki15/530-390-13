#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import assignment61 as a61

# For testing
#A = np.zeros(10)
#for i in range(10):
#  A[i] = i

#N = 100000
#beta = .4
#A = np.zeros(N)
#for i in range(N):
#  A[i] = a61.exponential(beta)

#[X,H] = a61.histogram(A,10)
#plt.figure()
#plt.scatter(X,H)
#plt.show()
#plt.figure()
#plt.plot(H)
#plt.show()

[I,S] = a61.monte_carlo_3d(a61.density,[-.5,-.5,-1],[1,1,1],a61.sphere,100000)
[x,Sx] = a61.monte_carlo_3d(a61.xmoment,[-.5,-.5,-1],[1,1,1],a61.sphere,100000)
[y,Sy] = a61.monte_carlo_3d(a61.ymoment,[-.5,-.5,-1],[1,1,1],a61.sphere,100000)
[z,Sz] = a61.monte_carlo_3d(a61.zmoment,[-.5,-.5,-1],[1,1,1],a61.sphere,100000)

print(x/I,y/I,z/I)
