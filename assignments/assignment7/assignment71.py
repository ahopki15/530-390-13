import numpy as np

def couette_flow(u,U,mu,dt,dy):
  Ny = len(u)
  tmp = np.zeros(Ny)
  mudtdy2 = mu*dt/(dy*dy)
  tmp[0] = U
  tmp[Ny-1] = -U
  for j in range(1,Ny-1):
    tmp[j] = u[j] + mudtdy2*(u[j+1]-2*u[j]+u[j-1])
  return tmp
