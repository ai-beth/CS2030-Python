#Create the stack class
class Stack:

    #initializer
    def __init__(self):
        self.__elements = []

    #return true if the stack is empty
    def isEmpty(self):
        return len(self.__elements) == 0

    #return the element at the top of the stack
    #without removing it from the stack
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements) - 1]

    #stores an elelmetns into the top ofo the stack
    def push(self, value):
        self.__elements.append(value)


    #remove element at the top of the stack
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()

    #return the size ofthe stack
    def getSize(self):
        return len(self.__elements)


            
