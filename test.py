class Bababooey():
    def __init__(self, x):
        self.x = x
    
    def add_one(self, a=None):
        if a == None:
            a = self
        print(a.x + 1)
        return

test = {'a':1, 'b':2, 'c':3}
print(list(test.keys()))