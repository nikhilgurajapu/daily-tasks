"""1.Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."
"""
list = [1,2,3,"six","seven",0.5]
if "six" in list:
    result = list.index("six")
    print(result)
else:
    print("Element not found")
