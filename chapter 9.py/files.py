# f = open('sample.rb')  # here rb refers that this files is a binary type
# data = f.read()  # reads first  5 character from the file
# print(data)
# f.close()

f = open('sample.rb')
data = f.readline()  # read  the first line of the programme
print(data)
f.close()
