# Dylan Renard 
# AMATH 301 WI 2023
# Jeremy Upsal
# Sunday Jan 22th, 2023

# AMATH 301 HW #2 Coding Section:
# In this program we do several numerical summations, 
# explore fibonacci sequence
# and compute the third order taylor series for Cosine

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

############## Problem 1 ################
M = np.genfromtxt('Plutonium.csv', delimiter=',')
t = M[0, :]
P = M[1, :]

## Part a
# Compute h from the t array
A1 = t[1] - t[0]

## Part b
# forward difference formula at t=0
A2 = (P[1] - P[0]) / A1 

## Part c
A3 = (P[-1] - P[-2]) / A1

## Part d
# Uncomment the line below to get A4
A4 = (-3*P[0] + 4*P[1] - P[2])/(2*A1)

## Part e #
A5 = (3*P[-1] - 4*P[-2] + P[-3])/(2*A1)


## Part f
# You may want to use a for loop here
rizz = np.zeros(41)
rizz[0], rizz[-1] = A4, A5

for k in range(1, len(t)-1):
    rizz[k] = (P[k+1] - P[k-1])/(2*A1)
A6 = rizz


## Part g
A7 = -1/P * A6

## Part h
A8 = np.average(A7)


## Part i
A9 = np.log(2)/A8

## Part j

# derive a scheme for the 2nd derivative at t=22
A10 = (P[23] + P[21] + (-2*P[22]))/(A1**2)

# To derive the equation follow the same steps but isolate the f''(x) term
# Removing f(x) and f'(x)

############## Problem 2 ################
# You are going to want to define the integrand as an anonymous function.
mu = 85
sigma = 8.3
integrand = lambda x: np.exp(-(x-mu)**2/(2*sigma**2))/np.sqrt(2*np.pi*sigma**2)

# Let's also define the left and right bounds of the integral
left = 110
right = 130

## Part a
A11, err = integrate.quad(integrand, left, right)
## Part b
# To define the h array, we can take 2 to the power of an array.
power = -np.linspace(1, 16, 16)

# Now create h from that array!
A12 = np.zeros(len(power))
dx = 0
for i in range(len(A12)):
    dx = 2**power[i]
    x = np.arange(110, 130 + dx, dx)
    y = integrand(x)
    A12[i] = dx * np.sum(y[:-1]) 


## Part c
A13 = np.zeros(len(power))
dx = 0
for i in range(len(A13)):
    dx = 2**power[i]
    x = np.arange(110, 130 + dx, dx)
    y = integrand(x)
    A13[i] = dx * np.sum(y[1:]) 


# ## Part d
A14 = np.zeros(len(power))
dx = 0
for i in range(len(A14)):
    dx = 2**power[i]
    x = np.arange(110, 130 + dx, dx)    
    for k in range(len(x) - 1):
        A14[i] += dx * integrand((x[k] +x[k+1])/2)
print("A14", A14)


# ## Part e
A15 = (A12 + A13) / 2

# ## Part f
A16 = np.zeros(len(power))
for i in range(len(A16)):
    dx = 2**power[i]
    x = np.arange(110, 130 + dx, dx)
    y = integrand(x)
    A16[i] = (dx/ 3) * (y[0] + 4*sum(y[1:-1:2]) + 2*sum(y[2:-2:2]) + y[-1])

print("A16", A16)



