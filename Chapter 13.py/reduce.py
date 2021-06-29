from functools import reduce


def sum1(a, b):
    return a+b


# sum2 = lambda a, b: a*b
l = [1, 2, 3, 4, 5]

value1 = reduce(sum1, l)
print(value1)

# value2 = reduce(sum2, l)
# print(value2)
