#Write a python program to remove  specified column from the nestedlist?
list =[[1,2,3],[4,5,6],[7,8,9]]
for i in list:
    del i[0]
print(list)