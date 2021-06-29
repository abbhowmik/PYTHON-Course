class Number:
    def __init__(self, num):  # the method are called as a dunder method
        self.num = num

    def __add__(self, num2):
        print('Lets add')
        return self.num + num2.num

    def __mul__(self, num2):
        print('Lets Multiply')
        return self.num * num2.num

    def __str__(self):
        return f'Decimal Number {self.num}'
        # this method return exact decimal number

    def __len__(self):
        return 1  # this return the lenth of the given argument or number


n = Number(9)
print(n)
print(len(n))
