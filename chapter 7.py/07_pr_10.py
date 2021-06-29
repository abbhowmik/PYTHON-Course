# num = int(input("Pleade enter a number"))
# # print("List of number in reverse order from {0} to 1 : " .format(num))
# while num>=1:
#     print(num , end = '  ')
#     num = num - 1 


# num = int(input("Pleade enter a number"))
# # print("List of number in reverse order from {0} to 1 : " .format(num))
# for i in range(1, 11):
#     print(f"{num}X{i}={num*i}")

for i in range(1,10):
	for j in range(1,i+1):
		print(str(i)+"*"+str(j)+"="+str(i*j)+" ",end="")
	print()

 #str(x) convert i to a string, end="" terminate py wrap
   #print() makes a line break after calculating a loop
