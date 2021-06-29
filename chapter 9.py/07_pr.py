content = True
i = 1

with open('log.txt', 'r') as f:
    while content:
        content = f.readline()

        if 'python' in content.lower():
         # this lower function only read the lower case value of python
            print(content)
            print(f"Yes, python is present on line number {i}")

        i += 1


# lineNumber = 1

# with open('new2.txt') as f:
#     while True:
#         content = f.readline()

#         if 'python' in content.lower():
#             print(f'Yes, python is present in line number {lineNumber}')
#         lineNumber += 1

# # print(f'Yes, python is present in line number {lineNumber}')
