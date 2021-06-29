class Number:
    def __init__(self, num):  # the method are called as a dunder method
        self.num = num

    def __add__(self, num2):
        print('Lets add')
        return self.num + num2.num

    def __mul__(self, num2):
        print('Lets Multiply')
        return self.num * num2.num


n1 = Number(4)
n2 = Number(6)

add = n1 + n2
print(add)

mul = n1 * n2
print(mul)
