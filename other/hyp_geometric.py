import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

def hyp_geometric(N, K, n, x):
    valid_vals = range(max(0,n+K-N), min(n,K)+1)
    total = 0
    if type(x) != list:
        x = [x]
    for val in x:
        if val not in valid_vals:
            continue
        total += (ncr(K,val) * ncr(N-K,n-val))/ncr(N,n)
    return total

print(hyp_geometric(24,9,12,[0,1,2,3,4,5,6,7,8]))
