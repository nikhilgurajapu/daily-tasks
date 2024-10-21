#	Write a python program to check weather the given value is present in the dictionary or not ?
val = input("enter the value: ")
d = {"name": "nikhil","age":24,"salary":30000}
if val in d.values(): #values() or keys() methods used to check selected keys or values present in dict or not
    print(val)
