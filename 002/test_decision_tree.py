import sys
sys.path.append('002')
from decision_tree import *
'''
init_points = {'x': [(1,1), (1,2), (2,2), (2,3)], 'o': [(1,3), (1,4), (2,4)]}
dt = DecisionTree(init_points)
print("first test case")
print("initial points:", dt.point_dict)
print("initial entropy:", dt.entropy)
print("best split:", dt.get_best_split())

dt.fit()
print("fitted the tree")
print("prediction for (2,1):", dt.predict((2,1)))
print("prediction for (1,6):", dt.predict((1,5)))

init_points = {'o':[(2,1),(2,2),(3,1),(3,2)], 'x':[(3,3),(4,1),(4,2),(4,3),(5,1)]}
dt = DecisionTree(init_points)
print('\nsecond test case')
print("initial points:",dt.entropy)
print("best split:",dt.get_best_split())

dt.fit()
print("fitted the tree")
print("prediction for (1,1):", dt.predict((1,1)))
print("prediction for (2,3):", dt.predict((2,3)))
print("prediction for (4,4):", dt.predict((4,4)))
print("prediction for (5,2):", dt.predict((5,2)))
'''
init_points = {'x':[(1,7),(2,7),(3,7),(3,8),(3,9),(7,1)], 'o':[(1,9),(5,1),(5,2),(5,3),(6,3),(7,3)]}
dt = DecisionTree(init_points, 7)
print(dt.get_best_split())
dt.fit()
print(dt.branches[0].best_split)