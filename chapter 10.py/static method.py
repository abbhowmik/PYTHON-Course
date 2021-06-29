class Employee:
    company = 'Google'

    def getSalary(self, Signature):
        print(
            f'Salary for this employee working in {self.company} is  {self.Salary}\n{Signature}')

    @staticmethod  # thus we announce a static method  ,, function and method is same
    def greet():
        print('Good Morning, Sir')

    @staticmethod
    def time():
        # thus we add staticmethod many times
        print('The time is now 3:30 PM in the evening')


harry = Employee()
harry.Salary = 10000
harry.getSalary('Thanks!')
harry.greet()
harry.time()


# class Employee:
#     company = 'Google'

#     def getSalary(self, Signature):
#         print(
#             f'Salary for this employee working in {self.company} is {self.Salary}\n{Signature}')

#     @staticmethod
#     def greet():
#         print('Good morning sir')

#     @staticmethod
#     def time():
#         print('the time is 2:20 am now sir')


# a = Employee()
# a.Salary = 500
# a.getSalary('Signature')
# a.greet()
# a.time()
