
#1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"


def wish():
    greet="Hello"
    name= input("enter your name here : ")
    print(greet +' '+ name)
wish()
 
#2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.
 
def add():
    n1 = int(input("enter the n1 : "))
    n2 = int(input("enter the n2 : "))
    total = n1+n2
    print("sum = ", total)
add()
 
 
#3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
 
def is_even(n):
    if n % 2 ==0:
        return "Even"
    else:
        return "Odd"
n = int(input("Enter a number : "))
res = is_even(n)
print(f"The number {n} is {res}.")
 
 
#4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
 
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return (n * factorial(n-1))
c = int(input("entr the value : "))
result= factorial(n)
print("factorial of ", n,"is : ", result)

 
#5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.
 
def max_of_three(a,b,c):
    return max(a,b,c)
a=22
b=45
c=39
operation = max_of_three
print(max_of_three(a,b,c))
 

"""6.Write a function `count_vowels` that takes a string as input and returns the number of
 vowels (a, e, i, o, u) in the string.
"""
def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
 
result = count_vowels("Hello, World!")
print(result) 

"""7.Create a function `is_prime` that takes a number as input and returns `True` if the number
 is prime, and `False` otherwise."""

def is_prime(x):
    l = int(x)
    if l >= 0 and l%2 == 1:
        print("yes its a prime")
    else:
        print("no its not a prime")

x = input("enter the input: ")
is_prime(x)


"""8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns
the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` 
should return \(1 + 2 + 3 + 4 + 5 = 15\).
"""
def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)
    


#9.Write a function `calculator` that takes three parameters: two numbers and an operator
#  (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the
#  two numbers and return the result.
def calculator(n1, n2, operator):
    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    elif operator == "/":
        if n2 != 0:
            return n1 / n2
        else:
            return "Warning:  operation with zero not posible"
    else:
        return "Error: Invalid operator"
print(calculator(15, 5, "+"))
print(calculator(20, 2, "-"))
