# Dylan Renard 
# AMATH 301 WI 2023
# Jeremy Upsal
# Friday Jan 20th, 2023

# AMATH 301 HW #2 Coding Section:
# In this program we do several numerical summations, 
# explore fibonacci sequence
# and compute the third order taylor series for Cosine
import numpy as np
import matplotlib.pyplot as plt

######### Problem 1 ##########
# Use a for loop!
result = np.zeros(32)
for n in range(1,33,1):
    numerator = n * (n + 1) * (2*n + 1)
    denominator = 6
    result[n - 1] = numerator / denominator
A1 = result

######### Problem 2 ##########
## Part a
# I will start this off for you, you will need to finish it.

# Initializing Summation terms
y1 = 0
y2 = 0
y3 = 0
y4 = 0

# Initializing Coefficient terms
term12 = 0.1
term3 = 0.25
term4 = 0.5

for k in range(100000):
    y1 += term12
for k in range(100000000):
    y2 += term12
    y3 += term3
    y4 += term4
A2 = y1
A3 = y2
A4 = y3
A5 = y4

## Part b - Now take the difference, don't forget absolute value!
A6 = np.abs(10000 - y1)
A7 = np.abs(y2 - 10000000)
A8 = np.abs(25000000 - y3)
A9 = np.abs(y4 - 50000000)


######### Problem 3 ##########
## Part a
# I will let you fill this in.
A10 = np.zeros(200)


## Part b
# You will this in
a, b = 1, 1
n = 0

## Part c
# I will start it off for you. Remove the comments and fill in the missing
# parts.
for k in range(200):
    if a > 1000000:
        break
    else:
        A10[k] = a
        a,b = b, a + b
        n = k


## Part d
# Update the code above to find and record that k corresponding to the largest
# Fibonacci number less than 1,000,000! Hint: use an if statement and save a
# new variable!
A11 = n

## Part e
# Slice! If N is the variable corresponding to the k you found above, then
# slice up through (including) N.
A12 = A10[:30]

######### Problem 4 ##########
## Part a
# I will let you create x here.
A13 = np.linspace(-np.pi, np.pi,100)

## Part b
# Assuming that x is defined correctly above, now we can just do regular
# arithmetic with it. Compare to what you did in Problem 2.
TaylorSwift = 0*A13 # Initialize the Taylor approximation - Remove this once you
                # define x!
# for loop here
for k in range(0,4):
    numerator = ((-1)**k)
    denominator = np.math.factorial(2*k)
    TaylorSwift += numerator*(A13**(2*k))/denominator
A14 = TaylorSwift

# update Taylor in the for loop using the formula in the sum!

