#using for loop in set by using type conversion AND RETURN THE odd numbers

s = {1,2,3,4,5,6,7,8,9,10}
l = list(s)

for i in l:
    if i % 2 == 0:
        #print(i,end ="")
        l.remove(i)
print(l)
s= set(l)
print(s)