from stack import Stack

def postFixEvaluation(postFixExp):
    operandStack = Stack()
    tokenList = postFixExp.split()

    for token in tokenList:
        if token in '0123456789':
            operandStack.push(token)
        else:
            operand2 = operandStack.pop()    
            operand1 = operandStack.pop()
            operand2 = int(operand2)    
            operand1 = int(operand1)    
            result = domath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()        

def domath(op,op1,op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2                        


print(postFixEvaluation('7 8 + 3 2 + /'))