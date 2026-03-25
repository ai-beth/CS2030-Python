#Create the BMI class
class BMI:

    #Initialize the Object
    def __init__(self,name,age,weight,height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    #Compute the BMI
    def getBMI(self):
        #Name constant for the conversion values
        KILO_POUND = 0.45359237
        METERS_INCH = 0.0254

        #Calculate the bmi
        bmi = self.__weight * KILO_POUND / \
              (pow(self.__height * METERS_INCH, 2))

        #Return the bmi to the caller
        return round(bmi * 100) / 100

    #Find the status of our current bmi
    def getStatus(self):
        bmi = self.getBMI()

        #Multi-way to check the status
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    #Getter methods
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight

    def getHeight(self):
        return self.__height














    










        











    

        

        
