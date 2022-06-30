#important topics
#inheritance and incapsulation




#here varbale will be default public

#if you want to make variable private use __variable
class Person:
    __age=89
    def __init__(self):
        self.first_name="Ram"
        self.last_name="Thapa"
        self.age=23
        
        
p=Person()
print(p.first_name)
print(Person.__age);#it will give error because it is private



#getter and setter are used to access the  private variable
class Person:
    __age=89
    def __init__(self):
        self.first_name="Ram"
        self.last_name="Thapa"
        self.age=23
    #getter is used to get the value of the private variable    
    def get_age(self):
        return self.__age
    
    #setter is used to set the value of the private variable
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("age should be greater than 0")
                  
    
print(Person.get_age())

#getter has one parameter which is self
#setter have two parameter one is self and other is new value



