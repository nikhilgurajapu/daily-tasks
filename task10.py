"""program that counts the number of even and odd numbers in a list"""
li = [1,2,3,4,5,6,7,8,9]
count_li = len(li)
even_li = []
odd_li = []
for i in range(1 , count_li + 1):
    if i % 2 == 0:
        even_li.append(i)
for i in range(1 , count_li + 1):
    if i % 2 != 0:
        odd_li.append(i)
count_even = len(even_li)
count_odd = len(odd_li)
print(f'number of even numbers is {count_even}')
print(f'number of odd numbers is {count_odd}')