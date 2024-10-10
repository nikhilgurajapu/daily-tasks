"""1.Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list.
"""
l1 = [1,2,3,4,5,6,7,8,9]
x = l1
print(x)

l1.pop()
print(l1)

print(x)

result = l1.copy()
print("                 ------------------------------                    ")


l1.pop()
print(l1)
print(result)
