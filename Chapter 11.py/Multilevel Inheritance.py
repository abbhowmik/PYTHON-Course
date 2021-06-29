class Person:
    country = 'India'

    def takeBreathe(self):
        print("I am breathing.....")


class Employee(Person):
    company = "Honda"
    Salary = 1999

    def getSalary(self):
        print(f'Salary is {self.Salary}')

    def takeBreathe(self):
        print('I am an Employee, so i am luckily breathing')


class Programmer(Employee):
    company = 'Fiver'

    def getSalary(self):
        print('NO salary for Programmer')

    def takeBreathe(self):
        print('I am a Programmer, so i am luckily breathing')


p = Person()
e = Employee()
pr = Programmer()
p.takeBreathe()
e.takeBreathe()
pr.takeBreathe()  # it takees the latest value
print(pr.company)
print(pr.Salary)
print(pr.country)
pr.getSalary()
e.getSalary()
