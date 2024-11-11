"""
polymorphism:-
           polymorphism means having many forms. In programming, polymorphism means the same function name
            (but different signatures) being used for different types.
            The key difference is the data types and number of arguments used in function

it have two methods 
1.method overriding
2.mothod over loading

1.method over riding:-
"""
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