from stack import Stack

def revStr(strings):
    oneStack = Stack()
    output = ''
    for str in strings:
        oneStack.push(str)

    while not oneStack.isEmpty():
        output = output + oneStack.pop()   
    return output   

print(revStr('dog'))   # output = god