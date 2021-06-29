

try:
    a = int(input('Please enter the first number:: '))
    b = int(input('Please enter the second number:: '))
    c = (a/b)
    print(c)

except ValueError as e:
    print('Please enter a valid value')

except ZeroDivisionError as e:
    print('the value of this division is infinite')

print('Thanks for using out code!!!')