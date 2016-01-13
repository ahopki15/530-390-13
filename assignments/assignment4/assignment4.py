import numpy as np
import fft

def correlation(A,B):
  fft.fft(A,1.)
  fft.fft(B,-1.)
  N = len(A) >> 1
  corr = np.zeros(2*N)
  for i in range(N):
    corr[2*i] = A[2*i]*B[2*i] - A[2*i+1]*B[2*i+1]
    corr[2*i+1] = A[2*i+1]*B[2*i] + A[2*i]*B[2*i+1]
  fft.fft(corr,-1.)
  return corr
