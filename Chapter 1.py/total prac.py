# a = 'Hello world'
# print(a)



# import math 
# print('The value of sine is ', math.sin(60))
# print('The value of cosine is ', math.cos(60))
# print('The value of tangent is ', math.tan(60))
# print('The value of pi is ', math.pi)



# import pygame


# import os 
# print(os.listdir())



# from playsound import playsound
# playsound('C:\\Users\\HP\\Downloads\\Besharam Bewaffa - B Praak.mp3')



import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
         
            
     
while True:


    a = random.randint(0, 2)
    # print(a)

    if a == 0:
        comp = 's'
    elif a == 1:
        comp = 'w'
    elif a == 2:
        comp = 'g'



 
 

    
    print('Press q to quite')

    print('Comp Turn: Snake(s), Water(w) and Gun(g):  ')

    you = input('Your Turn :  Snake(s), Water(w) and Gun(g):  ')

    print('Enter q to quite: ')

    print(f'comp select: \n {comp}')

    print(f'you select: \n {you}')

    print(a)

     

    b = gamewin(comp, you)

    if b == None:
        print('The game is a Tie,\n \t play again to win ')
    elif b:
        print('Congratulation ! \n \t you win the game')
    else:
        print('You lose the game')