# contains fibonacci function I wrote and relevant functrions from class from
# improc and fft
import numpy as np
import matplotlib.pyplot as plt 

# calculates the xth fibonacci number
def fibonacci(x):
  if x == 0:
    return 0
  elif x == 1:
    return 1
  else:
    return fibonacci( x - 1 ) + fibonacci( x - 2 )

# selection sort
def selectionsort(A, n):
  for i in range(n):
    m = A[i]
    mj = i
    for j in range(i,n):
      if A[j] < m:
        m = A[j]
        mj = j
    A[mj] = A[i]
    A[i] = m

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

# plot complex number
def plot_c(x,y):
  N = len(x)
  yr = np.zeros(N)
  yi = np.zeros(N)
  for i in range(N):
    yr[i] = y[2*i]
    yi[i] = y[2*i+1]
  plt.figure()
  plt.plot(x,yr,x,yi)
  plt.legend(["real","imaginary"])
  plt.show(block=False)

def fft_slow(data, isign):
  N = len(data) >> 1
  tmp = np.zeros(2*N)
  if N < 2 or N & (N-1): # checks if power of two
    print("data must be length of power of two")
    return data
  else:
    for n in range(N):
      for k in range(N):
        theta = isign*2.*PI*k*n/N
        ct = np.cos(theta)
        st = np.sin(theta)
        tmp[2*n] = tmp[2*n] + ct*data[2*k] - st*data[2*k+1]
        tmp[2*n+1] = tmp[2*n+1] + ct*data[2*k+1] + st*data[2*k]
    if isign < 0:
      for i in range(2*N):
        tmp[i] = tmp[i] / N
    return tmp
