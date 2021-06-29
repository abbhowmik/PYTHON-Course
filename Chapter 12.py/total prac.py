# while True:
#     print('Press  q to quit:  ')
#     a = input('please enter a number:: ')
#     if a == 'q':
#         break
#     try:
#         a = int(a)
#         if a >6:
#             print('Yes, you entered a number that is grater than 6')
#         else:
#             print('you entered a number less than 6')
#     except Exception as e:
#         print(f'''Your input value is not the right argument according to the question a
# and error is ::  {e}, Please select according to the question''')
# print('Thanks for Playing with us')



# def increment(num):
#     try:
#         return int(num) + 1
#     except:
#         raise ValueError('this is not valid')
        
# a = increment('eawd')
# print(a)


# try:
#     i = int(input('Enter a number::'))
#     a = 1/i
# except Exception as e:
#     print(e)
# else:
#     print('We are successfull!!')




# try:
#     i = int(input('Enter a number::'))
#     a = 1/i
# except Exception as e:
#     print(e)
#     exit()
# finally:
#     print('We are successful!')



# def greet(name):
#     print(f"good morning! {name}" )

# if __name__ == '__main__':
#     n = input('Please enter a name: ')
# greet(n)


# a = 3
# def func1 ():
#     global a
#     print(f'print statesment 1 is :: {a}')
#     a = 34
#     print(f'print statesment 2 is :: {a}')
#     a = 45
#     print(f'print statesment 3 is :: {a}')
# func1()
# print(f'print statesment 4 is :: {a}')



# a = [2, 3, 4, 5, 6, 7, False, 'ashis']

# # index = 0
# # for item in a:
# #     print(index, item)
# #     index += 1

# for index, item in enumerate(a):
#     print(index, item)



# a = [4, 2, 5, 6, 6, 7, 34, 45, 34, 12, 23, 24, 45]

# # b = []
# # for item in a:
# #     if item % 2 == 0:
# #         b.append(item)
# # print(b)

# b = [i for i in a if i % 2 ==0]
# print(b)
# b = [i for i in a if i % 2 !=0]
# print(b)



# a = [4, 2, 5, 6, 6, 7, 34, 45, 34, 12, 23, 24, 45]
# s = {i for i in a}
# print(s)


# try:
#     n = int(input('Please enter a number::'))
#     a = 1/n
#     print(a)

# except ValueError as e:
#     print('please enter a valid number')

# except ZeroDivisionError as e:
#     print(" can't divided by zero")

# print('thanks for playing with us')


# def readFile(filename):

#     try:
#         with open(filename, 'r') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f'{filename} file is not found')
# readFile('1.txt')
# readFile('3.txt')
# readFile('4.txt')
 

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for index, item in enumerate(a):
#     if index==2 or index==4 or index== 6:
#         print(f'the {index + 1}th element is {item}')



# with open('mul.txt', 'w') as f:
#     f.write('the man')


# a = int(input('Please Enter a number :: '))
# table = [ a * i for i in range(1, 11)]
# a = print(table)

# with open('mul.txt') as f:
#     print(f.read())

# with open('mul.txt', 'w') as f:
#     f.write(str(a)) 



# try:
#     a = int(input('Please enter the first number:: '))
#     b = int(input('Please enter the second number:: '))
#     c = (a/b)
#     print(c)

# except ValueError as e:
#     print('Please enter a valid value')

# except ZeroDivisionError as e:
#     print('the value of this division is infinite')

# print('Thanks for using out code!!!')
