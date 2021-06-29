class Employee:
  company = 'Google'

  def showDetails(self):
    print('This is an employee')
  
class Programmer(Employee):
  language = 'Python'
  company = "Youtube"
  
  def getLanguage(self):
    print(f'The language is {self.language}')
  
  def showDetails(self):
    print('This is an Programmer')

e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
print(p.company)
print(p.company)