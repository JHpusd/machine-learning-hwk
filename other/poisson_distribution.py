import operator as op
from functools import reduce
import numpy
import math

def factorial(x):
    return numpy.prod([i for i in range(1,x+1)])

def poisson(lam, X):
    if type(X) != list:
        X = [X]
    total = 0
    for x in X:
        total += (lam**(x) * math.exp(-lam)) / factorial(x)
    return total

print(1-poisson(3, [0,1]))