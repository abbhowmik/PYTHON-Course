# with open('1.txt', 'w') as f:
#     f.write('this is one.txt')

# with open('2.txt', 'w') as f:
#     f.write('this is two.txt')

# with open('4.txt', 'w') as f:
#     f.write('this is three.txt')


def readFile(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())

    except FileNotFoundError:
        print(f'{filename} file is not found')


readFile('1.txt')
readFile('3.txt')
readFile('4.txt')
