##Write a program to create a list of numbers on the range 1 to 10 , then delete all odd numbers from the list and print the final list.
list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    if i % 2 != 0:
        list.remove(i)
print(list)
        