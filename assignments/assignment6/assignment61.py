
import numpy as np
import random

def monte_carlo_3d(func,a,b,inregion,N):
  f = 0
  f2 = 0
  Lx = b[0]-a[0]
  Ly = b[1]-a[1]
  Lz = b[2]-a[2]
  for i in range(N):
    x = a[0] + random.random()*Lx
    y = a[1] + random.random()*Ly
    z = a[2] + random.random()*Lz
    if inregion(x,y,z):
      f = f + func(x,y,z)
      f2 = f2 + func(x,y,z)*func(x,y,z)
  f = f / N
  f2 = f2 / N
  I = f * Lx*Ly*Lz
  S = np.sqrt((f2-f*f) / N) * Lx*Ly*Lz
  return [I,S]
  
def sphere(x,y,z):
  if x*x + y*y + z*z <= 1:
    return True
  else:
    return False

def density(x,y,z):
  return 1.

def exponential(beta):
  tmp = random.random()
  if tmp == 0:
    tmp = random.random()
  else:
    return -np.log(tmp)/beta

def trap_d(x, y):
  N = len(x)
  h = (x[N-1]-x[0]) / (N-1)
  S = 0.5*(y[0] + y[N-1])
  for j in range(1,N-1):
    S = S + y[j]
  S = S*h
  return S

# merge sort (entry point)
def mergesort(A,n):
  if n > 1:
    m = round(0.5 * n)
    mergesort(A[0:m],m)
    mergesort(A[m:], n-m)
    merge(A,n,m)

def merge(A,n,m):
  B = np.empty(n)
  i = 0  # first half index
  j = m  # second half index
  for k in range(n):
    if j == n:
      B[k] = A[i]
      i = i+1
    elif i == m:
      B[k] = A[j]
      j = j+1
    elif A[j] < A[i]:
      B[k] = A[j]
      j = j+1
    else:
      B[k] = A[i]
      i = i+1
  for i in range(n):
    A[i] = B[i]

def histogram(A,N):
  n = len(A)
  maximum = A[0]
  minimum = A[0]
  for i in range(n):
    if A[i] > maximum:
      maximum = A[i]
    if A[i] < minimum:
      minimum = A[i]
    else:
      maximum = maximum
      minimum = minimum
  bin_size = (maximum - minimum) / N
  B = np.zeros(N)
  j = 0
  p = round(n/2)
  mergesort(A,p)
  for i in range(N):
    while A[j] < bin_size*(i+1):
      B[i] = B[i]+1
      j = j + 1
  X = np.zeros(N)
  for i in range(N):
    X[i] = i
  Int = trap_d(X,B)
  norm = 1/Int
  for i in range(N):
    B[i] = B[i]*norm
  return [X,B]
