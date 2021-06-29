with open('donkey.rb', 'r') as f:
    content = f.read()
content = content.replace('donkey', "in order")

with open('donkey.rb', 'w') as f:
    f.write(content)


# with open('new2.txt') as f:
#     content = f.read()
# content = content.replace('you', 'Ashis')
# with open('new2.txt', 'w') as f:
#     f.write(content)
