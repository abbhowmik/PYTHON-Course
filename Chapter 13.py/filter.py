def grater_than_5(num):
    if num > 5:
        return True
    else:
        return False


l = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 341, 432, 54, 2, 35, 4, 54]


def a(a): return a > 34


print(list(filter(grater_than_5, l)))
print(list(filter(a, l)))


# l = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 341, 432, 54, 2, 35, 4, 54]
# a = lambda num: num>12
# print(list(filter(a, l)))
