sub1 = int(input("Enter first subject number marks \n"))
sub2 = int(input("Enter second subject number marks \n"))
sub3 = int(input("Enter third subject number marks \n"))

if( sub1<33 and sub2<33 and sub3<33 ):
    print("You are fail because your marks are less than 33 in every subject")
elif(sub1+sub2+sub3)/3 < 40 :
    print("You are fail because your partentace is less than 40 ") 
else:
    print("Congratulation!, You are passed in exam ")