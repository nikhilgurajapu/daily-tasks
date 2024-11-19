"""
encapsulation:-
        binding of data or properties into single unit

here we have public members 
            protected members  # identified with keeping an underscore before
            private members    #identified with keeping an double underscore before it
"""
class bank_account:
    def __init__(self):
        self.__acc_num = int(input("Enter Account Number Here : "))
        self.__pin_num = int(input("Enter PIN NUmber Here : "))
        self.__amount = int(input("Enter Amount Here : "))
        self.__balance = 0.0
   
    def deposite(self):
        __amount = int(input("Enter Amount Here : "))
        self.__balance += __amount
 
    def balance_details(self):
        print("Balance In Your Account : ", self.__balance)
 
    def withdraw(self,__amount,__pin_num):
        if self.__validate_PIN(__pin_num):
            if __amount <= self.__balance:
                self.__balance -= __amount
            else:
                print("Insufficient funds")
        else:
            print("Invalid PIN")
 
    def check_balance(self):
        print(self.__balance)
 
    def __validate_PIN(self, PIN):
        print(self.__PIN == PIN)
 
c=bank_account()
c.deposite()
c.withdraw(3453,10000)
c.check_balance()
c.__validate_PIN()




class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
 
    def get_employee_info(self):
        print(self.__name)
        print(self.__age)
        print(self.__salary)
 
    def increase_salary(self, percentage):
        self.__salary *= (1 + percentage / 100)
 
emp = Employee("nani", 25, 24000)
print(emp.get_employee_info())  
emp.increase_salary(10)
print(emp.get_employee_info())  
 



class bike:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0
 
    def accelerate(self):
        self.__speed += 10
 
    def brake(self):
        self.__speed -= 20
 
    def get_speed(self):
        return self.__speed
 
bike= bike("bullet", "battalion black", 2017)
bike.accelerate()
print(bike.get_speed())  
bike.brake()
print(bike.get_speed())  