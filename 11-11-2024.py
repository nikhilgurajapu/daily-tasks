"""
polymorphism:-
           polymorphism means having many forms. In programming, polymorphism means the same function name
            (but different signatures) being used for different types.
            The key difference is the data types and number of arguments used in function

1.method overriding
2.mothod over loading

1.method overriding:-Method overriding is an ability of any object-oriented programming language 
that allows a subclass or child class to provide a specific implementation of a method that is
already provided by one of its super-classes or parent classes. When a method in a subclass
has the same name, the same parameters or signature, and same return type(or sub-type) as a method in its super-class,
then the method in the subclass is said to override the method in the super-class.

2.method overloading:-Method overloading is a feature in object-oriented programming that allows a class
to have multiple methods with the same name but different parameters. This can be achieved by changing
the number of parameters, the type of parameters, or both.
"""

#examples of polymorphysm
class Car:
    def move(self):
        print("Drive")

class Boat:
    def move(self):
        print("Sail")

class Plane:
    def move(self):
        print("Fly")

car = Car()
boat = Boat()
plane = Plane()

for vehicle in (car, boat, plane):
    vehicle.move()


#example 2
class bus:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive")

class bike:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("ride")

class lorry:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("ridder")

buses = bus("Ashok leyland", "Tata")     
bikes = bike("royal enfiled", "Ktm") 
lorrys = lorry("ashok leyland", "hitachi")    

for vehicle in (buses, bikes, lorrys):
  vehicle.move()