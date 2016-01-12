import assignment3
import numpy as np
import matplotlib.pyplot as plt
import time

#Question 1
array_100 = np.random.rand(100)
array_1000 = np.random.rand(1000)
assignment3.selectionsort(array_100,100)
t0 = time.time()
array_10000 = np.random.rand(10000)
t_100_select = time.time()
assignment3.mergesort(array_100,50)
t_100_merge = time.time()
assignment3.selectionsort(array_1000,1000)
t_1000_select = time.time()
assignment3.mergesort(array_1000,1000)
t_1000_merge = time.time()
assignment3.selectionsort(array_10000,10000)
t_10000_select = time.time()
assignment3.mergesort(array_10000,5000)
t_10000_merge = time.time()

#print(t_100_select-t0)
#print(t_100_merge-t_100_select)
#print(t_1000_select-t_100_merge)
#print(t_1000_merge-t_1000_select)
#print(t_10000_select-t_1000_merge)
#print(t_10000_merge-t_10000_select)


x = np.zeros(3)
y = np.zeros(3)
z = np.zeros(3)

# Matrix of array size values
x[0] = 100
x[1] = 1000
x[2] = 10000

# Matrix of selection sort times per value
y[0] = t_100_select-t0
y[1] = t_1000_select-t_100_merge
y[2] = t_10000_select-t_1000_merge

# Matrix of merge sort times per value
z[0] = t_100_merge-t_100_select
z[1] = t_1000_merge-t_1000_select
z[2] = t_10000_merge-t_10000_select

print(x)
print(y)
print(z)

# I tried to print the results in python but got x forwarding errors so I 
# printed the values and plotted them in Excel instead
#plt.plot(x,y)
#plt.show()
#plt.plot(x,z)
#plt.show()

# Question 2
#24th fibonacci number
print(assignment3.fibonacci(24))

# Question 3
# I had similiar x forwarding erros as in problem 1, so I wasn't
# able to actually generate the graphs
PI = 2*np.arcsin(1)
N = 64
L = 2*PI
dx = L / (N-1)
x = np.zeros(N)
f = np.zeros(N)
y = np.zeros(2*N)

# for f = sin(x) + sin(4x)
A = 4

for i in range(N):
  x[i] = i*dx
  f[i] = i
  y[2*i] = np.sin(x[i]) + np.sin(A.*x[i])
  y[2*i+1] = 0

y = fft.fft_slow(y,1.)
fft.plot_c(f[:0.5*N],y[:N])

y = np.zeros(2*N)

# for f = sin(x) + sin(13*x)
A = 13

for i in range(N):
  x[i] = i*dx
  f[i] = i
  y[2*i] = np.sin(x[i]) + np.sin(A.*x[i])
  y[2*i+1] = 0

y = fft.fft_slow(y,1.)
fft.plot_c(f[:0.5*N],y[:N])

y = np.zeros(2*N)

# for f = sin(x) + sin(28*x)
A = 28

for i in range(N):
  x[i] = i*dx
  f[i] = i
  y[2*i] = np.sin(x[i]) + np.sin(A.*x[i])
  y[2*i+1] = 0

y = fft.fft_slow(y,1.)
fft.plot_c(f[:0.5*N],y[:N])

y = np.zeros(2*N)

# for f = sin(x) + sin(39*x)
A = 39

for i in range(N):
  x[i] = i*dx
  f[i] = i
  y[2*i] = np.sin(x[i]) + np.sin(A.*x[i])
  y[2*i+1] = 0

y = fft.fft_slow(y,1.)
fft.plot_c(f[:0.5*N],y[:N])

y = np.zeros(2*N)

# for f = sin(x) + sin(59*x)
A = 50

for i in range(N):
  x[i] = i*dx
  f[i] = i
  y[2*i] = np.sin(x[i]) + np.sin(A.*x[i])
  y[2*i+1] = 0

y = fft.fft_slow(y,1.)
fft.plot_c(f[:0.5*N],y[:N])

y = np.zeros(2*N)

plt.show()
