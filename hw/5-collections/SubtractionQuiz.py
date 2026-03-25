#CS2030
#Problem 14.12 (Subtraction Quiz)
#Description:Rewrite Problem 7.36 to store the answers in a set
#rather than a list


#import random
import random

#Generate two random single-digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

#If number1 < number2, swap number1 with number2
if number1 < number2:
    number1, number2 = number2, number1

#Set to store answers
answers = set()

#Prompt the user to answer 
while True:
    answer = int(input(f"What is {number1} - {number2}? "))
    
    #Check if the answer has already been entered
    if answer in answers:
        print(f"You've already entered {answer}.")
        continue
    
    #Store the answer
    answers.add(answer)
    
    #Check if the answer is correct
    if number1 - number2 == answer:
        print("You got it!")
        break
    else:
        print("Wrong answer. Try again.")
