words = ['donkey', 'kaddu', 'mote']


with open('donkey.rb', 'r') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$$%^&#")
    with open('donkey.rb', 'w') as f:
        f.write(content)


# words = ['donkey', 'kaddu', 'mote']

# with open('new2.txt') as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word, 'new')
# with open('new2.txt', 'w') as f:
#     f.write(content)
