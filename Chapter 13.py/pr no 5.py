from functools import reduce
l = [3, 4, 5, 6, 7, 34254, 4523, 563]
a = reduce(max, l)
print(a)