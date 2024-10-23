from functools import reduce    #importing reduce from function tools

#we cannot acces the reduce() function with out importing
numbers = [1, 2, 3, 4,5,6,7,8,9]
res = reduce(lambda x, y: x + y, numbers)
print(res)


tuple= ('a','b','c','d','e','f','g','h','i','j')
print(tuple[0:2]) # ('a', 'b')
print(tuple[-1:-5:-2]) # ('j',)
print(tuple[1:7:2]) # ('b', 'd', 'f')
