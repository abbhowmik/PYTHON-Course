for i in range(2, 21):
    with open(f'folder/Multiplication_table_of_{i}.txt', 'w') as f:
        for j in range(1, 11):
            f.write(f'{i}X{j}= {i*j}')
            if i != 21:
                f.write('\n')


# for i in range(2, 21):
#     with open(f'folder/Multiplication_table_of {i}.txt', 'w') as f:
#         for j in range(1, 11):
#             f.write(f'{i}X{j} = {i*j}')
#             if i != 21:
#                 f.write('\n')
