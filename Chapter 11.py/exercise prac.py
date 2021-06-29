# class C2dVec:
#     def __init__(self, i, j):
#         self.icap = i 
#         self.jcap = j

#     def __str__(self):
#         return f'{self.icap}i + {self.jcap}j'
    
# class C3dVec(C2dVec):
#     def __init__(self, i, j, k):
#         # self.icap = i
#         # self.jcap = j # or
#         super().__init__(i, j)
#         self.kcap = k

#     def __str__(self):
#         return f'{self.icap}i + {self.jcap}j + {self.kcap}k'
    

# a = C2dVec(2, 3)
# b = C3dVec(1, 2, 3)
# print(a)
# print(b)





class Animal:
    animalType = 'Mammal'

class Pets:
    colour = 'Black'

class Dog:
    @staticmethod
    def bark():
        print('bow bow')
d = Dog()
d.bark()