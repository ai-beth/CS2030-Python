#Super function with single inheritance example
#Dogs, Cats, Cows, share common characteristics
#They are mammals, They have a tail, and four legs
#They are considered domestic


#Create a class
class Animals:

    #INitializing Constuctor
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True

        #MEthod to chech the animal is a mammal
    def isMammal(self):
        if self.mammals:
            print("It's a mammal!")
            
    #MEthod to check if the animal is domestic

    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal!")

#Create a dog subclass
class Dogs(Animals):
    #Initializing method Constructor
    def __init__(self):
        super().__init__()

    def isMammal(self):
        super().isMammal()

#Create a cow subclass
class Cows(Animals):
    #initilizing method constructor
    def __init__(self):
        super().__init__()

    #Check for tail and legs
    def TailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has all its legs and a tail")

#Test
hank = Dogs()
hank.isMammal()
print(hank.domestic)

bobby = Cows()
bobby.TailandLegs()
        
