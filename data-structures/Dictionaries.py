'''
A dictionary is ac ontainer object that stores a collection of key value pairs

It enables fast retrieval/deletion an dupdating of the values by accessing
their corresponding key values

The key in a dictionary can be any hashable object like numbers and strings
NOTE: You can not have duplicate keys as each key maps to one value

Dictionary keys are immutable objects (numbers / Strings)



'''

#Create an empty dictionary
students = {}
students = dict()


students = {"700-1":"Ashley", "700-2":"Tony"}
print(students["700-2"])



#adding modifying and retrieving values
students["700-3"] = "Stan"
students["700-4"] = "Roger"
students["700-5"] = "Steve"

print(students)


#modyfing current values
students["700-3"] = "Stan Smith"
print(students)

#Note: If you try to retrieve a key that does not exist you will get a KeyError exception
#print(students["700-8"])

#Deleintg items
#use the delete keyword from the item
del students["700-2"]

#or you can use the pop method
students.pop("700-5")
print(students)


