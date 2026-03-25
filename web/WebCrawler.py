'''
Description: Develop a program that will automaticall traverse
the documents on the web by following the hyperlinks.

This type of program is commonly known as a webcrawler

This process may continue forever,
we will exit the program when we have traversed 100 pages. 
'''

#import url lib request module
import urllib.request

#Create our main
def main():

    #prompt the user for the starting url
    url = input("Enter a URL: ").strip()

    #invoke the crawler function
    crawler(url)  #will traverse the web fromthe starting page


#Create our crawler function
def crawler(startingURL):
    #Create an epty list for appending already visited list
    listOfPendingURLs = []
    listOfTraversedURLs = []

    #Append our first URL
    listOfPendingURLs.append(startingURL)

    #Create a while loop
    #Note the continuation condition is if we have atleast 1 pending URL
    #and we havent traversed 100 URLS
    while len(listOfPendingURLs) > 0 and len(listOfTraversedURLs) <= 100:


        #Staore the first element in the pending to be checked
        urlString = listOfPendingURLs[0]

        #Delete the entry
        del listOfPendingURLs[0]

        if urlString not in listOfTraversedURLs:

            #appand the new URL into traversed list
            listOfTraversedURLs.append(urlString)

            #Display URL
            print("Crawl", urlString)

            #invoke hte getSubURLs to find all URLS in page
            for s in getSubURLs(urlString):
                #if it is na ew url, append it to the appending list
                if s not in listOfTraversedURLs:
                    listOfPendingURLs.append(s)

#Check the current URL for SubURLS
#Our current page has URLs we will sotre it into a list
#and return that list back  the caller to iterate through
def getSubURLs(urlString):


    #Create an empty list
    lst = []

    #Try block
    try:
        input = urllib.request.urlopen(urlString)

        text = input.read().decode()

        #Initilize our curent line to zero
        current = 0

        #int he current line looking fot text that starts with https
        current = text.find("https:",current)
        while current > 0:
            endIndex = text.find("\"", current)
            #ensure that a correct URL is found
            if endIndex > 0:
                lst.append(text[current:endIndex])
                current = text.find("https:", endIndex)
            else: #NO URL FOUND
                current = -1

    #Except block to catch errors
    except Exception as ex:
        print("Error:", ex)

    #return the list back to the caller
    return lst
#call main
main()



        

                                    
    
                    
        
    
