import imp
import math
from numpy import real 
import numpy 




# The function we wanna calculate there racins "Solutions"
def f(x):

    return x**3-(11/6)*(x**2)+x-1/6

# Dichotonomie Mthode of calculation :

# The interval 
a = int(input("Give us the first number of the interval: "))
b = int(input("Give us the second nimber of the interval: "))

#eps = real(input("Give us the epsilon number :")) # nombre of iteration 
eps = 10**-2
# init n 
n=1
# the 
while abs(a-b)/2>eps:
    root = None  #intialise the root "solution " to None 
    mid = (a+b)/2
    #print(f'abs((a-b)/2)>eps was True, x is {x}!')
    # check 
    if f(mid) == 0 or abs(f(mid)) < eps:  
            root = mid                    # This to  find out if the mid is close to the solution 
            break
    
    if f(a)*f(mid) <= 0:
        a = mid             # make the a mid to do another mid also until it came up with the solution 

    else:
        b = mid             #make the b mid to do another mid also until it came up with the solution

    n = n + 1


# Print the result:
if root is None:
    print('Root not found')
else:
    print(f'The root, according to the dichotomy method, is at the point x = {root}')  # print the solution as Root = x    f(root)=~o 

#print('the solution of this function is ',)
print(n,root) #number of iteration  
# graph of the function :
# use matplotlib