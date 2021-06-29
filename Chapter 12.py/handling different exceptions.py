
# try:
#     a = int(input('Enter a number: '))
#     c = 1/a
#     print(c)
#     exit()

# except Exception as e:
#     print('Exception occurs....')
#     print(e)
# print('Thanks for using this code...')


try:
    a = int(input('Enter a number: '))
    c = 1/a
    print(c)

except ValueError as e:
    print('Please Enter a valid value....')
    # print(e)

except ZeroDivisionError as e:
    print('Can"t divided by zero....')
    # print(e)

print('Thanks for using this code...')
# thus we can handle different types of error
