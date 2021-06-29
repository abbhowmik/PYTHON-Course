a = [3, 3, 34, 5, 54, 98, 34, 54, 55, 3]

# b = []
# for item in a:
#     if item % 2 == 0:
#         b.append(item)
# print(b)
# the other method to doing this Shocutly is mentioned in below


b = [i for i in a if i%2==0]
print(b)


# num = int(input('Enter a number:  '))
# for i in range(1, 11):
#     print(f'{i}X{num}={i*num}')
