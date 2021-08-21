import time

def n_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

start = time.time()
for _ in range(10):
    n_sum(1000000)
end = time.time()
print((end-start)/10)