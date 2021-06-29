# class Employee:
#     company = 'Google'
# harry = Employee()
# a = harry.company
# Employee.company = 'Youtube'
# b = Employee.company
# print(b)
# print(a)





# class Employee:
#     company = 'Google'
#     salary = 100
# harry = Employee()
# ashis = Employee()
# harry.salary = 200
# ashis.salary = 300
# print(harry.salary)
# print(ashis.salary)
 





# class RailwayForm:
#     formType = 'RailwForm'

#     def allData(self):
#         print(f'Your name is {self.name}')
#         print(f'Your trani is {self.train}')

# ashisApplication = RailwayForm()
# ashisApplication.name = 'Ashis'
# ashisApplication.train = 'Rajdhani Express'
# ashisApplication.allData()






# class Employee:
#     company = 'Google'

#     def getSalary(sef):
#         print('Wow! Your salary is 100k')
     
# harry = Employee()
# # harry.getSalary()
# Employee.getSalary(harry)#we can use one of this two method





# class Employee:
#     company = 'Microsoft'

#     def getSalary(self):
#         print(f'Salary of this Employee working in the {self.company} Company is {self.Salary}')
    
# harry = Employee()
# harry.Salary = 50000
# harry.getSalary()





# use of __init__ function
# class Employee:
#     company = 'Google'

#     def __init__(self, name, salary, subunit):
#         self.name = name 
#         self.salary = salary
#         self.subunit = subunit
#         print('Employee is created!')

#     def getSalary(self):
#         print(f'the name of the Employee is {self.name}')
#         print(f'the salary  of the Employee is {self.salary}')
#         print(f'the subunit of the Employee is {self.subunit}')

# harry = Employee('Ashis','50k','Youtube')
# harry.getSalary()





# class Employee:
#     company = 'Youtube'

#     def getSalary(self, Signature):
#         print(f'the salary of the employee working in {self.company} is {self.Salary} \n {Signature}')
#     @staticmethod
#     def greet():
#         print('Good Morning! Ashis')
#     @staticmethod
#     def time():
#         print('The time is 4:56 PM in the Evening')
# harry = Employee()
# harry.Salary = 244444
# harry.getSalary('Wow!')
# harry.greet()
# harry.time()






# class Remote:
#     pass
# class Player:
#     def moveright(self):
#         pass 
#     def moveleft(self):
#         pass 
#     def moveTop(self):
#         pass  
# remote1 = Remote()
# player1 = Player()

# if(remote1.isLeftPressed()):
#     Player.moveleft()






# class Programmer:
#     company = 'Microsoft'

#     def __init__(self, name, product):
#         self.name = name
#         self.product = product
#     def getInfo(self):
#         print(f'the name of the {self.company} programmer is {self.name} and the product is {self.product}')

# ashis = Programmer('Ashis', 'Mobile')
# harry = Programmer('Harry', 'Telephone')
# ashis.getInfo()
# harry.getInfo()

    



# class calculator:

#     def __init__(self, number):
#         self.number = number

#     def square(self):
#         print(f'the square of {self.number} is {self.number ** 2}')
#     def squareRoot(self):
#         print(f'the squareRoot of {self.number} is {self.number ** 0.5}')
#     def cube(self):
#         print(f'the cube of {self.number} is {self.number ** 3}')

# a = calculator(3)
# a.square()
# a.squareRoot()
# a.cube()






# class Sample:
#     a = 'Harry'

# obj = Sample()
# obj.a = 'Ashis'
# print(Sample.a)
# print(obj.a)
# yes we can change the value of the class






# class calculator:

#     def __init__(self, number):
#         self.number = number

#     def square(self):
#         print(f'the square of {self.number} is {self.number ** 2}')
#     def squareRoot(self):
#         print(f'the squareRoot of {self.number} is {self.number ** 0.5}')
#     def cube(self):
#         print(f'the cube of {self.number} is {self.number ** 3}')
#     @staticmethod
#     def greet():
#         print('Welcome to our coding competetion!')
    
# a = calculator(3)
# a.square()
# a.squareRoot()
# a.cube()
# a.greet()





# class Sample:
#     def __init__(self, name):
#         self.name = name 
# wow = Sample('Harry')
# print(wow.name)






class Train:

    def __init__(self, name, fare, seats):
        self.name = name 
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f'the name of the train is {self.name}')
        print(f'Now {self.seats} are available in this Train')

    def getInfo(self):
        print(f'every ticket price is Rs: {self.fare}')

    def getTicket(self):

        if self.seats>0:
            print(f'Your ticket is booked, and your ticket no. is {self.seats}')
            self.seats = self.seats - 1

            print(f'now available seats is {self.seats}')

        else:
            print('No more seats available in this train, Please contact another train')

News = Train('Shatabdi Express:  2344', 50, 600)
News.getStatus()
News.getInfo()
News.getTicket()

# News.getTicket()





         