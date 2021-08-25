import numpy as np
import time
print("\npsuedoinverse")
def run():
    y = [[0],[1],[4],[9]]
    data = [[0,1],[1,1],[2,1],[3,1]]
    transpose = np.transpose(data)
    square = np.matmul(transpose, data)
    inverse = np.linalg.inv(square)
    answer = np.matmul(inverse, np.matmul(transpose, y))

start = time.time()
for _ in range(10):
    run()
end = time.time()
print("Python: ", (end-start)/10)

