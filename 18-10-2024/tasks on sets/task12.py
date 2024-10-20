#Check if two sets have any elements in common. If yes, display the common elements?
s1 = {1,2,3,4,5,6,34,657,789}
s2 = {1,2,3,4,763,9873.98734}
"""res = s1.intersection(s2)
print(res)"""
if s1.isdisjoint(s2):  #we use isdisjoin() method to check uncomon elements or not
    print("no comon elements")
else:
    print(s1.intersection(s2))

