# class Stack:

#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def push(self, item):
#         self.items.append(item)        

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[len(self.items)-1]

#     def count(self):
#         return len(self.items) 

from stack import Stack

def divBy2(decNumber, base):
    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    binString = ''
    while not remStack.isEmpty():    
        binString = binString + str(remStack.pop())
    return binString

print(divBy2(4,8))            