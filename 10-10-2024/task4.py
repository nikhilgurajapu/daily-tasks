"""3.Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, the last three numbers, and every second number in the list."""
l1 = [1,2,3,4,5,6,7,8,9,10]
output = l1[0:3]
print(output)
result = l1[-3:]
print(result)
stp = l1[1:11:2]
print(stp)