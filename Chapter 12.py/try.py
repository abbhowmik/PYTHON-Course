# while True:
#     print('Press q to quit')

#     a = input("Enter a Number : ")
#     if a == 'q':
#         break
#     a = int(a)
#     if a > 6:
#         print('Yes you entered a number grater than 6')
#     elif a == 6:
#         print('You enter a number that is 6')
#     else:
#         print('you entered a number less than 6')
# print('Thanks for Playing us!')


while True:
    print('Press q to quit')

    a = input("Enter a Number : ")
    if a == 'q':
        break

    try:
        a = int(a)
        if a > 6:
            print('Yes you entered a number grater than 6')

        else:
            print('you entered a number less than 6')

    except Exception as e:
        print(f'Your input resulted in an error : {e}')

# print('Thanks for Playing us!')
# # thus we can avoid error in python
