#	Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
#Sample string : 'skywavessoftwares'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
s=input("enter the value :")
dict={}
for i in s:
    if i in dict:
        dict[i]=+1
    else:
        dict[i]=+1
print(dict)