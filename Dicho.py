


import numpy as np 
from matplotlib import pyplot as plt






# The function we wanna calculate there racins "Solutions"
def f(x):

    return x**3-(11/6)*(x**2)+x-1/6 

# Dichotonomie Mthode of calculation :

# The interval 
a = int(input("Give us the first number of the interval: "))
b = int(input("Give us the second nimber of the interval: "))

#eps = real(input("Give us the epsilon number :")) # nombre of iteration 
eps = 10**-2
n = 1 #Init at 1  
# Dichotomy Algorithm :
def dichotomy(a,b,eps):
    while abs(f(b)-f(a)) > eps:
        root = None  #intialise the root "solution " to None 
        mid = (a+b)/2
    print(f'abs((a-b)/2)>eps was True, x is {x}!') ####
    # check 
    if f(mid) == 0 or abs(f(mid)) < eps:  
        root = mid                    # This to  find out if the mid is close to the solution 
    
    if f(a)*f(mid) <= 0:
        a = mid             # make the a mid to do another mid also until it came up with the solution 

    else:
        b = mid             #make the b mid to do another mid also until it came up with the solution

    n = n + 1
    if root is None:
        print('Root not found') # solution not found 
    else:
        print(f'The root, according to the dichotomy method, is at the point x = {root}') # print the solution

#dichotomy(a,b,eps)

 
# graph of the function :
# use matplotlib

pltr = input("Do you wanna plot the fonction graph?:[y/n]:")

x = np.linspace(a,0.0001,b)   # the interval of the plot [a,b] and the x

y = x**3-(11/6)*(x**2)+x-1/6   # the function we wanna plot f(x) = y

if pltr == "y" :
    plt.plot(x, y, c = "black",)     # use any color you want the standard is blue 
    plt.title(input("Give us the Function Title: "))
    plt.xlabel("axe x")                # name the axes as x and y ...
    plt.ylabel("axe y")     
    plt.show()                  # if True the graph will show up 
elif pltr == "n":
    print("OK,Thank you")


# if there is an error :
else:
    print("Error, You didnt shose [y/n] Try again.")

