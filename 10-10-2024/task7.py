"""2.Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results.
"""
l1 = ["kowshik","nikhil","neon","teena","swetha","manoj"]
l1.reverse()
print(l1)

print("-----------------------------")

result = l1[::-1]
print(result)

print(l1 == result)