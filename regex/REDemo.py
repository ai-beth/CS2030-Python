'''
A Regular Exprssion is a string that describes a pattern for
matching a set of strings. You can use r.e for matching , replacing, and
splitting strings

Examples: phone numbers, email address, zip codes, ssn, etc
'''
#Import the re module
import re
'''
#Regex string
regex = r"\d{3}-\d{2}-\d{4}" #SSN R.E

#Prompt the user to input a ssn
ssn = input("Enter S.S.N: ")

#Check if the input value matches the rules of our pattern
match1 = re.match(regex,ssn)

#Display the results if we do not return none
if match1 != None:
    print(f"{ssn} is valid")
    print(f"Starting postion of the match {match1.start()}")
    print(f"Ending position of the match {match1.end()}")
else:
    print(f"{ssn} is not valid")

#Telephone numbers
#(xxx)xxx-xxxx the first digit cannot be 0
regex = r"([1-9]\d{2})-\d{3}-\d{4}"

#Prompt the user to input a valid phone number
phone = input("Cell Phone: ")

match1 = re.match(regex,phone)

#Check if the results is not none
if match1 != None:
    print(f"{phone} is valid")
else:
    print(f"{phone} is not valid")
'''
#User Account Name
regex = "^[A-Z][a-z]{3,6}"
username = input("Please Enter Account Name: ")

#Check the username with the pattern
match1 = re.match(regex,username)

if match1 != None:
    print(f"Welcome {username}")
else:
    print("Account Name invalid")

#Stripping the user email at the @
regex = r"^(.*)(?=@)" #Capturing just the username
email = "minzey@ucmo.edu"
match = re.search(regex,email)

if match != None:

    #group() method returns the complete matched subgroup by default
    #or a tuple of matched subgroups depending on the number of args
    print("Username: ", match.group())

#\w matches any alphanumeric character [a-zA-Z0-9_]
regex = r"^(\w+)@(\w+).(\w+)$"
match = re.match(regex,email)

print(match.group()) #Entire match
print(match.group(1)) #First subgroup
print(match.group(2)) #Second subgroup
print(match.group(3)) #Third subgroup
print(match.group(1,2,3)) #tuple for all match subgroups
    
