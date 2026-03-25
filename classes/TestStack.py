#Description: Testing the stack class

#import Stack Class
from Stack import Stack

#create a stack object
stack = Stack()

#Push elements 0 - 9 ont the stack
for i in range(10):
    stack.push(i)

#Get the size of the stack
print(f"Stack size is {stack.getSize()}")

#peek at the top of the stack
print(f"Peek top of stack: {stack.peek()}")

#pop elemtns off the stack
while not stack.isEmpty():
    print(f"{stack.pop()}")
