#inheritance
#gaining the property of parent class

class Employee:
    def __init__(self,fn,ln):
        self.firtsname=fn
        self.lastname=ln
        
        
        
#     
class FullName(Employee):
    pass

class PartTimeEmployee(Employee):
    pass


f=FullName("Ram","Thapa")
        
    