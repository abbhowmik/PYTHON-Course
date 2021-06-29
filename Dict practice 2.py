# a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
# print(sum(a))

myDict = {   
       "Fast": "In a quick Manner",  
       "Harry":"A Coder",
       "anotherdict": {"Harry":"Player"},
       "Mark": [1,2,3,4,5], 
       1:2
}
# print(myDict["Mark"])
# print(myDict["Fast"])
# print(myDict["anotherdict"]["Harry"])
# print(type(myDict))
# print(list(myDict.values()))
# print(myDict.keys())
# print(type(myDict.items()))
# myDict['Mark']= [1, 2, 3, 4,]  
# print(myDict)
updateDict = {
              "Fast": "Student", 
              "Bhowmik": "A very Good Boy", 
              "Name": "What is your name?" 
}
myDict.update(updateDict)
print(updateDict)
   
# print(myDict.get("Harry2")) # return None as harry is not present in the myDictionary
# print(myDict["Harry2"])     # throws an error as harry2 is not present in the myDictionary 

print(myDict.get('Harry'))
