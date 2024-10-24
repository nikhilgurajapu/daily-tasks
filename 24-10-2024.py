"""
module it is used for storing the  data and passing the data one module to another moduce for readability of code
modules are two types:-
1.costomized module and 
2.buit in module
1. costomized module is created by developers 
ex:- module_1,module_2
2.built in module means it is already exixting in python
ex:- math,random,datetime etc,.
"""
#here we are creating module_1 as coxtomized module
from module_1 import mul,add,even_nums

x=  10
y = 30
print(add(x,y))

print(mul(x,y))

x= [1,2,3,4,5,6,7,8,9,10]
print(even_nums(x))


#examples of built_in_modules:-

#functool module:- which is included in Python's standard library,
#provides essential functionality for working with high-order functions
 

from functools import reduce
list1 = [2, 4, 7, 9, 1, 3]
sum_of_list1 = reduce(lambda a, b:a + b, list1)
 
list2 = ["abc", "xyz", "def"]
max_of_list2 = reduce(lambda a, b:a if a>b else b, list2)
 
print('Sum of list1 :', sum_of_list1)
print('Maximum of list2 :', max_of_list2)

#Random Module:- The random module in Python is used to generates random numbers
# and provides the functionality of various random operations such as ‘random.randint()’,
# ‘random.choice()’, ‘random.random()’, ‘random.shuffle()’ and many more.
 
 
import random  
num = random.randint(1, 10)
print(f"Random integer between 1 and 10: {num}")


fruits = ["apple","mango","kiwi","jack","grapes"]
chosen_fruit = random.choice(fruits)
print(f"Randomly chosen language: {chosen_fruit}")


#datetime module:- The datetime module allows for manipulation and reading of date and time values.
#  Some of the basic method of “datetime” module are “datetime.date”, “datetime.time”,
#  “datetime.datetime”, and “datetime.timedelta”.
 
import datetime
 
print(dir(datetime))

print(datetime.time(12,50,30)) #we giving the hrs,mins,secs

print(datetime.datetime(2024,11,19)) #we giving the year,month and days value

 
