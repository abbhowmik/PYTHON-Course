# i = 1
# while i<51:
#     print(str(i))
#     i = i + 1
# print('This is 1 to 50')


# i = 0
# while i<5:
#     print('Harry')
#     i = i + 1

# l = [1, 2, 3, 4]
# i = 0
# while i<len(l):
#     print(str(i))
#     i = i + 1


# l = [1, 2, 3]
# for item in l:
#     print(item)

# for i in range (0, 10):
#     print(i)


# l = [1, 2, 3, 4, 5, 7]
# for item in l:
#     print(item)
# else:
#     print('Done')

# for i in range(4):
#     if i == 2:
#         continue
#     print(i)


# i = [1, 2, 3, 4]
# for item in i:
#     pass


# a = int(input('Enter a number that you want to multiplicate ::  '))
# for i in range(1, 11):
#     print(f'{i}X{a} = {i*a}')
# print(f'this is the multliplication table of {a}')


# l = ["Harry", "Sohan","Sachin"," Rahul"]
# for name in l:
#     if name.startswith('S'):
#         print('Good Morning!, ' + name)


# a = int(input('Enter a number here::  '))
# i = 1
# while i < 11:
#     print(str(i) + 'X' + str(a) + '=' + str(i*a))
#     i = i + 1
# print('this is the multliplication table', str(a))


a = int(input('Please Enter a number here:: '))
prime = True
for i in range(2, a):
    if a % i == 0:
        prime = False
        break
if prime:
    print('Yes !, this number is a prime number')
else:
    print('No! this number is not a prime number')


# num = int(input('Enter the natarul number:: '))
# sum = 0
# while num>0:
#     sum = sum + num
#     num = num - 1
# print(f'the sum of  your natarul number is {sum} ')


# num  = int(input('Please Enter the number here that you want to factoriate!  ::'))
# factorial = 1
# while num>0:
#     factorial  =  num * factorial
#     num = num  - 1
# print(f"the factorial of your number is {factorial}")


# num = int(input('Enter a number'))
# factorial = 1
# for i in range(1, num + 1):
#     factorial = factorial * i
# print(f'the factorial of {num} is {factorial}')


# a = int(input('Please Enter a number :: '))
# for i in range(10, 0, -1):
#     print(f"{a}X{i}={a*i}")


# n = 3
# for i in range(n):
#     print("*" * (i + 1))
# print('this is the star pattern')


# n = 3
# for i in range(n):
#     print('*' * (n-i))


# n = 3
# for i in range(n):
#     print(" " * (n-i-1), end = '')
#     print("*" * (2*i + 1), end = '')
#     print(" " * (n-i-1), )


# n = 3
# for i in range(n):
#     print("*" * n)
#     # print("*" * n)
