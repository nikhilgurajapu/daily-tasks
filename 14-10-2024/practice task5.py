#Different ways to clear a list in Python
list = ['kavya',"suneel","sathya"]
cleared_list = list.clear()
print(cleared_list)

list_len = len(list)
for i in range(list_len):
    list.pop()
print(list)