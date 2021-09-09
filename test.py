def add(input_dict, obj):
    input_dict[obj] = 5

test_1 = {'a': 1, 'b':2, 'c':3}
test_2 = test_1.copy()
add(test_2, 'd')
print(test_1)
print(test_2)