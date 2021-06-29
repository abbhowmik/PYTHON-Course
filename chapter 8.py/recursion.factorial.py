# product = 1
# n = 4
# for i in range(n):
#     product = product * (i+1)
# print(product)
# # thus we print factorial by recursion


# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i + 1)
#     return product

# f = factorial_iter(5)
# print(f)


# so n! =  n * (n-1)!
# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
# f = factorial_recursive(5)
# print(f)


# the below mentioned method is a anothor way to find factorial

# num = int(input('Enter number:: '))
# factorial = 1
# while num>0:
#     factorial = factorial * num
#     num = num - 1
# print(f'the factorial of your number is {factorial}')


# the below mentioned method is a anothor way to find factoria

# factorial using for loop

# num = int(input('Enter a number here::'))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print(f'The factorial of {num} is {factorial}')
