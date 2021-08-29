import time
print("\ngradient descent minimization")
d = 0.1
a = 0.001
f = lambda x,y: 1 + 2*(x**2) + 3*(y**2)

def run(x,y):
    for _ in range(2):
        f_x = (f(x+0.5*d, y) - f(x-0.5*d, y)) / d
        f_y = (f(x, y+0.5*d) - f(x, y-0.5*d)) / d
        x -= a*f_x
        y -= a*f_y
    return (x,y)
print("by hand answer: (0.9938, 1.981)")
print("calculated answer: ",run(1,2))
start = time.time()
for _ in range(10):
    run(1,2)
end = time.time()

print("python: ", (end-start)/10)
