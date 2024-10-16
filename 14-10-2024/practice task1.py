"""
Python program to exchange first and last elements in a list
Python program to swap two elements in a list
Python – Swap elements in String list
Python | Ways to find length of list
Maximum of two numbers in Python
Minimum of two numbers in Python
Python | Ways to check if element exists in list
Different ways to clear a list in Python
Python | Reversing a List
Python | Cloning or Copying a list
Python | Count occurrences of an element in a list
Python Program to find sum and average of List in Python
"""
def interchange_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst


l = [1,"sky",54,"thirty",8764,"flag"]
"""sl_1 =l[0]
sl_e  = l[-1]
sl_m = l[1:-1]
output = (sl_e.split()) + sl_m + sl_1
print(output)"""
output = interchange_first_last(l)
print(output)

list = ["kjnixc","bell" ,"cars","bikes","jeep"]

print(interchange_first_last(list))





