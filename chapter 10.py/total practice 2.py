# class Employee:
#     company = 'Google'
    
#     def getSalary(self):
#         print('Salary is not there')
# a = Employee()
# a.getSalary()
# print(a.company)


# class Employee:
#     company = 'google'
# harry = Employee()
# print(harry.company)
# Employee.company = 'Youtube'
# print(harry.company)
 



# class Employee:
#     company = 'google'
#     salary = 100
# harry = Employee()
# ashis = Employee()

# print(harry.salary)
# print(ashis.salary)
# harry.salary = 2100
# ashis.salary = 344
# print(harry.salary)
# print(ashis.salary)


# class Employee:
#     company = 'Google'

#     def getSalary(self):
#         print('Your salary is 100k')
# harry = Employee()

# # harry.getSalary()
# Employee.getSalary(harry)



# class Employee:

#     company = 'Google'

#     def getSalary(self):
#         print(f'the salary of the employee working in {self.company} is {self.Salary}')
# harry = Employee()
# harry.Salary = 2323
# harry.getSalary()


# a = (2021)
# print(type(a))





# class Employee:
#     company = 'Google'

#     def getSalary(self):
#         print(f'salary of the employee working in {self.company} is {self.Salary}')
    
#     @staticmethod
#     def greet():
#         print('Good morning , Ashis!')
#     @staticmethod
#     def news():
#         print('Ashis, do you hear today"s news')
# harry = Employee()
# harry.Salary = 3000
# harry.getSalary()
# harry.greet()
# harry.news()






# class Employee:
#     company = 'Google'

#     def __init__(self, name, salary, workplace):
#         self.name = name
#         self.salary =salary
#         self.workplace = workplace
#         print('Employee is already created now!')

#     def getDetails(self):
#         print(f'the name of the employee is {self.name}')
#         print(f'the salary of the employee is {self.salary}')
#         print(f'the workplace of the employee is {self.workplace}')

# harry = Employee('ashis', 100, 'Microsoft')
# harry.getDetails()



# class Programmer:
#     company = 'Microsoft'

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def getDetails(self):
#         print(f'the name of the programmer working in {self.company} is {self.name}')
#         # print(f'the salary of the programmer working in {self.company} is {self.salary}')

# harry = Programmer('Harry', 150000)
# ashis = Programmer('Ashis', 130000)
# harry.getDetails()
# ashis.getDetails()



# class calculator:

#     def __init__(self, number):
#         self.number = number

#     def square(self):
#         print(f'The square of {self.number} is {self.number **2}')
#     def squareRoot(self):
#         print(f'The squareRoot of {self.number} is {self.number ** 0.5}')
#     def cube(self):
#         print(f'The cube of {self.number} is {self.number **3}')

#     @staticmethod
#     def greet():
#         print('Hello, welcome to our new Calculator!')

 
# a = calculator(5)
# a.greet()
# a.square()
# a.squareRoot()
# a.cube()


# class Sample:
#     a = 'Harry'
# obj = Sample()
# obj.a = 'Ashis'
# Sample.a = 'Ashis'


# print(Sample.a)
# print(obj.a)




# class Sample:
#     def __init__(self, name):
#         self.name = name

# obj = Sample('Ashis')
# print(obj.name)




# class Train:

#     def __init__(self, name, status, seats):
#         self.name = name
#         self.status = status
#         self.seats = seats

#     def getStatus(self):
#         print(f'the name of the train is {self.name}')
#         print(f'{self.seats} are availabe in this {self.name} train')

#     def fareInfo(self):
#         print(f'each ticket price is {self.status}')
    
#     def bookTicket(self):
#         if (self.seats)>0:
#             print(f'Your ticket is booked, Your seat No. is {self.seats}')
#             self.seats = self.seats - 1
#         else:
#             print('No more Ticket in this train , Please contant another train')
     
#     def ticketPending(self):
#         print(f'Now {self.seats} ticket available in this {self.name} train')

# train = Train('Shatabdi', 300, 50)
# train.getStatus()
# train.fareInfo()
# train.bookTicket()
# train.ticketPending()