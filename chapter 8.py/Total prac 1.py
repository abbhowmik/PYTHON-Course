# def greet(name):
#     print("Good Morning," + name)

# def mysum(sum1, sum2):
#     return sum1+sum2
# s = mysum(2, 3)
# print(s)
# greet('Harry')


# def greet (name):
#     gr = 'Hello' + name
#     return gr
# a = greet('Harry')
# print(a)


# def greet(name = 'Ashis'):
#     print('good day,' + name)
# greet('Harry')
# greet()


# product = 1
# n = 4
# for i in range(n):
#     product = product *  (i+1)
# print(product)


# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product

# f = factorial_iter(5)
# print(f)


# def factorial_recursive(n):
#         if n==0 or n==1:
#             return 1
#         else:
#             return  n * factorial_recursive(n-1)
# f = factorial_recursive(5)
# print(f)


def percent(marks):
    p = (sum(marks)/400)*100
    return p


marks1 = [65, 78, 98, 58]
parcentage1 = percent(marks1)

marks2 = [66, 70, 99, 57]
parcentage2 = percent(marks2)
print(parcentage1, parcentage2)
