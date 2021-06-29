# a = {1, 2, 3, 6, 7, 2, 1}
# print(type(a)) 

# a = {}        # this syntax will creat an empty dictionary and not an empty set 
# print(type(a))  

# an empty set can be created using the below syntax:

b = set()
b.add(2)
b.add(45)
b.add((1, 2, 3, 3))
b.add(3)
# b.add({"Harry": "A Coder"})# can not be added a dictionary in a set
                                        #  cannot add list or dictionary in sets but it also added touple 
                    # touple starts with ( ),,, but list starts with [   ],, and list can be changed or updated but a touple can not be changed or updated
                    # dictionary starts with { a:b }and sets are { , } 
# print(b)
# length of this set  
# print(len(b)) # print the length of this set means number of element 
# b.remove(45)  # remove 45 from the set
# b.pop()
# print(b.pop())
# print(b)
# b.clear()
# print(b.clear)