#2.Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not.
l1 = [1,"a",2,"b"]
x = l1

"""l1.remove(2)
print(l1)
print(x)"""
print(id(x))
print(id(l1))

print("--------------------------------")

list = l1.copy()
print(list)

print(id(list))
print(id(l1))