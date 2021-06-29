class Employee:
    company = 'Google'

    def showDetails(self):
        print('This is an employee')


class Programmer(Employee):
    language = 'Python'
    company = "Youtube"

    def getLanguage(self):
        print(f'The language is {self.language}')
        print(f'The language is {self.company}')

    # def showDetails(self):
    #     print('This is an Programmer')


e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
p.getLanguage()
print(p.company)
print(e.company)
