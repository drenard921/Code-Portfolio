# Let's see how to work with variables

x = 8 # Assign the variable x = 8

# This assigns the value ``8`` to a variable named ``x``.
# After running this code, python will store the number 8 somewhere in memory.
# We can retrieve this value whenever we need it by using the name ``x``.
# For example, we could print it out using

print(x)

# or we could use it in other calculations such as

print( (x + 12) / 4 )

print(x - 2)

print(x * 5.0 - x)

# Notice that in all of these calculations python simply replaces all instances of
# ``x`` with ``8`` and then proceeds with normal arithmetic.  

#If we want to change the value of ``x``, we can just reassign it with the
# ``=`` operator.  For example:
x = 3
print(x)
print(x-2)

# Now let's see what happens when we use a random variable
import random 
print('this is a random number', random.randint(0, 10))
