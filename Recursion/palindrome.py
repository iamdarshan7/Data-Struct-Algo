def palindRecur(str, s, e):
    
    if s == e:
        return True

    if (str[s] != str[e]):
        return False    

    if s < e + 1:
        return palindRecur(str, s+1, e-1) 

    return True        


def palind(str):

    n = len(str)

    if (n == 0):
        True

    return palindRecur(str, 0, n-1) 

str = 'madam'
if palind(str):
    print("Yes")
else:
    print('No')        