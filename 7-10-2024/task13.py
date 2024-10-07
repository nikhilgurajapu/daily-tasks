"""Python program to count alphabets, digits and special characters"""
given_str = "nikhil@123"
strn = 0
digit = 0
spcl_char = 0
"""for char in given_str:
  if char.isalpha():
        strn += char
print("alphabets = " + str(len(strn)))
numbers = len(given_str) - len(strn)
print(f"digits = {numbers}")"""

for i in range(len(given_str)):
    if given_str[i].isalpha():
        strn += 1
    elif given_str[i].isdigit():
        digit += 1
    else:
        spcl_char += 1
print(f"alphabets = {strn}")
print(f"digits = {digit}")
print(f"special char = {spcl_char}")
