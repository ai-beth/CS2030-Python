#Create the class
class Course:

    #Initializer method
    def __init__(self,courseName):
        self.__courseName = courseName
        self.__students = []

    #Method to add the student
    def addStudent(self,student):
        self.__students.append(student)

    #Method to get the student
    def getStudent(self):
        return self.__students

    #Method to get number of students
    def getNumberOfStudents(self):
        return len(self.__studnets)

    #Method to get course name
    def getCourseName(self):
        return self.__courseName

    #Method to drop the student
    def dropStudent(self,student):
        self.__students.remove(student)









    
