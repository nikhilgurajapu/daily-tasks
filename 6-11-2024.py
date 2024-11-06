"""
inheritence:-
        it inherits the properties from parent class to the child class.

types of inheritence:-
1.sigle inheritence:-  a child class inherits properties and methods from a single parent class.

2.multiple inheritence:- a class to inherit attributes and methods from more than one parent class.

3.hierachical inheritence:- inheriting properties and method from single class from multiple class at a same time.

4.multilevel inheritence:- inheriting properties from multilevel clases to single class.

5.hybrid inheritence:- using more then one type of inheritence.
"""

#example of single inheritence

class Animal:   # Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Child class 
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks as Bow Bow")

dog = Dog("choco")
dog.speak()


#example of multiple inheritence:-

class Worker:
    def do_work(self):
        print("Doing work")
 
class Manager:
    def manage(self):
        print("Managing the team")
 
class Employee(Worker, Manager):  #inherits both worker and manager class
    def perform(self):
        print("Performing employee duties")
 
employee = Employee()
employee.do_work()  
employee.manage()  
employee.perform()

#example of multilevel inheritence

class GF:
        def m1(self):
                self.car = "ambasidor"
class F(GF):
        def m2(self):
               print(self.car)
               self.car = "maruti alto"
class C(F):
        def m3(self):
                print(self.car)
                self.car = "creta"
                print(self.car)
c = C()
c.m1()
c.m2()
c.m3()

#example of heirachial inheritence:-
class gf:
    def __init__(self):
        self.land=20
 
class f(gf):
    def m1(self):
        print("father",self.land-10)
 
class c(gf):
    def m2(self):
        print("child",self.land-10)
 
F = f()
F.m1()
C = c()
C.m2()   


#example of hybrid inheritence:-
class Device:
    def power_on(self):
        print("Device powered on")
 
class Phone(Device):
    def make_call(self):
        print("Making a call")
 
class SmartPhone(Phone):
    def browse_internet(self):
        print("Browsing the internet")
 
class Laptop(Device):
    def run_program(self):
        print("Running program")
 
class SmartLaptop(Laptop):
    def video_call(self):
        print("Making a video call")
 
smartphone = SmartPhone()
smartphone.power_on() 
smartphone.make_call()  
smartphone.browse_internet()  
smartlaptop = SmartLaptop()
smartlaptop.power_on()   
smartlaptop.run_program() 
smartlaptop.video_call()  



