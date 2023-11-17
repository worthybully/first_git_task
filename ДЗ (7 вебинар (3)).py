from functools import reduce
list1 = [34, 5, 6, 6, 28, 93]
the_biggest = int(reduce(lambda x, y: x if x >= y else y, list1))
the_biggest