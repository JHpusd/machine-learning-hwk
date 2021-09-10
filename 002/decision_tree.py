import math as m

class DecisionTree():
    def __init__(self, point_dict):
        self.point_dict = point_dict
        self.entropy = self.get_entropy()
        self.parent = None
        self.branches = None
        self.best_split = None
    
    def get_all_coords(self, point_dict=None):
        result = []
        if point_dict == None:
            point_dict = self.point_dict
        for key in point_dict:
            result += point_dict[key]
        return result

    def get_entropy(self, point_dict=None):
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
        result = []
        if point_dict == None:
            point_dict = self.point_dict
        all_coords = self.get_all_coords(point_dict)
        for i in range(len(all_coords[0])):
            unique = list(set([coord[i] for coord in all_coords]))
            midpoints = self.get_midpoints(unique)
            for midpoint in midpoints:
                result.append((i, midpoint))
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
            child_1 = DecisionTree(greater_dict)
            child_2 = DecisionTree(lesser_dict)
            child_1.parent = self
            child_2.parent = self
            self.branches = [child_1, child_2]
        return [greater_dict, lesser_dict]
    
    def weighted_entropy(self, point_dict_list):
        weighted_entropy = 0
        num_points = sum([len(self.get_all_coords(point_dict)) for point_dict in point_dict_list])
        for point_dict in point_dict_list:
            entropy = self.get_entropy(point_dict)
            num_point_ratio = len(self.get_all_coords(point_dict))/num_points
            weighted_entropy += entropy * num_point_ratio
        return weighted_entropy
    
    def get_best_split(self, point_dict=None):
        check = False
        if point_dict == None:
            check = True
            point_dict = self.point_dict
        all_splits = self.get_splits(point_dict)
        best_split = all_splits[0]
        best_entropy = self.weighted_entropy(self.split(best_split, point_dict))
        for split in all_splits:
            branches = self.split(split, point_dict)
            weighted_entropy = self.weighted_entropy(branches)
            if weighted_entropy < best_entropy:
                best_split = split
                best_entropy = weighted_entropy
        if check:
            self.best_split = best_split
        return best_split

