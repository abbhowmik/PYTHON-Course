class Employee:
    salary = 1000
    incremment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.incremment


    @salaryAfterIncrement.setter
    def  salaryAfterIncrement(self, sai):
        self.incremment = sai/self.salary


e = Employee()
print(e.salaryAfterIncrement)
print(e.incremment)
e.salaryAfterIncrement = 4000
print(e.incremment)

