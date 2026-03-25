#Description: Create a BMI object to display their status

#Import the BMI Class
from BMI import BMI

#Create a main function
def main():

    #Create a bmi object
    bmi1 = BMI("Tom Jerry",18,145,70)

    #Display Tom resutls
    print(f"The BMI for {bmi1.getName()} is {bmi1.getBMI()}, which puts \
you at {bmi1.getStatus()} status.")

    #Create a bmi object
    bmi2 = BMI("Stan Smith",45,202,74)

    #Display Stans results
    print(f"The BMI for {bmi2.getName()} is {bmi2.getBMI()}, which puts \
you at {bmi2.getStatus()} status.")

#Invoke the main function
main()
