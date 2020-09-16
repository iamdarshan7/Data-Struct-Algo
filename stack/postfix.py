from stack import Stack

def toPostFix(exp):
    prec = {}
    prec['*'] = 3 
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    outputList = []

    tokenList = exp.split()
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            outputList.append(token)

        elif token == '(':
            opStack.push(token)

        elif token == ")":
            topToken = opStack.pop()        
            while topToken != '(':
                outputList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                outputList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        outputList.append(opStack.pop())                        
    return ''.join(outputList)


print(toPostFix("A * B + C * D"))
print(toPostFix("5 * B + 4 * D"))
print(toPostFix("( A + B ) * C - ( D - E ) * ( F + G )"))