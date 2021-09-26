import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

def nb(r,p,x):
    if type(x) != list:
        x = [x]
    total = 0
    for val in x:
        if val < r:
            continue
        choose = ncr(val-1, r-1)
        p_1 = (1-p)**(val-r)
        p_2 = p**r
        total += choose * p_1 * p_2
    return total

print(nb(9,0.7,13))