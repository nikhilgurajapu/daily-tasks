#Write a python program to combine two dictionaries by adding values of common keys ?
d = {"a":30,"age":25,"salary":25000}
t = {"a":55,"age":19,"sex":"female"}
p ={}
for key in t:
    if key in d:
        t[key] += d[key]
    else:
        pass

print(t)

            
            


