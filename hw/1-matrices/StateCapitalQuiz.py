#CS2030
#HW1 Problem 8.39
#Game: Guess the capitals
#Write a program that promts the user to repeatedly guess the US state capitals
#Case Insensitive, and then displays a total count


#List of states and their capitals
list = [
    ['Alabama', 'Montgomery'],
    ['Alaska', 'Juneau'],
    ['Arizona', 'Phoenix'],
    ['Arkansas', 'Little Rock'],
    ['California', 'Sacramento'],
    ['Colorado', 'Denver'],
    ['Connecticut', 'Hartford'],
    ['Delaware', 'Dover'],
    ['Florida', 'Tallahassee'],
    ['Georgia', 'Atlanta'],
    ['Hawaii', 'Honolulu'],
    ['Idaho', 'Boise'],
    ['Illinois', 'Springfield'],
    ['Indiana', 'Indianapolis'],
    ['Iowa', 'Des Moines'],
    ['Kansas', 'Topeka'],
    ['Kentucky', 'Frankfort'],
    ['Louisiana', 'Baton Rouge'],
    ['Maine', 'Augusta'],
    ['Maryland', 'Annapolis'],
    ['Massachusetts', 'Boston'],
    ['Michigan', 'Lansing'],
    ['Minnesota', 'Saint Paul'],
    ['Mississippi', 'Jackson'],
    ['Missouri', 'Jefferson City'],
    ['Montana', 'Helena'],
    ['Nebraska', 'Lincoln'],
    ['Nevada', 'Carson City'],
    ['New Hampshire', 'Concord'],
    ['New Jersey', 'Trenton'],
    ['New Mexico', 'Santa Fe'],
    ['New York', 'Albany'],
    ['North Carolina', 'Raleigh'],
    ['North Dakota', 'Bismarck'],
    ['Ohio', 'Columbus'],
    ['Oklahoma', 'Oklahoma City'],
    ['Oregon', 'Salem'],
    ['Pennsylvania', 'Harrisburg'],
    ['Rhode Island', 'Providence'],
    ['South Carolina', 'Columbia'],
    ['South Dakota', 'Pierre'],
    ['Tennessee', 'Nashville'],
    ['Texas', 'Austin'],
    ['Utah', 'Salt Lake City'],
    ['Vermont', 'Montpelier'],
    ['Virginia', 'Richmond'],
    ['Washington', 'Olympia'],
    ['West Virginia', 'Charleston'],
    ['Wisconsin', 'Madison'],
    ['Wyoming', 'Cheyenne']
]


#Initialize the correct answer count
count = 0

#Loop through each state in the list
for state, capital in list:
    #Prompt the user to guess the capital
    guess = input(f"What is the capital of {state}? ").strip().lower()
    
    #Check if the guess matches the capital (case-insensitive)
    if guess == capital.lower():
        print("Correct!")
        count += 1
    else:
        print(f"Wrong! The capital of {state} is {capital}.")

#Display the total number of correct answers
print(f"\nThe correct count is {count}.")
