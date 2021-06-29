# f = open('what.rb', 'w')
# f.write('what is paper and go with a single')

# f = open('new.rb', 'w')
# f.write('for nothing but also but for coding')


import os
oldname = 'what.rb'
newname = 'new.rb'

with open(oldname) as f:
    content = f.read()

with open(newname, 'w') as f:
    f.write(content)
  # or--> content = f.write(content)

os.remove(oldname)
