"""
Static variables:- are defined inside the class definition,
 but outside of any method definitions. They are typically initialized 
 with a value, just like an instance variable, but they can be accessed and modified through the class itself, 
 rather than through an instance.

 static variables are not changing object to object
 we can declare the static variable inside the class directly 
 using class name we can access inside the constructor and instance method

 features of static variable:-
 1.memory efficiency
 2.acces through class
 3.constant behaviour

 Class Variables: Shared across all instances of the class.
 instance varible
 A variable that changes from object to object
 we can access instance variable inside class by using self keyword
 we can access outside of the class using ORV

"""
#using by directly taking the values
#example of static variable:-
class Car:
    wheels = 4  # This is a class variable (static variable)
    def __init__(self, make, model):
        self.make = make 
        self.model = model

#here we  Access the class variable
print(Car.wheels)  
car1 = Car("Toyota", "hyundai")
car2 = Car("Honda", "suziki")

print(car1.wheels)  #output is 4
print(car2.wheels)  
Car.wheels = 6
print(car1.wheels)  # Outputs: 6
print(car2.wheels)



#using input method to take values
#for example we take a bank sector
class account:
    def __init__(self):
        self.balance = 0
        print("New Account Created.")
    def deposit(self):
        amount = float(input("Enter amount to Deposit : "))
        self.balance += amount
        print("New Balance : ", self.balance)
    def withdraw(self):
        amount = float(input("Enter amount to Withdraw : "))
        if amount > self.balance:
            print("insufficent balance")
        else:
            self.balance -= amount
            print("New Balance : ", self.balance)
    def Total_Balance(self):
        print("Total Balance : ", self.balance)

account = account()
account.deposit()#20,000 assuming the input
account.withdraw()#10000  assuming withdrawl amount
account.Total_Balance()#10,000 the result

