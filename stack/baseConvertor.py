from stack import Stack

def baseConvertor(decNumber, base):
    digits = '0123456789ABCDEF'

    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    bitString = ''
    while not remStack.isEmpty():    
        bitString = bitString + digits[remStack.pop()]
    return bitString    

print(baseConvertor(4,2))
print(baseConvertor(10,16))