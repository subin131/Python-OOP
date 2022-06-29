#variables in oop
#instance variable which value changes from object to object also called object level variable
class Person:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
        
p=Person("ram","edfghnj")
r=Person("Gary","asdfg")

#static variables which values depends upon the class and doenot change from object to object and also called class level variable
class Student:
    school_name="subway"
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
        
p=Student("ram","edfghnj")
r=Student("Gary","asdfg")
#used to 
print(Student.school_name)



#instance method which is a method which used for instance variables
#instance varibale have self argument as a first argument
#object dependent instance method
def get_student_name(self):
    print(self.first_name)




#class method which is method which gives class dependent variables
#class method can be called using class Name.
@classmethod
def get_school_name(cls):
    print(Student.school_name)
    
    
    
#static method thats doesnot depend upon the class and object.
#decorator
@staticmethod
def print_gov_holiday():
    print("Teej Holiday")
    
    
p=Student("ram","shd")
Student.print_gov_holiday()