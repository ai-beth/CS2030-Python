#Import the circle class
from CircleWithPrivateRadius import Circle

#Create a 2 circle objects
c = Circle(5)
c1 = Circle()

#print(c.__radius) #Error because radius is private
#c.__radius = 7 #Not always will the interpter break
print("C Radius is", c.getRadius())
print("C1 Radius is", c1.getRadius())

c.setRadius(7)
print("C Radius is", c.getRadius())
print("C Perimeter is", c.getPerimeter())
print("C Area is", c.getArea())
