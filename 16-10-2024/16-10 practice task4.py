#removing of elements from the set
s={"1","two",34,0.5,True}
s.discard(True)
print(s) #set returns only in sequence order

s.remove(2)
print(s)# it returns exception becuase of 2 does not exist in s

s.pop()
print(s)

s.clear()
print(s)


"""del s
print(s)"""
