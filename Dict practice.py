mydict = {
     "Pankha": "Fan",

     "Pani": "Water",

     "Pitaji": "Father",

     "Nanaji": "Grandfather"

}
print("Options are", mydict.keys())
a = input("Enter the hindi Word\n:") # if a word is not present in dictionart and if we don't 
# want to show an error, then we will apply mydict.get(a)
print(mydict[a])
print(mydict.get(a))
# print(mydict[a])