# def greet(name):
#     print(f'Good Morning, {name}')


# if __name__ == '__main__':
#     n = input('Enter a name :  ')
#     greet(n)

# this __name__ == '__main__': evaluates this files arguments  not
# others and it does not add as a module in another file


def greet(a):
    print(f'good morning, {a}')


if __name__ == '__main__':
    n = input('Enter a name:  ')
    greet(n)
