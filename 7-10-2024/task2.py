""" Python Program to check if two Strings are Anagram. """
"""anagram means to check whether the chars of two strings are same or not"""
str_1 = "race"
str_2 = "care"
str_11 = str_1.lower()
str_22 = str_2.lower()
if sorted(str_11) == sorted(str_22):
    print("yes both the strings are anagrams")
else:
    print("NO both the strings are not anagrams")
