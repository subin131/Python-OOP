#usecase of oop 
#class is generalization
#when we are representing the real world objects
#class is blue print of the object
#object is an instantiation of a class
class Person:
    pass

p=Person()
#where p is reference variable


#in python constructor is called initializer __init__ .. The use case is : it dtermine the size of the object and initialize the object
class Person:
    #special kind of function
    def __init__(self):
        self.first_name="Ram"
        self.last_name="Thapa"
        self.age=23
        
        
p=Person()
print(p.first_name)



#declarative programming