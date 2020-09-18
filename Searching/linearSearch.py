def linearSearch(mylist, target):
    pos = 0 
    found = False

    while pos < len(mylist) and not found:
        if mylist[pos] == target:
            found = True
        else:
            pos = pos + 1
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(linearSearch(testlist, 3))
print(linearSearch(testlist, 13))