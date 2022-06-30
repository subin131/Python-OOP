#poly-multi and mephism is the different form

class Employee:
    def __init__(self,fn,ln):
        self.firtsname=fn
        self.lastname=ln
        
        
    def calculate_salary(self):
        print("I am parent class")
        
class FullName(Employee):
    def calculate_salary(self):
        print("I am full time  class")

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("I am part time  class")


f=FullName("Ram","Thapa")


#method overriding is used to override the method of parent class
# above the method calculate_salary is overridden from parent class by FullTime and PartTime class
#to create the uniformity in the code
        

