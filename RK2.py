import numpy as np
import math

# User's input
h = float(input("Please enter the step length: "))
X0 = float(input("Please Enter the initial value of X: "))
Y0 = float(input("Please enter the initial value of Y:"))

X = float(input("Please enter the value of X to find the value of Y(X): "))

# -------------------------------------------------------------------------------
# 
a = X0
b = Y0

# -------------------------------------------------------------------------------

# Here is the function calculation

def Function(x,y):
    # This is the equation
    F = (5/50)*(1-math.exp(-50*x))
    # Change Equation to any other desired equation
    return F
    
F = Function(a,b)
# Testing the function
print (F)
# -------------------------------------------------------------------------------
#Method one to approaching the task
        # Yn = Yn-1 + 0.5(K1 + K2)
            # Where:
                # K1 = hf(Xn-1, Yn-1)
                # K2 = hf(Xn-1 + h, Yn-1 + K1)

i = 0
for i in np.arange(0,X,h):
    j = 1
    K1 = h*Function(a,b)
    # print (f"K1 = {K1}")
    K2 = h*Function(a+h,b+K1)
    # print (f"K2 = {K2}")
    Yn = round(b + 0.5*(K1 + K2),5)
    a+=h
    print (f"Y({j}) / Y({a}) = {Yn}")
    ++j
    b = Yn
    print (f"The new X = {a} and new Y = {b} \n")

# -------------------------------------------------------------------------------
# Method two to approaching the task
        # Yn = Yn-1 + K2
            # Where:
                # K2 = hf(Xn-1 + h/2, Yn-1 + K1/2)
                # K1 = hf(Xn-1, Yn-1)

# i = 0
# for i in np.arange(0,X,h):
#     j = 1
#     K1 = h*Function(a,b)
#     print (f"K1 = {K1}")
#     K2 = h*Function(a+h/2,b+K1/2)
#     print (f"K2 = {K2}")
#     Yn = round(b + K2,5)
#     a+=h
#     print (f"Y({j}) / Y({a}) = {Yn}")
#     ++j
#     b = Yn
#     print (f"The new X = {a} and new Y = {b} \n")