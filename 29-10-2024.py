
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
 
def factorial(c):
    if c==1 or c==0:
        return 1
    else:
        return (c * factorial(c-1))
c = int(input("entr the value : "))
result= factorial(c)
print("factorial of ", c,"is : ", result)

 
#5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.
 
def max_of_three(a,b,c):
    return max(a,b,c)
a=22
b=45
c=39
operation = max_of_three
print(max_of_three(a,b,c))
 


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

