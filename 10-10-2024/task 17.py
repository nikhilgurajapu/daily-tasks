"""Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).
"""

list = [1,4,3,4,5,2,3,4,5,6,7,8,7,6,8,8,7,]
list_1 = []
for i in list:
    if i not in list_1:
        list_1.append(i)
print(list_1)