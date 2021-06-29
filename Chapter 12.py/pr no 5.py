# with open('Tables.txt', 'w') as f:
#     f.write('')

num = int(input('Enter a number:  '))
table = [num*i for i in range(1, 11)]
a = print(table)

with open('Tables.txt', 'a') as f: # here a refers to append 
    f.write(str(table))
    f.write('\n')