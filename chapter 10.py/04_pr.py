class calculator:
    
    def __init__(self, number):
        self.number = number
    
    def square(self):
        print(f'The value of {self.number} square is {self.number **2}')
         

    def squareRoot(self):
        print(f'The value of {self.number} squareRoot is {self.number **0.5}')


    def cube(self):
        print(f'The value of {self.number} square is {self.number **3}')

    @staticmethod
    def greet():
        print('***Hey! Welcome to the best calculator programme in the world***')
    

a = calculator(9)
a.greet()
a.square()
a.squareRoot()
a.cube()
