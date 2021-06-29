# f = open('log.txt', 'w')
# f.write('harry')



with open('log.txt', 'r') as f:
    content = f.read()
if 'python' in content.lower(): # this lower function only read the lower case value of python 
    print("Yes, python is present")
else:
    print("NO, python is not present")