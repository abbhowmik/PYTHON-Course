# f = open('this.rb', 'w')
# f.write('I am this file\n this is good') # thus we can creat a text or read in binary or rb



with open('this.rb') as f:
    content = f.read()

with open('copy.rb', 'w') as f:
    f.write(content)
    