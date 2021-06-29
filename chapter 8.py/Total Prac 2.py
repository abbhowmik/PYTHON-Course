# def greet(name):
#     print('good day,' + name)
# greet('Harry')


# def mysum(sum1, sum2):
#     return sum1 + sum2
# a = mysum(2, 3)
# print(a)


# def greet(name):
#     gr = 'Hello' +  name
#     return gr
# a = greet('harry')
# print(a)


# num = int(input('Enter number:: '))
# factorial = 1
# while num>0:
#     factorial = factorial * num
#     num = num - 1
# print(f'the factorial of your number is {factorial}')


# #factorial using for loop
# num = int(input('Please Enter a number:'))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = i * factorial
# print(f'the factorial of {num} is {factorial}')


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * (n - 1)

# a = factorial(5)
# print(a)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)


# f = factorial(2)
# print(f)


# def factorial_recursive(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
# f = factorial_recursive(0)
# print(f)


# product = 1
# n = 5
# for i in range(n):
#     product = product * (i + 1)
# print(product)


# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * ( i + 1)
#     return product
# f = factorial_iter(3)
# print(f)


# def greatnumber(num1, num2, num3):
#     if num1>num2:
#         if num1>num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2>num3:
#             return num2
#         else:
#             return num3

# a = greatnumber(2, 1, 5)
# print(str(a)  +  ' is the greatest number among them')


# def calculate(cel):
#     return (cel * (9/5)) + 32
# c = calculate(3)
# print(str(c)  + ' is the converted form of Fahrenhite')


# print ('Hello', end = " ")
# print ('How', end = " ")
# print ('are', end = " ")
# print ('you?', end = " ")


# def factorial_recursive(num):
#     if num ==0 or num ==1:
#         return 1
#     else:
#         return num + factorial_recursive(num - 1)
# a = factorial_recursive(5)
# print(a)

# another method is in below

# def factorial_iter(n):
#     product = 0
#     for i in range(n):
#         product = product + ( i + 1)
#     return product
# f = factorial_iter(5)
# print(f)


# def calculate(inch):
#     return inch * 2.54
# c = calculate(5)
# print( str(c) + ' is the converted form of cm ')


# a = '            Harry is a good boy and also a good Coder             '
# print(a.strip())


# n = int(input('Please Enter a number that you want to multiplicate:: '))
# for i in range(1, 11):
#     print(f'{n}X{i}={n*i}')
# print(f'this is the multiplication table of {n}')


# def remove_and_split(string, name):
#     newstr = string.replace('name', "  ")
#     return newstr.strip()
# x = 'Ashis is a good boy and he now starts coding in Python'
# y = remove_and_split(x, 'Ashis')
# print(y)
# #thus we can remove a particualr word or name in the string and strip or join the space at a same time
