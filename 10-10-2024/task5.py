"""1.Write a Python program that initializes a list with some numbers and:
2.Adds a new number to the list using the append() method.
3.Inserts a number at the second position using insert().
4.Extends the list with another list of numbers.
5.Remove all occurrences of the number 3 from a list of integers.
Write a Python program to remove the last element of a list using pop() and print the updated list."""


l1=[1,2,3,7,9,10,14,3,6,7]
l1.append(8)
print(l1)

print("---------------------")

l1.insert(4,6)
print(l1)

print("---------------------")

l2=[5,6,7,8,9,10]
l1.extend(l2)
print(l1)

print("------------------------")

l1.remove(3)
l1.remove(3)
print(l1)

print("------------------------------")

l1.pop()
print(l1)