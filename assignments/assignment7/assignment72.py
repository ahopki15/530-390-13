#!usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import assignment71 as a71

L = 1
U = 1
mu = 1
T = .1

Ny = 100
dy = L/(Ny-1)
dt = .00001
Nt = round(T/dt + 1)

t = np.zeros(Nt)
y = np.zeros(Ny)
u = np.zeros([Nt,Ny])

for i in range(Ny):
  y[i] = i*dy

i = 1
while (i < Nt):
  t[i] = t[i] + dt
  u[i,:] = a71.couette_flow(u[i-1,:],U,mu,dt,dy)
  u[i,0] = -U
  u[i,Ny-1] = U
  i = i + 1

plt.plot(u[round(Nt/8),:],y,u[round(Nt/4),:],y,u[round(Nt/2),:],y,u[Nt-1,:],y)
plt.show()
