#modification of set
"""
set doesnt allow any modification if we want any modification we needto covert the datastructure
and again convert into set after modifying data
"""
s = {1,2,3,"two","nine"}
l = list(s)
l.append(8)

l.pop()

l.insert(2,"eighty")

s = set(l)# after all modifications the set returns in sequence oreder of the elements
print(s)