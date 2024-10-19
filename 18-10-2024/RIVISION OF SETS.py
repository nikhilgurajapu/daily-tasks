#practice of dictionaries
d = {}
d["name"] = "nikhil"
print(d)

d["sex"] = "male"
print(d) #one of the way to update the dictionariess



d.update({"age":30})
print(d)# update() it updates the key value pair into the end of the dict


d.pop("name")
print(d)# pop() deletes the entire key valve of specific element

d.popitem() #it removes the last element of the dictionary
print(d)


del d["sex"]
print(d)


d.update({'name': "roshini","age": 18,"sex":"female"})
print(d)

print(d.get("name"))  #or d["name"] it returns the vale of specific key

print(len(d))




