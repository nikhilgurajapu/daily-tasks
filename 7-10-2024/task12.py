"""Python program to remove repeated character from string"""
given_str = "fearless"
str_2 = ""
for char in given_str:
    if char not in str_2:
        str_2 += char
print(str_2)