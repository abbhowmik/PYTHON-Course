class Employee:
    company = 'Bharat Gas'
    salary = 5000
    salarybonus = 500
    # totalSalary =  4500

    @property   # it is called getters method
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 7000
# print(e.salarybonus)
print(e.salary)
print(e.salarybonus)
