
with open('this.rb') as f:
    content1 = f.read()
with open('copy.rb') as f:
    content2 = f.read()

if content1 == content2:
    print('Files are identical')
else:
    print("Files are not identical")
