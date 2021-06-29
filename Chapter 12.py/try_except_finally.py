try:
    i = int(input('Enter a number:  '))
    a = 1/i
except Exception as e:
    print(e)
    exit()

finally:
    print('We are done!')

print('Well Done!')
