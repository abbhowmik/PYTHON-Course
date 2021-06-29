name = input('enter your name  : ')
marks = input('enter your marks : ')
phone = input('enter phone number: ')
template = ' The name of the student is {}, his marks is {} and phone number is {}'
output = template.format(name, marks, phone)
print(output)
