import sys
sys.path.append('002')
from decision_tree import *

init_points = {'x': [(1,1), (1,2), (2,2), (2,3)], 'o': [(1,3), (1,4), (2,4)]}
tree = DecisionTree(init_points)
print(tree.get_best_split())
