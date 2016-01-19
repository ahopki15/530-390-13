#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import assignment61 as a61

# For testing
#A = np.zeros(10)
#for i in range(10):
#  A[i] = i

N = 100000
beta = .4
A = np.zeros(N)
for i in range(N):
  A[i] = a61.exponential(beta)

[X,H] = a61.histogram(A,10)
plt.scatter(X,H)
plt.show()

[I,S] = a61.monte_carlo_3d(a61.density,[-.5,-.5,-1],[1,1,1],a61.sphere,100000)
print(I,S)
