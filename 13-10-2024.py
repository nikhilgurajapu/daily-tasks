# Abstraction in Python is a concept that allows you to hide complex implementation details and show only the essential features of an object or function. It helps in reducing complexity by providing a clear interface and hiding unnecessary information.
 
 
#1. Abstract Classes: These are classes that cannot be instantiated directly and may contain abstract methods that must be implemented by subclasses. You can create abstract classes using the abc (Abstract Base Class) module.
 
 
#2. Abstract Methods: Methods in an abstract class that have no implementation. They must be overridden in any subclass.
 
 
 
#Example:
 
from abc import ABC, abstractmethod
 
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
 
class Dog(Animal):
    def make_sound(self):
        print("Bark")
 
dog = Dog()

#Real time example of abstraction:-
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @abstractmethod
    def show_speed(self):
        pass
 
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."
    
    def stop_engine(self):
        return "Car engine stopped."
    
    def show_speed(self):
        return "Car speed: 120 km/h."
 
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started."
    
    def stop_engine(self):
        return "Bike engine stopped."
    
    def show_speed(self):
        return "Bike speed: 80 km/h."
class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started."
    
    def stop_engine(self):
        return "Truck engine stopped."
    
    def show_speed(self):
        return "Truck speed: 60 km/h."
 
vehicles = [Car(), Bike(), Truck()]
 
for vehicle in vehicles:
    print(vehicle.start_engine())
    print(vehicle.show_speed())
    print(vehicle.stop_engine())
    print()
