#Description: Operators and Special Methods demo

#Create two strings
s1 = "Washington"
s2 = "California"

#Use the index operator to find the element at index 0
print(f"The first character in s1 is {s1[0]}")

#Use the + operator to concatenate two strings
print(f"S1 + S2 is {s1 + s2}")

#Use the comparison operator to compare two strings
print(f"S1 < S2? {s1 < s2}")
print("----------------------")

#These operators can also be used on lists
#operators are actually methods defined in the str and list class

#Rewrite the above examples using methods from table
print(f"The first character in s1 is {s1.__getitem__(0)}")
print(f"S1 + S2 is {s1.__add__(s2)}")
print(f"S1 < S2? {s1.__lt__(s2)}")










