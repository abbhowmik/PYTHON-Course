# class Employee:
#     company = 'Google'

#     def showDetails(self):
#         print('This is an Employee')

# class Programmer(Employee):
#     language = 'Python'
#     # company = 'Youtube'

#     def getLanguage(self):
#         print(f'the language of the employee is {self.language}')

#     def showDetails(self):
#         print('Ashis is a programmer')

# e = Employee()
# p = Programmer()
# e.showDetails()
# p.showDetails()
# print(e.company)
# print(p.company)
  



# class Employee:
#     company = 'Microsoft'
#     level = 0


# class Freelancer:
#     company = 'Youtube'
#     fees = 500

#     def upgradeLevel(self):
#         self.level = self.level + 1

# class Programmer(Freelancer, Employee):
#     name = 'Ashis'

# p = Programmer()
# print(p.company)
# print(p.level)
# print(p.fees)
# p.upgradeLevel()
# print(p.level)




# class Employee:
#     company = 'Google'
#     language = 'Java'

#     def showDetails(self):
#         print('This is an Employee')

# class Programmer(Employee):
#     company = 'Microsoft'
#     language = 'Python'

#     def getLanguage(self):
#         print(f"Programmer's language is {self.language}")
    
#     def showDetails(self):
#         print('this is a programmer')
    
# e = Employee()
# p = Programmer()
# e.showDetails()
# p.showDetails()
# print(e.company)
# print(p.company)
# print(e.language)
# print(p.language)
 



# class Employee:
#     company = 'google'
#     ecode = 10

# class Freelancer:
#     company = 'Microsoft'
#     level = 0

#     def upgradeLevel(self):
#         self.level = self.level + 1
    
# class Programmer(Freelancer, Employee):
#     name = 'Ashis'

# p = Programmer()
# print(p.company)
# print(p.level)
# print(p.ecode)
# p.upgradeLevel()
# print(p.level)



# class Person:
#     country = 'India'

#     def takeBreathe(self):
#         print('I am breathing......')

# class Employee(Person):
#     company = 'Honda'
#     salary = 60000

#     def getSalary(self):
#         print(f'your salary is {self.salary}')

#     def takeBreathe(self):
#         print('I am an Employee, so i am breathing now..... ')
# class Programmer(Employee):
#     company = 'Flipkart'

#     def getSalary(self):
#         print('No salary for programmer!!')
#     def takeBreathe(self):
#         print('I am a programmer so i am luckily breathing....')

# # p = Person()
# e = Employee()
# pr = Programmer()
# p.takeBreathe()
# e.takeBreathe()
# pr.takeBreathe()
# print(p.country)
# print(pr.country)
# print(pr.salary)
# print(pr.company)





# class Person:
#     country = 'India'

#     def takeBreathe(self):
#         print('I am breathing......')

# # class Employee(Person):
# #     company = 'Honda'
# #     salary = 60000

# #     def getSalary(self):
# #         print(f'your salary is {self.salary}')

# #     def takeBreathe(self):
# #         super().takeBreathe()
# #         print('I am an Employee, so i am breathing now..... ')

# # class Programmer(Employee):
# #     company = 'Flipkart'

# #     def getSalary(self):
# #         print('No salary for programmer!!')

# #     def takeBreathe(self):
# #         super().takeBreathe()
# #         print('I am a programmer so i am luckily breathing....')

# # p = Person()
# # p.takeBreathe()

# # e = Employee()
# # e.takeBreathe()

# # pr = Programmer()
# pr.takeBreathe()





# class Person:
#     country = 'India'

#     def __init__(self):
#         print('Initializing Person ')

#     def takeBreathe(self):
#         print('I am breathing......')

# class Employee(Person):
#     company = 'Honda'
#     salary = 60000

#     def getSalary(self):
#         print(f'your salary is {self.salary}')
    
#     def __init__(self):
#         super().__init__()
#         print('Initializing Employee')

#     def takeBreathe(self):
#         super().takeBreathe()
#         print('I am an Employee, so i am breathing now..... ')

# class Programmer(Employee):
#     company = 'Flipkart'

#     def getSalary(self):
#         print('No salary for programmer!!')
    
#     def __init__(self):
#         super().__init__()
#         print('Initializing Programmer')

#     def takeBreathe(self):
#         super().takeBreathe()
#         print('I am a programmer so i am luckily breathing....')

# p = Person()
# p.takeBreathe()

# e = Employee()
# e.takeBreathe()

# pr = Programmer()
# pr.takeBreathe()




# class Employee():
#     company = 'google'
#     salary = 100
#     location = 'Delhi'

#     def changeSalary(self, salary):
#         self.__class__.salary = salary 

# e = Employee()
# print(e.salary)
# e.changeSalary(7876)
# print(e.salary)
# print(Employee.salary)





# class Employee:
#     company = 'Hondai'
#     salary = 5000
#     salarybonus = 400

#     @property
#     def totalSalary(self):
#         return self.salary + self.salarybonus
    
#     @totalSalary.setter
#     def totalSalary(self, val):
#         self.salarybonus = val - self.salary 

# e = Employee()
# print(e.totalSalary)
# e.totalSalary = 8900
# print(e.salary)
# print(e.salarybonus)



# class Number:
#     def __init__(self, num):
#         self.num = num
    
#     def __add__(self, num2):
#         print('lets add')
#         return self.num + num2.num
#     def __mul__(self, num2):
#         print('lets multiply')
#         return self.num * num2.num
# n1 = Number(4)
# n2 = Number(5)
# sum = n1 + n2
# mul = n1 * n2
# print(sum)
# print(mul) 



# class Number:
#     def __init__(self, num):
#         self.num = num
    
#     def __add__(self, num2):
#         print('lets add')
#         return self.num + num2.num

#     def __mul__(self, num2):
#         print('lets multiply')
#         return self.num * num2.num
#     def __str__(self):
#         return f'Decimal value is {self.num}'
#     def __len__(self):
#         return 1
# n = Number(8)
# print(n)
# print(len(n))





# class Employee:
#     salary = 50000
#     incremment = 1.2

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary * self.incremment

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, sai):
#         self.incremment = sai / self.salary
# e  = Employee()
# print(e.salaryAfterIncrement)
# print(e.incremment)
# e.salaryAfterIncrement = 70000
# print(e.incremment)


# class Complex:
    
#     def __init__(self, r, i):
#         self.real = r
#         self.imaginary = i

#     def __add__(self, c):
#         return Complex(self.real + c.real , self.imaginary + c.imaginary)

#     def __mul__(self, c):
#         mulReal = self.real*c.real - self.imaginary*c.imaginary
#         mulImg = self.real*c.imaginary + self.imaginary*c.real
#         return Complex(mulReal , mulImg)

#     def __str__(self):
#         return f'{self.real} + {self.imaginary}i'

# c1 = Complex(3, 2)
# c2 = Complex(1, 7)
# print(c1 + c2)
# print(c1 * c2)


# class Vector:

#     def __init__(self, vec):
#         self.vec = vec

#     def __str__(self):
#         a  = ""
#         index = 0
#         for i in self.vec:
#             a += f'{i} a{index} +'
#             index += 1
#         return a[:-1]

#     def __add__(self, vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return Vector(newList)

#     def __mul__(self, vec2):
#         b = 0
#         for i in range(len(self.vec)):
#             b += self.vec[i] * vec2.vec[i]
#         return b


# v1 = Vector([1, 4, 5])
# v2 = Vector([1, 2, 3])
# print(v1 + v2)
# print(v1 * v2)



# class Vector:

#     def __init__(self, vec):
#         self.vec = vec

#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k "


# v = Vector([1, 2, 3])
# v2 = Vector([2, 3, 4])
# print(v)
# print(v2)


