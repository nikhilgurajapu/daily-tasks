#prin#1. Write a Python program to calculate the length of a string.
 
#2. Write a Python program to count the number of characters (character frequency) in a string.
#Sample String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
 
 
#3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3'
#Sample String : ' w'
#Expected Result : Empty String
 

str = "nikhil"
len_str = len(str)
print(len_str)

str_1 = "kowshik"
len = 0
for i in str_1:
    len += 1
print(len)

"""s = "polymorphysm"
index = {}
for i in set(s):
    index[i] == s.count(i)
    for char,count in index.items():
        print(f"'{char}': {count}")
"""
my_string = "Nikhil gurajapu"
char_count = {}
 
for char in set(my_string):  # Using set to avoid duplicate characters
    char_count[char] = my_string.count(char)
 
# Print the character count
for char, count in char_count.items():
    print(f"'{char}': {count}")



v = "nikhil"
res = v[0:2] + v[-2:]
print(res)

r = "w3"
print(r*2)

s2="kowshik"
print("before: ",s2)
name = s2.replace("kowshik","")
print("after: ",name)

"""1. Single Inheritance
Problem Statement: Create a base class Animal with an attribute name and a method speak(). Then, create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".

Tasks:
Define a base class Animal with an __init__ method that takes name as a parameter.
Define a method speak() in Animal that prints "Animal sound".
Create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".
Create an instance of Dog and call the speak() method."""

class Animal:
    def __init__(self,name,breed,color):
        self.name = name
        self.breed = breed
        self.color = color
    
    def speak(self):
        print(self.name)
        print(self.breed)
        print(self.color)

class dog(Animal):
    def speak(self):
        self.barks = "bow bow..."
        print(self.name)
        print(self.breed)
        print(self.color)
        print(f"{self.name} barks as {self.barks}")

d = dog("tillu","shitzu","brown")
d.speak()



"""
1.Problem Statement: Create a class Teacher with an attribute subject. Then, create a
class Researcher with an attribute field. Finally, create a class TeachingResearcher that inherits from both Teacher and Researcher,
and has an additional method to display both attributes.

Tasks:
Define a Teacher class with an __init__ method to initialize subject.
Define a Researcher class with an __init__ method to initialize field.
Define a TeachingResearcher class that inherits from both Teacher and Researcher,
 and has an __init__ method to initialize both subject and field. Add a method to display both.
Create an object of TeachingResearcher and display its attributes.
"""

# Teacher class
class Teacher:
    def __init__(self):
        self.subject = input("subject name: ")

# Researcher class
class Researcher:
    def __init__(self):
        self.field = input("enter the field: ")

class TeacherResearcher(Teacher, Researcher):
    def __init__(self):
        Teacher.__init__(self)
        Researcher.__init__(self)
        
    def display(self):
        print(f"Subject: {self.subject}")
        print(f"Field: {self.field}")


tr = TeacherResearcher()
tr.display()




"""
Problem Statement: Create two base classes: Bird and Flyable. Bird should have an attribute species, and Flyable should have a method fly().
 Then, create a derived class Eagle that inherits from both Bird and Flyable.

Tasks:
Define a class Bird with an attribute species.
Define a class Flyable with a method fly() that prints "Flying".
Create a class Eagle that inherits from both Bird and Flyable, and has a method to display species and flying capability.
Create an instance of Eagle and call its methods.
"""

class bird:
    def __init__(self):
        self.species = input("enter the species: ")

class flyover:
    def flyable(self):
        self.flyable = input("enter the flyable: ")

class eagle(bird,flyover):
    def __init__(self):
        bird.__init__(self)
        flyover.flyable(self)

    def display(self):
        print(self.species)
        print(self.flyable)

e=eagle()
e.display()