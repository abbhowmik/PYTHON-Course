# f = open('prac.txt')
# data = f.read()
# print(data)
# f.close()



# f = open('WoW.txt', 'w')
# f.write('Ashis is a good boy and he now trying to learn python')
# f.close()
# # thus we can create a txt file if the creating file does not supported



# with open('another.txt', 'r') as f:
#     data = f.read()
#     print(data)




# f = open('new.rt','w')
# data = f.write('Hey wassap guyes')  
# f.close()




# with open('WoW.txt') as f:
#     a = f.read()
#     print(a)
# with open('new.rt', 'w') as f:
#     a = f.write('whats your name and how are you')
#     print(a)
     




# with open('poems.txt', 'w') as f:
#     data = f.write('twilkle twinkle little star')
# print(data)




# f = open('poems.txt')
# t = f.read()

# if 'twinkle' in t:
#     print('Yes')
# else:
#     print('No')





# def game():
#     return 67
# gamescore = game()

# with open('poems.rb', 'r') as f:
#     highscore = int(f.read())

# if gamescore > highscore:
#     with open('poems.rb', 'w') as f:
#         f.write(str(gamescore))
#         print('Yes , you broke the highscore')



# def game():
#     return 68
# gamescore = game()

# with open('poems.rb') as f:
#     highscore = f.read()

# if  highscore=='':
#     with open('poems.rb', 'w') as f:
#         f.write(str(gamescore))

# elif int(highscore)=='':
#     with open('poems.rb', 'w') as f:
#         f.write(str(gamescore))




# f = open('donkey2.rb', 'w')
# f.write('hey donkey and donkey and donkey')
# f.close()
    


# with open('donkey2.rb') as f:
#     content = f.read()
# content = content.replace('donkey', '&*%#&8')

# with open('donkey2.rb', 'w') as f:
#     f.write(content)


# words = ['kaddu', 'mote', 'ashis']
# with open('donkey2.rb') as f:
#     content = f.read()
# for word in words:
#     content = content.replace(word, 'sdjflaj')

#with open('donkey2.rb', 'w') as f:
#       print("*" * n)
#       f.write(content)
 


       
# with open('log.txt') as f:
#     content = f.read()

# if 'python' in content.lower():
#     print('yes, python is present')
# else:
#     print('No, python is not present')



# i = 1

# with open('log.txt') as f:
#     while True:
#         content = f.readline()
#         if 'python' in content.lower():
#             print(f'python is present in line no. {i}')
#         i = i + 1



# # with open('this.rb') as f:
# #     content = f.read()
    
# # with open('copy.rb', 'w') as f:
#     f.write(content)
     


# with open('this.rb') as f:
#     content1 = f.read()

# with open('copy.rb') as f:
#     content2 = f.read()

# if content1==content2:
#     print('Yes, this two files are Identical')
# elif content1!=content2:
#     print('NO, this two files are not Identical')



# import os 
# oldname = 'new.rb'
# newname = 'renamed_by_python.txt'

# with open(oldname) as f:
#     content = f.read()
# with open(newname, 'w') as f:
#     f.write(content)

# os.remove(oldname)

