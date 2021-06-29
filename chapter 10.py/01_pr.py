class Programmer:
    company = 'Microsoft'

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f'The name of the {self.company} programmer is {self.name} and the name of the prodct is {self.product}')

ashis = Programmer("Ashis", 'Mobile')
harry = Programmer('Harry', 'Cricket bat')

ashis.getInfo()
harry.getInfo()




