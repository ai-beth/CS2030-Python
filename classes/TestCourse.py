#Import the Course Class
from Course import Course

#Create a main function
def main():

    #Create two courses
    course1 = Course("Data Structures")
    course2 = Course("Python Programming 2")

    #Add students into course 1
    course1.addStudent("John Wick")
    course1.addStudent("Hank Hill")
    course1.addStudent("Stan Smith")
    course1.addStudent("Bobby Hill")

    #Add students into course 2
    course2.addStudent("Peggy Hill")
    course2.addStudent("Roger Smith")
    course2.addStudent("Steve Smith")

    #Get the number of students in the courses
    print(f"Number of students in course1: \
{course1.getNumberOfStudents()}")

    print(f"Number of students in course2: \
{course2.getNumberOfStudents()}")

#invoke the main
main()
    
    
