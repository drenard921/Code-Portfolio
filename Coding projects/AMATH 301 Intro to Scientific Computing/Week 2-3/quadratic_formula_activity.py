# AMATH 301 WI 23
# Authored by the legendary trio
# Dylan Renard (drenard9)
# Kai Poffenbarger (kaipoff)
# Nick Nelson (nichon3) 

# We solved the quadratic formula in this program
# 4.0 plz

import numpy as np

a = 4
b = 5
c = 6
tol = 10**(-12)

discriminant = b**2-4*a*c

if np.abs(discriminant) < tol:
   print('There is one real root')
   root1 = -b/(2*a)
   roots = np.array([root1]) 
elif discriminant >= tol:
    print('There are two real roots')
    root1 = (-b - np.sqrt(np.abs(discriminant)))/(2*a)
    root2 = (-b + np.sqrt(np.abs(discriminant)))/(2*a)
    roots = np.array([root1, root2])
else:
    print('There are no real roots')
    roots = np.array([]) # This creates an empty array


print(roots)