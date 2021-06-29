 
# func = lambda x: x + 5
# square = lambda a: a*a
# sum = lambda a, b, c: a + b + c
# x = 5
# print(func(x))
# print(square(x))
# print(sum(1, 2, 3))



# a = ['laptop', 'phone', 'computer', 'iphone']
# b = ' and '.join(a)
# c = ' \n '.join(a)
# print(c)
# print(b)
# print(type(b))



# a = 'Ashis'
# b = 'Coding channel'
# c = 'CodeWithAshis'

# s = 'This is {0} and his {1} channel is {2}'.format(b, a, c)
# print(s)



# def square(num):
#     return num * num
# l = [2, 4, 6]

# # l1 = []
# # for item in l:
# #     l1.append(square(item))


# print(list(map(square, l)))




# def grater_than_5(num):
#     if num>5:
#         return True
#     else:
#         return False
# l = [ 5, 6 ,7, 3, 4, 5, 3, 2 , 8 , 9, 7, 8, 56, 453, 34, 56 ]
# a = lambda a: a>10
# print(list(filter(grater_than_5, l)))
# print(list(filter(a, l)))




# from functools import reduce
# a = lambda x,y: x * y
# l = [1, 2, 3, 4, 5]
# value = reduce(a, l)
# print(value)




# name = 'Ashis'
# marks = 99
# number = 9866543221
# a = '''The name of the student is {0}, his marks are
# {1} and phone number is {2}'''.format(name, marks, number)
# print(a)




# a = [str(i*7) for i in range(1, 11)]
# b = '\n'.join(a)
# print(b)

# def divide(num):
#     if num%5==0:
#         return True
#     else:
#         return False

# l = [5, 15, 3, 4, 55, 35, 85]
# print(list(filter(divide, l)))



# l = [5, 15, 3, 4, 55, 35, 85]
# a = lambda a: a%5==0
# print(list(filter(a, l)))



# from functools import reduce

# l = [1, 2, 3, 43, 54234, 43, 523452 ,4 , 356, 2345 ]
# a = reduce(max, l)
# print(a)