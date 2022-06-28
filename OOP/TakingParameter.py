class Person:
    #special kind of function
    def __init__(self,fn,ln,ag):
        self.first_name=fn
        self.last_name=ln
        self.age=ag
        
      
p=Person("ram","thapa",34)
print(p.first_name)



#story of the self
#self is reference variable that pointing to the current running object
#The self value will not  change until next object pointing by the self

# everything is an object in python 