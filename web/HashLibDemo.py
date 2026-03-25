'''
Hash Library implements a common interface to many different secure hash
and message digest algorithms. (Secure hash and message digest) are inter
changeable

Note: Older algorithms were called message digests
'''
#import the hash and re
import hashlib, re

#Display the director of hashlib
for i in dir(hashlib):
    print(i)
print()

print("Algorithms Available")
for i in hashlib.algorithms_available:
    print(i)

#Create a password
pw = "abc123"

'''
Encode the password using MD5 ( Message Digest 5) Secure Hash Algorithm
return 128 bit hash value (32 characters each represent a hexadecimal)
64 bit hash which 16 charactres
encode() converts the string into bytes to be accepted by hash function
digiest() returns the encoded data in byte format
hexdigest() returns the encoded data in hexadeciaml format
'''
pwE = hashlib.md5(pw.encode())
print(f"Password: {pw}")
print(f"Md5 Hash Password: {pwE.hexdigest()}")
print()

#Sha256 (Secure Hash Algorithm
#returns 256 bit hash value (64 characters)
code = "012345"
shacode = hashlib.sha256(code.encode())
print(shacode.hexdigest())

#Common Password Requirements
print("1. Password must start with one of the following special\
characters !@#$%^&")
print("2. Password must contain at least one digit, one lowercase letter,\
and one uppercase letter")
print("3. Password is between 6 and 12 letters long")

#Password pattern
regex = r"^[!@#$%^&].*(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,12}$"

password = "@a2Bth7"

match1 = re.match(regex,password)

if match1 != None:
    print("Password is valid")
else:
    print("Password is invalid")


























