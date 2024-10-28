"""
oops concept
mainly the full form of oops is:
Object oriented programing structure
Object-Oriented Programming is a way of approaching, designing and developing software,
so that the components of the software and the interactions between them resembles real-life objects and their interactions.

Proper usage of OOPS concepts helps us build well-organized systems that are easy to use and extend.

__init__:-
a special method __init__ is used to assign values to properties.



uses:-
it is used for better understanding code for developers
resuable code

coming to oops 
we have to know abot the classes and objects
Syntax for creating an instance of class looks similar to function call.


class:-
   class is a blueprint of the object

object:-
   object it is nothhing but a thing or a structure,An instance of class is Object.

instance methods of a class:-
        For instance method, we need to first write self in the function definition
           and then the other arguments.

Arguments:-
Similar to functions, Methods also support positional,
 keyword & default arguments and also return values.

"""
#example
class Mobile:
    def __init__(self, model, camera,price,ram):
        self.model = model
        self.camera = camera
        self.price = price
        self.ram = ram
        
    def display(self):
        print(self.model)
        print(self.camera)
        print(self.price)
        print(self.ram)

obj = Mobile("iPhone 16 Pro", "48 MP",111600,"6gb")
obj.display()

obj2 = Mobile("samsung S23","50 MP",65000,"8gb")
obj2.display()


class car:
   def __init__(self):
      self.brand = input("enter the brand name: ")
      self.model = input("enter the model name: ")
      self.color = input("enter the colour: ")
      self.price = input("enter the price: ")
      self.variant = input("enter the variant: ")

   def car_details(self):
      print(self.brand)
      print(self.model)
      print(self.price)
      print(self.variant)


car_1 = car()
print(car_1)
      

