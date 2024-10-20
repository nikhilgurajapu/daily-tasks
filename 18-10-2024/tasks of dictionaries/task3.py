#	Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
"""for i in range(1,16):
    print(d["i"] = i**2)"""


dict_of_squares = {i: i**2 for i in range(1,16)}  # here we are using the code comprehension as lists
print(dict_of_squares)
d = {}

