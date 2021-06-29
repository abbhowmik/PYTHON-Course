# class Employee:
#     company = 'Google'

#     def getSalary(self):
#         print("Wow! Your Salary is 100K")


# harry = Employee()
# harry.getSalary()
# we can print this by this two of any one
# here self is a one type of Parameter that automatically passes value inside it
# Employee.getSalary(harry)


class Employee:
    company = 'Google'

    def getSalary(self):
        print(
            f'Salary for this employee working in {self.company} is  {self.Salary}')


harry = Employee()
harry.Salary = 10000
harry.getSalary()
