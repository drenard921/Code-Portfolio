import numpy as np

# Define function of two variables
f = lambda x, y: (x-2)**2 + (y+1)**2 + 5*np.sin(x)*np.sin(y) + 100
# Notice that we don't have x or y defined anywhere. We plug those in later.

# Check that it works as expected:
# print(f(0, 0)) # Should be 105
# print(f(6,4))
# print(f(np.pi/2,1))

# We want to use an "adapter function" to make this function have just one
# input. This is because that is the required format for python built-in
# functions.
fp = lambda p: f(p[0], p[1]) #p[0] represents x, p[1] represents y
# Notice again that we don't have p defined anywhere, it's something we will
# plug in later. 


f_x = lambda x, y: 2*(x - 2) + 5*np.cos(x)*np.sin(y)
f_y = lambda x, y: 2*(y+2) + 5*np.sin(x)*np.cos(y)

gradf_xy = lambda x, y: np.array([2*(x - 2) + 5*np.cos(x)*np.sin(y), 2*(y+2) + 5*np.sin(x)*np.cos(y)])  
gradf = lambda p: gradf_xy(p[0], p[1]) # adapter function

gradf_xy(6,4)