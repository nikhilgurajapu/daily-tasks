"""
types of arguments:-
positional arguments 
keyword argumets  ///args as */
variable lenght keyword arguments   ///kwargs as **/
default arguments"""

#****Positional Arguments: Values can be passed without using argument names.
#These values get assigned according to their position.
#Order of the arguments matters here. 
def greet(arg_1, arg_2): 
    print(arg_1 + arg_2) 
arg_1 = 30
arg_2 = 40 
greet(arg_1,arg_2)

#***Keyword Arguments: Passing values by their names. 

def greet(arg_1, arg_2): 
    print(arg_1 + " " + arg_2) # Good Morning Ram 
greet(arg_1="Good Morning", arg_2="Ram") 

#***Default Arguments: by defaultly takes the none by this we didn't get any exceptions
"""def greet(arg_1="Hi", arg_2=None): 
    print(arg_1 + " " + arg_2) # Hi Ram 
greeting = input()
name = input() 
greet()
"""
#Variable Length Arguments: Variable length arguments are packed as tuple. 

def more_args(*l):
  print(l) # (1, 2, 3, 4) 
more_args(1, 2, 3, 4)  




#1. Write a Python function to check whether a number falls within a given range.
n = 6
given_r = 10
for i in range(given_r):
    if n == i:
        print("yes number is in the range")


print("---------------------------------------------------------------------------")

#2. Write a Python function that accepts a string and counts the number of upper and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

str = "The quick Brow Fox"
upper = []
lower = []
for i in str:
    if i.isupper():
        upper.append(i)
    else:
        if i.islower():
            lower.append(i)

"""print(upper)
print(lower)"""

u = len(upper)
l = len(lower)

print(f"number of upper charectors : {u}")
print(f"number of lower charectors : {l}")

print("---------------------------------------------------------------------")

#3. Write a Python function that takes a list and returns a new list with unique elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

sl = [1,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,7,9]
ml = set(sl)
print(list(ml))



 #4. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
#Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.       

n = 7
if n >= 0 and n % 2 == 1:
    print("yes it is a prime")
else:
    print("not a prime")

#5. Write a Python program to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]

sen = [1,2,3,4,5,6,7,8,9]
even = []
for i in sen:
    if i % 2 == 0:
        even.append(i)
print(even)
    