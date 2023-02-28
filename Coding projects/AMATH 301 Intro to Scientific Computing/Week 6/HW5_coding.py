import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

##################### Coding Problem 1 ##########################
## Part a - Load in the data
# The data is called 'CO2_data.csv'
data = np.genfromtxt("CO2_data.csv", delimiter = ",") 

# Once you have M defined from CO2_data, uncomment the 
# following code to define t and CO2
t = data[:, 0]
CO2 = data[:, 1]
A1 = t
A2 = CO2

## (b)
# Define the error function that calculates the sum of squared error.
# I've started this for you, but you need to fill it in and uncomment. 
def sumSquaredError(a,b,r):
   # Define the model y
   y = lambda t: a + b*np.exp(r*t)
   # Compute the error using sum-of-squared error
   return np.sum((y(t) - CO2)**2)

# Check the error function by defining A3
A3 = sumSquaredError(300,30,0.03)
## (c)
# We need an adapter function to make this work with scipy.optimize.fmin
# Uncomment the line below to use the adapter function
adapter = lambda p: sumSquaredError(p[0], p[1], p[2])

# Once adapter is defined, use fmin
# We use the following guess
guess = np.array([300, 30, 0.03])

A4 = scipy.optimize.fmin(adapter,guess, maxiter=2000)


## (d)
# Once we have found the optimal parameters, 
# find the error for those optimal parameters
A5 = adapter(A4)


## (e)
# Now we do the same thing except with max error. 
# Your function looks similar, except use the max error
def maxError(a,b,r):
   # Define the model y
   y = lambda t: a + b*np.exp(r*t)
   # Compute the error using sum-of-squared error
   return  np.amax(np.abs(y(t) - CO2))


adapter_max = lambda p: maxError(p[0], p[1], p[2])
A6 = maxError(300,30,0.03)
A7 = scipy.optimize.fmin(adapter_max, guess, maxiter=2000) 

## (f)
# This error function has more inputs, but it's the same idea.
# Make sure to use sum of squared error!
def sumSquaredError2(a,b,r,c,d,e):
   # Define the model y
   y = lambda t: a + b*np.exp(r*t) + c *np.sin(d*(t - e)) 
   # Compute the error using sum-of-squared error
   return sum(np.abs(y(t) - CO2)**2)

A8 = sumSquaredError2(300, 30, 0.03,-5,4,0)

## (g)
adapter2 = lambda p: sumSquaredError2(p[0], p[1], p[2], p[3], p[4], p[5])
initial_guess = np.array([A4[0], A4[1], A4[2], -5, 4, 0])
best_guess = scipy.optimize.fmin(adapter2, initial_guess, maxiter=20000)
A9 = best_guess



# And we need to make a new adapter function
# Again, this will have more inputs but will look pretty similar. 

## (h)
# Once we have found the optimal parameters, find the associated error.
A10 = sumSquaredError2(best_guess[0], best_guess[1], best_guess[2], best_guess[3], best_guess[4], best_guess[5])


######################### Coding problem 2 ###################
## Part (a)
M = np.genfromtxt('salmon_data.csv', delimiter=',')

year = M[:,0] #Assign the 'year' array to the first column of the data
salmon = M[:,1] #Assign the 'salmon' array to the first column of the data

## (b) - Degree-1 polynomial
first_degree_p = np.polyfit(year, salmon, 1)
A11 = first_degree_p
p0 = lambda x: first_degree_p[0]*x + first_degree_p[1]
## (c) - Degree-3 polynomial
third_degree_p = np.polyfit(year, salmon, 3)
A12 = third_degree_p
p1 = lambda x: third_degree_p[0]*x**3 + third_degree_p[1]*x**2 + third_degree_p[2]*x +third_degree_p[3]

## (d) - Degree-5 polynomial
fifth_degree_p = np.polyfit(year,salmon,5)
A13 = fifth_degree_p
p2 = lambda x: fifth_degree_p[0]*x**5 + fifth_degree_p[1]*x**4 + fifth_degree_p[2]*x**3 +  + fifth_degree_p[3]*x**2 + fifth_degree_p[4]*x +fifth_degree_p[5] 

## (e) - compare to exact number of salmon
exact =  752638 # The exact number of salmon
first_d_err = np.abs(p0(2022)- exact)/exact
third_d_err = np.abs(p1(2022)- exact)/exact
fifth_d_err = np.abs(p2(2022)- exact)/exact

A14 = [first_d_err,third_d_err,fifth_d_err]
