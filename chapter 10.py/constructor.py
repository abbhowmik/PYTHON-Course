class Employee:
    company = 'Google'

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print('Employee is created!')

    def getDetails(self):
        print(f'The name of the employee is {self.name}')
        print(f'The salary of the employee is {self. salary}')
        print(f'The subunit of the employee is {self. subunit}')


harry = Employee('Harry', 100, 'YouTube')
harry.getDetails()


# class Employee:
#     company = 'Microsoft'

#     def __init__(self, name, marks, division):
#         self.name = name
#         self.marks = marks
#         self.division = division

#     def getDetails(self):
#         print(
#             f"The name of the employee is {self.name}\nHis marks is {self.marks}\nHe got {self.division} division in exam")


# ashis = Employee('Ashis', 90, 'A')
# ashis.getDetails()
