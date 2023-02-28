# Dylan Renard 
# AMATH 301 WI 2023
# Jeremy Upsal
# Saturday Jan 7th, 2023

# AMATH 301 HW #1 Coding section:
# In this program we explore several functions of numpy
# including
# linespace and arrange

import numpy as np
import matplotlib.pyplot as plt

## Problem 1
# Part a
x = 3.1
A1 = x

# Part b
y = -29
A2 = y

# Part c - "e" is implemented in numpy with np.e
z = 9*np.e
A3 = z

# Part d
# There are two ways to do this. We can raise the number "e" to the 4th power,
# or (preferably) we can use np.exp() which takes e to a power.
w = np.exp(4)
A4 = w
# print(A4) # uncomment this line to check your work!

# Part e
# You have to do this one! Don't do any simplifications, just write the code
# and let python do the computation for you. 

A5 =  np.sin(np.pi)

## Problem 2
# I'll start you off with:
x = np.linspace(0, 1, 5) # First create the vector [0, 1/4, 2/4, 3/4, 4/4]
# Now once that is created, we can just multiply by pi
x = np.cos((np.pi*x))
A6 = x

## Problem 3
# Try to do this problem like I've setup the last problem: do not type in u or
# v directly, instead use built-in functions, linspace and arange. 
# I've given you an example on how to use linspace above. Use that to create
# either u or v (hint: which one is defined by the number of points?
# You have seen how linspace works. Look up "numpy arange" on google to see how
# arange works.
u = np.linspace(3.00,4.00,6)
v = np.arange(0,4,0.75)
A7 = u
A8 = v
w = v + 2 * u
A9 = w
w = u**3
A10 = w

A11 = np.tan(u) + np.exp(v)
A12 = u[2]

## Problem 4
# Again try to do this problem without "hardcoding." That means that you should
# use built-in functions when you can. Use *indexing* instead
# of typing in the answer directly. 

z = np.arange(-6,3.01,1/100)
A13 = z
print(z)
# Assuming that you have z defined correctly, the following code will give you
# A14. Uncomment it and check!
temp = np.arange(0, len(z), 2) # This creates an array from 0 to the length
                                 # of z with a spacing of 2 (every other)
A14 = z[temp] # Now we can use this array to index, giving what we want!
print(A14) # Uncomment this line to check your work!

# I'll show you one more way to do this. 
A14 = z[0::2] # This says take elements of z starting at 0, up through the
                # end, in spacing of 2s
                # We could also get rid of the zero, having just z[::2], check
                # for yourself!
temp2 = np.arange(0, len(z), 3)
A15 = z[temp]
A15 = z[0::3]
A16 = z[len(z)-5:len(z)]


# Writeup problems

#Q1 Practice Plotting a Linear plot
x = np.arange(-5,5+0.5,0.5)
y = x
plt.plot(x,y,color='black')
plt.plot(x,y,color='blue',marker='o')
plt.title('Simple Linear plot of f(x) =x on domain of [-5,5]')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#Q2 Practice Plotting a Quadratic plot
y2 = x**2
plt.plot(x,y2,color='black')
plt.plot(x,y2,color='purple',marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Quadratic plot of f(x) =x^2 on domain of [-5,5]')
plt.show()