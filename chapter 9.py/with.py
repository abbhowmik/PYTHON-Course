# with open('anothertext.rt', 'r') as f:
#     a = f.read()
# print(a)  # thus we open other files content in this same programme


# and  by the below mention method, we can change a files content and print here in same programme

with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write("Hey bro! how are you and whats the going on")
print(a)


# with open('new2.txt', 'w') as f:
#     a = f.write('Hey Ashis , what is going on ')
# print(a)
