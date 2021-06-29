letter = '''Dear <|NAME|>, 
                You are selected!
               <|DATE|>                
'''
name = input('Enter your name here: ')
date = input('Enter the date here: ')
letter = letter.replace('<|NAME|>', name)
letter = letter.replace('<|DATE|>', date)
print(letter)


