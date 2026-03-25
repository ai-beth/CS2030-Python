#CS2030
#Write a program to test the Fan, Stock, and Rectangle class

'''
Write a test program that creates two Rectangle objects:
    First object with the width of 4 and height of 40.
    Second object with the width of 3.5 and height of 35.7.
Display the width, height, area, and perimeter of each rectangle in this order.

Write a test program that creates a Stock object with the following information:
    Symbol = INTC
    Name = Intel Corporation
    Previous Closing Price = 20.5
    New Current Price = 20.35
Display the price-change percentage.

Write a test program that creates two Fan objects.
First object:
    Assign the maximum speed.
    Radius = 10.
    Color = yellow.
    Turn the fan on.
Second object:
    Assign medium speed.
    Radius = 5.
    Color = blue.
    Turn the fan off.
Display each object’s speed, radius, color, and on properties.

'''
from Fan import Fan
from Rectangle import Rectangle
from Stock import Stock



def main():

    #Problem 1
    print("Problem #1: ")
    print()
    
    #Create two rectangle objects
    #1. width = 4 height = 40
    rectangle1 = Rectangle(4,40)
    
    #2. width = 3.5 height = 35.7
    rectangle2 = Rectangle(3.5,35.7)
    
    #Display the width, height, area, perimeter IN THAT ORDER
    print("rectangle1")
    print(f"Width: {rectangle1.getWidth()}")
    print(f"Height: {rectangle1.getHeight()}")
    print(f"Area: {rectangle1.getArea()}")
    print(f"Perimeter: {rectangle1.getPerimeter()}")
    print()
    print("rectangle2")
    print(f"Width: {rectangle2.getWidth()}")
    print(f"Height: {rectangle2.getHeight()}")
    print(f"Area: {rectangle2.getArea()}")
    print(f"Perimeter: {rectangle2.getPerimeter()}")
    print()
    print()
    


    #Problem 2
    print("Problem #2: ")
    
    #Create a stock object with the following
    #Symbol = INTC
    #Name = Intel Corporation
    #Previous Closing Price = 20.5
    #New Current Price = 20.35
    stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)
    
    #Display the price-change percentage
    print()
    print("The price-change percentage is: ")
    print(stock.getChangePercent())
    print()
    print()


    #Problem 3
    print("Problem #3: ")
    print()
    
    #Create two fan objects
    #First object
    #Assign the maximum speed.
    #Radius = 10.
    #Color = yellow.
    #Turn the fan on.
    fan1 = Fan(Fan.FAST,10,"Yellow",True)
    #Second object:
    #Assign medium speed.
    #Radius = 5.
    #Color = blue.
    #Turn the fan off
    fan2 = Fan(Fan.MEDIUM,5,"Blue",False)
    
    #Display each object’s speed, radius, color, and on properties.
    print("Fan 1:")
    print(f"Speed: {fan1.getSpeed()}")
    print(f"Radius: {fan1.getRadius()}")
    print(f"Color: {fan1.getColor()}")
    print(f"On: {fan1.isOn()}")
    print()
    print("Fan 2:")
    print(f"Speed: {fan2.getSpeed()}")
    print(f"Radius: {fan2.getRadius()}")
    print(f"Color: {fan2.getColor()}")
    print(f"On: {fan2.isOn()}")


#Call the main
main()



















