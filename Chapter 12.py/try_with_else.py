try:
    i = int(input('Enter a number:  '))
    a = 1/i
except Exception as e:
    print(e)
else:
    print('We are succesfull!')

# print(a)
# if there are no error as a input value, then else exicuted 
