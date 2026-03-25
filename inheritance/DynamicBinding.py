#Create a student class (C2)
class Student:
    #Override str method
    def __str__(self):
        return "Student"

    #Method to display instance of student
    def printStudent(self):
        print(self.__str__())

#Create a Graduate Student class (C1) subclass of (C2)
class GraduateStudent(Student):
    #Override str method
    def __str__(self):
        return "Graduate Student"

#Display student and Grad Student
a = Student()
b = GraduateStudent()

a.printStudent() #Using the printStudent method in the student class
b.printStudent() #Also using the printStudent method 

#Another example Dynamic BInding
#Object Class (C4)

class Animal: #(C3)
    def speak(self):
        print("Generic animal noises!")

class Dog(Animal): #(C2)
    def speak(self):
        print("Bark Bark!")

class Cat(Animal): #(C1)
    def speak(self):
        print("Meow Meow!")

#Create a function to make the animal sounds
def make_sounds(animal):
    animal.speak()

#Create a dog and cat
dog = Dog()
cat = Cat()

#Make them speak
make_sounds(dog)
make_sounds(cat)



















    











