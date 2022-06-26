import math
from numpy import real 
import numpy

# The function we wanna calculate there racins "Solutions"
def f(x):

    return x**3-(11/6)*(x**2)+x-1/6

# Dichotonomie Mthode of calculation :

# The interval 
a = int(input("Give us the first number of the interval "))
b = int(input("Give us the second nimber of the interval "))

#eps = real(input("Give us the epsilon number :")) # nombre of iteration 
eps = 10**-2
# init n 
n=1
# the 
while abs(a-b)/2>eps:
    x = (a+b)/2
    #print(f'abs((a-b)/2)>eps was True, x is {x}!')
    # check 
    
    if numpy.number(f(a))*numpy.number(f(b)) <= 0:
         a = a
         b = numpy.number(f(b))
    else:
        a = numpy.number(f(a))
        b = b
    n = n + 1


# Print the result:

print('the solution of this function is ',str(x))
print(n)