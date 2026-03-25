


#To create an emoty set use the set function
s = {} #Empty dictionary
s = set() #Empty set

print(type(s),s)

#create a set with three elements
s1 = {1,2,3}
print(s1)


#Create a set from a tuple
s2 = set((7,1,2,23,2,4,5))
print(type(s2),s2)

#Create a set form a list
s3 = set([7,1,2,23,2,4,5])
print(type(s3),s3)


#To remove all elements from a set we can use the clear() method
#s3.clear()
print(s3)

#A set is considered to be a non-homogenous: meaning it can contain
#different data types
s4 = {True, 3, 2.3, "Hello, World"}
print(type(s4),s4)


#Create a set from a string(a string is just a sequence of characters
#If a character appears twice it will only appear once in the set
#Remember sets do not have duplcates
s5 = set("abababacdcdc")
print(s5)

#CAN use the in and not in on sets
print(1 in s4)
print(1 not in s4)

#built-in function tha twe can use with sets
print(f"Length is {len(s3)}")
print(f"Max value is {max(s3)}")
print(f"Min value is {min(s3)}")
print(f"Sum value is {sum(s3)}")


#Create a set for our Summer MOnths
summer_months = {"June", "July", "August"}

#Create a set for the fall months
fall_months = set(("September", "October", "November"))

#Create a set for winter months
winter_months = set()

#Sets can be modifies, which makes them mutable objects
#We can add and remove elements from a set
#Using add and remove method
winter_months.add("December")
winter_months.add("January")
winter_months.add("February")


#Create a set for spring
spring_months = {"March", "April", "May"}

#May is already in the set it will not be added into
spring_months.add("May")
print(spring_months)


#must remove it to add
spring_months.remove("May")
print(spring_months)


#May is already in the set it will not be added into
spring_months.add("May")
print(spring_months)
print()


#If you try to remove something that is not in your set
#It will throw a key error exception
#spring_months.remove("Aprl")


#Can handle with a method
#Discard Method which will not throw the error
spring_months.discard("April")
print()


#Union | Difference |Intersection
#Add one more element to the seasons
summer_months.add("September")
fall_months.add("December")
winter_months.add("March")
spring_months.add("June")
print(f"Summer Months: {summer_months}")
print(f"Fall Months: {fall_months}")
print(f"Winter Months: {winter_months}")
print(f"Spring Months: {spring_months}")
print()
print()



#Intersection of two sets is a set that contains the elements
#That appear in both sets
#We can use the intersection mthod or the & operator
#Find the intersection of Fall and Summer
changeMonths = fall_months.intersection(summer_months) #The same thing
changeMonths = fall_months & summer_months #The same thing
print(f"Our intersection between fall and summer is {changeMonths}")
print()

#The union of a set is a set that contains all elements from both sets
#We can use union method OR |
changeMonths = changeMonths.union(fall_months.intersection(summer_months))
print(changeMonths)

changeMonths = changeMonths.union(fall_months.intersection(winter_months))
print(f"Union of fall and winter intersection is {changeMonths}")

changeMonths = changeMonths.union(winter_months.intersection(spring_months))
print(f"Union of winter and spring intersection is{changeMonths}")

changeMonths = changeMonths.union(spring_months.intersection(summer_months))
print(f"Union of spring and summer intersection is{changeMonths}") 

print()
print()






#Combine all months for the entire year
yearMonths = (summer_months.union(fall_months)).union\
             (winter_months.union(spring_months))
#Will display all 12 months
print(f"The 12 months of the year are {yearMonths}")
print()
print()




#Another example with colors
set1 = {"green", "red", "blue", "red"}
set2 = {"green", "yellow"}

#union using hte slash operator to add unique elements
set3 = set1 | set2 #OR
set3 = set1.union(set2)
print(f"The union of set1 and set2 is {set3}") #second red is a duplicate so it is removed
print()

#Difference between set1 and set 2 is a set that contains the elements in
#set1 but not set2
#can use difference method or minus operator
set3 = set1.difference(set2)
set3 = set1 - set2
print(f"The difference between set1 and set2 is {set3}")


#The intersection using hte or method or &
set3 = set1.intersection(set2)
set3 = set1 & set2
print(f"Intersection of set1 and set2 is {set3}")


#Symetric difference which is an exlusive or of two set
#is a set that contains the elements in either set but noth in both sets
#We can use our symetric difference methos or the carrot operator
set3 = set1.symmetric_difference(set2)
set3 = set1 ^ set2
print(f"The symmetric difference of set1 and set2 is {set3}")

#NOTE that the set operators can be used together in an expression
#Precedence order is -,&,^,|
#with difference being the highest
set4 = {1,2} | {1,3} - {1,4} & {2,3} ^ {3,5} #first will evaluate difference(-)
#{1,2} | {3,}, {2,3} ^ {3,5} Second evaluate Intersection(&)
#{1,2} | {3} ^{3,5} THird evaluate symmetric-difference (^)
#{1,2} | {5} Last we evaluate Union(|)
#{1,2,5}
print(set4)
print()

#Set Comprehension
#you can create sets using set comprehension
squared_set = {pow(x,2) for x in range(5)}
print(squared_set)
