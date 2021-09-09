import math as m

class DecisionTree():
    def __init__(self, point_dict):
        self.point_dict = point_dict
        self.entropy = self.entropy()
        self.parent = None
        self.branches = []
    
    def get_all_coords(self, point_dict=None):
        result = []
        if point_dict == None:
            point_dict = self.point_dict
        for key in point_dict:
            result += point_dict[key]
        return result

    def entropy(self, point_dict=None):
        entropy = 0
        if point_dict == None:
            point_dict = self.point_dict
        for sign in point_dict:
            ratio = len(point_dict[sign])/len(self.get_all_coords(point_dict))
            if ratio == 0:
                continue
            entropy += -1*ratio*m.log(ratio)
        return entropy
    
    def remove_from_dict(self, input_dict, vals):
        copy_dict = input_dict.copy()
        if type(vals) is not list:
            vals = [vals]
        for key in copy_dict:
            items = list(copy_dict[key])
            new_items = []
            for item in items:
                if item in vals:
                    continue
                new_items.append(item)
            copy_dict[key] = new_items
        return copy_dict
    
    def get_midpoints(self, unique):
        midpoints = []
        for i in range(len(unique)-1):
            midpoints.append((unique[i]+unique[i+1])/2)
        return midpoints

    def get_splits(self, point_dict=None):
        result = {}
        if point_dict == None:
            point_dict = self.point_dict
        all_coords = self.get_all_coords(point_dict)
        for i in range(len(all_coords[0])):
            unique = list(set([coord[i] for coord in all_coords]))
            midpoints = self.get_midpoints(unique)
            result[i] = midpoints
        return result
    
    def split(self, split_tuple, point_dict=None):
        check = False
        if point_dict == None:
            check = True
            point_dict = self.point_dict
        index = split_tuple[0]
        val = split_tuple[1]
        greater = [coord for coord in self.get_all_coords(point_dict) if coord[index]>=val]
        lesser = [coord for coord in self.get_all_coords(point_dict) if coord[index]<val]
        greater_dict = self.remove_from_dict(point_dict, lesser)
        lesser_dict = self.remove_from_dict(point_dict, greater)
        if check:
            self.branches = [DecisionTree(greater_dict), DecisionTree(lesser_dict)]
        return [DecisionTree(greater_dict), DecisionTree(lesser_dict)]

    
