import sys
sys.path.append('002')
from decision_tree import *

init_points = {'x': [(1,1), (1,2), (2,2), (2,3)], 'o': [(1,3), (1,4), (2,4)]}
dt = DecisionTree(init_points)

print("initial points:", dt.point_dict)
print("initial entropy:", dt.entropy)
print("best split:", dt.get_best_split())

dt.fit()
print("fitted the tree")
print("prediction for (2,1):", dt.predict((2,1)))
print("prediction for (1,6):", dt.predict((1,5)))