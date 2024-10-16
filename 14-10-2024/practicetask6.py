#Python | Cloning or Copying a list
list = ['NANI',"MANOH","NIKHIL","SUSHMA","RAMYA"]
cpy_list = list.copy()
print(cpy_list)

#checking
#by copying the id should be changed
print(id(list))
print(id(cpy_list))