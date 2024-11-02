
#1.Create a class Person that has instance variables name, age, and gender. Add methods to:
#Initialize these variables.
#Update the age.
#Display the person's information.
# Exercise:
 #> Create multiple instances of the Person class.
 #> Change the age of one person and display the updated information.


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        
    def update(self, new_age):
        self.age = new_age
        print("Updated Age:", self.age)
  
p = []
num_of_persons = int(input("enter number of persons : "))
for i in range(num_of_persons):  
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    
    person = Person(name, age, gender)
    p.append(person)  

for person in p:
    person.display()

update_index = int(input("Enter an index value (0 for the first person): "))
update_new_age = int(input("Enter your new age: "))
p[update_index].update(update_new_age)

for person in p:
    person.display()



#2.Create a class Company that keeps track of the total number of employees using a static variable total_employees.
#  Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
#  Exercise:
#   >Create multiple employee instances.
#   >Print the total number of employee s after adding each new employee.
#   >Check whether changing the total_employees in one instance affects the others.
 
class College:
    employee_count = 0
    def __init__(self):
        self.ename = input("Enter Employee Name Here : ")
        self.edepartment = input("Enter Employee Deportment Here : ")
        College.employee_count += 1
 
    def display_count(self):
        print("Total Employees : ", College.employee_count)
 
    def display_details(self):
        print("Name of Employee : ", self.ename)
        print("Name of Employee Deportment : ", self.edepartment)
 
e1 = College()
print(e1)
e1.display_count()
e1.display_details()
 
e2 = College()
print(e2)
e2.display_count()
e2.display_details()
 
e3 = College()
print(e3)
e3.display_count()
e3.display_details()
 
#3.Create a class Rectangle that has instance variables length and width.
#  Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
#  Exercise:
#    >Create instances of the Rectangle class with different lengths and widths.
#    >Calculate and print the area for each rectangle.
 
class Rectangle:
    def get_data(self):
        self.length = int(input("Enter The Length : "))
        self.width = int(input("Enter the Width : "))
 
    def show_data(self):
        print("Length : ", self.length)
        print("Width : ", self.width)
 
    def area(self):
        print("Area : ", self.length*self.width)
 
rect = Rectangle()
rect.get_data()
rect.show_data()
rect.area()


#4.Create a class Employee where:
 # Each employee has an instance variable salary.
  #There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
 # Write a method total_salary that calculates the total salary for an employee (including the bonus).
 ## Exercise:
  # >Create several employee instances with different salaries.
  # >Change the bonus amount (static variable) and see how it affects all employees.
  # >Calculate and print the total salary for each employe

class employee:
    def __init__(self,emp_name,emp_salary):
        self.emp_name = emp_name
        self.emp_salary=emp_salary

    def dispaly(self):
        print("emp_name: ",self.emp_name)
        print("emp_salary: ",self.emp_salary)    
 
    def total_salary(self):
        sum = emp_salary + emp_bonus
        return sum
 
emp=[]
num_of_emp=int(input("number of employes :"))

for i in range(num_of_emp):
    emp_name = input("enter employee name : ")
    emp_salary = int(input("enter employee salary:"))
    emp.append(employee(emp_name,emp_salary))
 
emp_bonus = int(input("enter your bonus :"))   
 
for employee in emp:
    employee.dispaly()
    sum = employee.total_salary()
    print(f"Total salary : {sum}")    


