#Description: Input Output demo

#Create team list that is empty for now
team = []

#open original team input file
teamFile = open("team.txt", "r")

#Read our first line of the file
lastName = teamFile.readline()

#continue reading file until the end of the dile is reached
while lastName != ' ':
    #add anme into our empty list
    team.append(lastName)
    lastName = teamFile.readline()

#close origina file
teamFile.close()

#sort team names in aplhabetical order
teamNames.sort()

#create a new file for output
sortFile = ope("teamSorted.txt","w")

#Loop throug the team list and write one neame per line
for name in team:
    sortFile.write(name)

#Close sorted file
sortFile.close()
