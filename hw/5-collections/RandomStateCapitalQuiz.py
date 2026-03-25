#CS2030
#Problem 14.10(Guess the Capitals)
#Will need to do 8.39
#Description: Rewrite 8.39 using a dictionary to store the pairs
#of states and capitals so that the questions are randomply displayed

#import random module
import random

#Dictionary of states and their capitals
statesAndCapitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "St. Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

#Create the main
#Will cycle through all 50 states randomly
#and give a correct count out of 50 in the end
def main():

    #Counter for correct answers
    correctCount = 0 
    
    #List of states (keys) for randomizing
    states = list(statesAndCapitals.keys())
   
    #Shuffle the states to randomize the order
    random.shuffle(states)  
    
    #Loop through all states and capitals
    for state in states:
        #Get the capital from the dictionary
        capital = statesAndCapitals[state]  
        
        #Prompt the user for their guess
        guess = input(f"What is the capital of {state}? ").strip()

        #Check if the guess is correct (case-insensitive)
        if guess.lower() == capital.lower():
            print("That's correct!")
            correctCount += 1
        else:
            print(f"That's not correct. The capital of {state} is {capital}.")

    #After all questions, print the total number of correct answers
    print(f"\nYou got {correctCount} of 50 correct!")

# Call the main
main()
