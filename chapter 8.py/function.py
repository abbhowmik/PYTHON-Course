def percent(marks):
    p = (sum(marks)/400)*100   # or ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100 
    return p                     # the space before p is called indentation


marks1 = [23, 34, 54, 33]
percentage1 =  percent(marks1)

marks2 = [12, 58, 78, 45] 
percentage2 = percent(marks2)

print(percentage1, percentage2)