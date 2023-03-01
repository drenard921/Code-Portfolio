# Dylan Renard
# AMATH 301 Winter 2023
# Jeremy Upsal
# February 3rd 2023

# HW 4 coding section
# This is a template for the coding portion of Homework 4 in AMATH 301, 
# Winter 2023 

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
import scipy.optimize

############## Problem 1 ################
## Part a
# Define x(t) below
x = lambda t: ((11/6)*(np.exp(-t/12)-np.exp(-t)))

# Define x'(t) below. I did this one for you.
xprime = lambda t: 11*(-1/12*np.exp(-t/12) + np.exp(-t))/6

# You need to do something to find the *maximum* using the *minimization*
# algorithms. How can you define a new anonymous function to make this work?
# Hint: you can define one anonymous function from another!

# Example: We use scipy.optimize.fsolve to find zeros of a function. For instance, if
example = lambda t: t*(t-1)
# We know that there are two zeros: one at t=0 and one at t=1. We can find the
# zero at t=1 by choosing a guess close to 1.
# The syntax is scipy.optimize.fsolve(anonymous_function, guess)
example_root = scipy.optimize.fsolve(example, 1) 
print('The root near x=1 of our example is = ', example_root) # Note that this
                            # is an array. To get the answer I have to index.
A1 = xprime(1.5)
A2 = scipy.optimize.fsolve(xprime, 1.5)
A3 = x(A2)
## Part b
# Look at some examples of how we have used fminbound in class, for example on
# January 23, 24, or 27.
negx = lambda t: -((11/6)*(np.exp(-t/12)-np.exp(-t)))
maximize = scipy.optimize.fminbound(negx, 0, 10)
max = x(maximize)
A4 = np.array([maximize, max])

############## Problem 2 ################
## Part a
# Define Himmelblau's function using lambda x, y: ... first, and then use an
# adapter function! The adapter function is below, you need to define fxy and
# then you can uncomment the following line.
fxy = lambda x, y: (x**2 + y - 11)**2 + (x + y**2 -7)**2
f = lambda p: fxy(p[0], p[1]) # Assuming that fxy is defined in terms of x
                                # and y. Once you have that defined, uncomment
                                # this line.
A5 = f([3,4])
## Part b
# Recall that the syntax for scipy.optimize.fmin 
# is scipy.optimize.fmin(anonymous_function, guess), where anonymous_function
# has to be a function of one variable. 
A6 = scipy.optimize.fmin(f, [-3, -2])

## Part c
# I'll start out this one by typing out the gradient, to limit the number of
# typos.
gradf_xy = lambda x,y: np.array([4*x**3 - 42*x + 4*x*y + 2*y**2 - 14,
                                 4*y**3 - 26*y + 4*x*y + 2*x**2 - 22])
# Now you need to turn it into a function of one variable using an adapter.
gradf = lambda p: gradf_xy(p[0], p[1])
A7 = gradf(A6)
A8 = np.linalg.norm(A7)
## Part d
# I'll start you off with a skeleton. You need to fill in parts. This is
# commented to start so that the code runs, you will need to uncomment it to
# use it. 
p = np.array([-3, -2]) # Initial guess defined in part (e)
tol = 10**(-7) # you need to define tol!
A10 = 0
for k in range(2000):
    grad = gradf(p)
    if np.linalg.norm(grad)>tol:
        phi = lambda t: p -t*grad
        f_of_phi = lambda t: f(phi(t))
        tmin = scipy.optimize.fminbound(f_of_phi, 0, 1)
        p = phi(tmin)
        A10 = A10 + 1

    if np.linalg.norm(grad)<tol:
        break
A9 = p
#


## Part e
# Done above!
