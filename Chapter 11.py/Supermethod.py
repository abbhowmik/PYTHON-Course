class Person:
    country = 'India'

    def __init__(self):
        print('Initializing Person ')

    def takeBreathe(self):
        print("I am breathing.....")


class Employee(Person):
    company = "Honda"
    Salary = 1999

    def __init__(self):
        super().__init__()   # this works as same as super method
        print('Initializing Employee ')

    def getSalary(self):
        print(f'Salary is {self.Salary}')

    def takeBreathe(self):
        super().takeBreathe()
        print('I am an Employee, so i am luckily breathing')


class Programmer(Employee):
    company = 'Fiver'

    def __init__(self):
        super().__init__()
        print('Initializing Programmer ')

    def getSalary(self):
        print('NO salary for Programmer')

    def takeBreathe(self):
        super().takeBreathe()
        print('I am a Programmer, so i am luckily breathing')


# p = Person()
# p.takeBreathe()

# e = Employee()
# e.takeBreathe()

pr = Programmer()
pr.takeBreathe()  # it takees the latest value

# so super method firstly check its  parents argument and then returns its own argument
