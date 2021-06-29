class Employee:
    company = 'Microsoft'
    eCode = 142


class Freelancer:
    company = 'Amazon'
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Employee, Freelancer):
    name = 'Ashis'


p = Programmer()
print(p.level)
print(p.company)
print(p.eCode)
p.upgradeLevel()
print(p.level)
print(p.name)
