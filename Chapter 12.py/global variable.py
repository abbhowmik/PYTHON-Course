a = 54  # Global Variable


def func1():
    global a
    print(f'print statement 1 is : {a}')
    a = 7  # local variable  # if gloal variabl is not used
    print(f'print statement 2 is : {a} ')


func1()
print(f'print statement 3 is  : {a}')
