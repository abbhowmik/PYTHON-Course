# name = input("Enter your name\n")
# print("Good Afternoon," + name)

# a = input("Enter your name\n")
# print("Good Afternoon," + a )


letter = '''Dear <|Name|>,
you are selected!,welcome to our coding family 
and we are noticed that you are scoring well in exam as before like. That's why your selected
in our partnership and very very welcome
Date: <|Date|>
''' 
name = input("Enter your name\n")
date = input("Enter Date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)  


# letter =''' Dear <|Name|>, 
# # You are selected! in our company,,,,congratulation;and the date is 

# # Date:<|Date|>\n      You should come in this particular day and we are\'s celebrating in this date as an important day... 
# '''
# name = input("Enter your name\n")
# date = input("Enter date\n")
# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", date)
# print(letter)




#Assignment Operators 

# a = 3 
# a += 2
# a -= 2
# a *= 8
# a/= 8
# print(a)