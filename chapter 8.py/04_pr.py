def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n + factorial_recursive(n-1)


f = factorial_recursive(5)
print(f)

# while True:

#     a = int(input('Enter a number here that you want to factoriate:: '))
#     factorial = 1
#     for i in range(a):
#         factorial = factorial * (i + 1)
#     print(f'The factorial of {a} is {factorial}')
