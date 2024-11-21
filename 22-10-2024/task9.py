from functools import reduce    #importing reduce from function tools

#we cannot acces the reduce() function with out importing
numbers = [1, 2, 3, 4,5,6,7,8,9]
res = reduce(lambda x, y: x + y, numbers)
print(res)



