from dequeue import Dequeue

def palindromeChecker(str):
    charDequeue = Dequeue()

    for ch in str:
        charDequeue.addRear(ch)

    stillEqual = True 

    while charDequeue.size() > 1 and stillEqual:
        first = charDequeue.removeFront()
        second = charDequeue.removeRear()
        if first != second:
            stillEqual = False
    return stillEqual

print(palindromeChecker('radar'))
print(palindromeChecker("lsdkjfskf"))

