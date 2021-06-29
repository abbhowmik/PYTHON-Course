# def divide(num):
#     if num%5 == 0:
#         return True

# l = [5, 10, 15, 20, 45, 23, 4, 34]
# print(list(filter(divide, l)))

# other method is --->

# l = [5, 10, 15, 20, 45, 23, 4, 34]
# def a(a): return a % 5 == 0


# print(list(filter(a, l)))

# def b(number):
#     if number > 75:
#         return True
#     else:
#         return False


l = [45, 67, 98, 76, 76, 87, 45, 43, 23, 56]
def a(a): return a > 70


# print(list(filter(b, l)))
print(list(filter(a, l)))
