# num = int(input('Enter a number:  '))
# table = [num*i for i in range(1, 11)]
# a = print(table)

# with open('mul.txt', 'a') as f:
#     f.write(str(table))
#     f.write('\n')


num = int(input('Please Enter a number : '))
table = [num*i for i in range(1, 11)]
# print(table)

with open('multable.txt', 'a') as f:
    f.write(str(table))
    f.write('\n')
