#Extending the string class

#create a class and extend string
class MyString(str):

    #initializer(constructor)
    def __init__(self, string = ' '):
        super().__init__()

    #return the index of the first occurence of a character
    #after fromIndex in the string. Return -1 if it doesnt match
    def indexOf(self,ch,fromIndex):
        for i in range(fromIndex, len(self)):
            
            #if we find it we reutn its index
            if self[i] == ch:
                return i

        return -1 #No character was found

    #return the index of the last occurence of a character
    #before fromIndex in the string return -1 if not matched
    def lastIndexOf(self,ch,fromIndex):
        for i in range(fromIndex, -1, -1):
            #if we find, return its index
            if self[i] == ch:
                return i

        return -1 #no character was found


#Create a main
def main():

    #defining hte constructor in the MyString class
    s = MyString("Programming is fun. Programming is fun.")

    #Search for the character i
    ch = 'i'

    #invoke indexOf and lastIndexOF
    print(s.indexOf(ch,10))
    print(s.indexOf(ch,23))
    print(s.lastIndexOf(ch,29))
    print(s.lastIndexOf(ch,4))


#invoke the main
main()
        
