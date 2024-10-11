"""1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
"""
even_num = []
odd_num = []
for i in range(1,21):
    if i%2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)
print(even_num)
print(odd_num)
    