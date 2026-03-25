'''
Polymorphism means having many forms.

In programming, polymorphism means the same function name being
used for different types

Key difference is the data types and number of arguments used
in a function
'''

#Example of Built-in polymorphic functions
#len() beign used for strings
print(len("Hello")) #Return the number of characters

#len() being used for a list
print(len([10,20,30,40])) #return the number of elements

#Example of user-defined polymorphic function
def add(x,y,z = 0):
    return x + y + z

print(add(2,3))
print(add(1,2,3))

#Example of class methods, where we can have multiple classes
#with the same method name
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    #Move method
    def move(self):
        print("Drive!")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    #Move method
    def move(self):
        print("Sailin!")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    #Move method
    def move(self):
        print("Flyin!")

#Create a car,boat, and plane object
car1 = Car("Honda","Civic")
boat1 = Boat("Thing","5")
plane1 = Plane("Boeing","747")

#Invoke the move method
for x in (car1,boat1,plane1):
    x.move()
print()


#Inheritance Class Polymorphism
#CLasses with child classes with same name

#Super Class
class Vehicle():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    #Move method
    def move(self):
        print("Movin!")
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    #Move method
    def move(self):
        print("Sailin!")

class Plane(Vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    #Move method
    def move(self):
        print("Flyin!")

#Create a car,boat, and plane object
car1 = Car("Honda","Civic")
boat1 = Boat("Thing","5")
plane1 = Plane("Boeing","747")

#Invoke the move method
for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
    print()
    
print()

#Child classes inherits the properties and methods from the
#parent class. Car class is empty but it inherits brand, model
#move from Vehicle class
#Boat and Plane override the move() method because of polymorphism
#we execute the same method for all classes
















    














    

