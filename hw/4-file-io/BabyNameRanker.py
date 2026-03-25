#CS2030
#Problem 13.17 (Baby Name Ranker)
#Description:write a program to look up the popularity ranking of baby names
#from text files for the years 2001 to 2010 based on gender and year


#import request to fethc the file
import urllib.request


#Create a function to select the correct year file, and find the gender and name
#and return the rank of that name that year
#If it did not make hte list, then return that
def babyRank(year, gender, name):
    
    #Construct the URL for the specified year
    url = f"https://liveexample.pearsoncmg.com/data/babynameranking{year}.txt"

    #Fetch the file from the URL
    response = urllib.request.urlopen(url)

    #Read the content of the file directly
    #Decode the response and split into lines
    lines = response.read().decode('utf-8').strip().splitlines()  

    for line in lines:
        column = line.split()  #Split the line into parts
        rank = column[0]  #Rank of the name
        boyName = column[1]  #Male baby name
        boyCount = column[2]  #Count of male births
        girlName = column[3]  #Female baby name
        girlCount = column[4]  #Count of female births
        
        #Check if the name matches for the specified gender
        #Case insensitive comparison
        if gender == 'M' and boyName.lower() == name.lower():
            print(f"Boy name {name} is ranked #{rank} in year {year}")
            break
        elif gender == 'F' and girlName.lower() == name.lower():  
            print(f"Girl name {name} is ranked #{rank} in year {year}")
            break
    else:
        print(f"The name {name} is not in the top 1000 for the year {year}.")

        
#Create the main function
def main():
    #Prompt user for input
    year = input("Enter the year: ")
    gender = input("Enter the gender (M or F): ").upper()
    name = input("Enter the name: ")

    #Get ranking and display result
    babyRank(year, gender, name)

#Call main
main()
