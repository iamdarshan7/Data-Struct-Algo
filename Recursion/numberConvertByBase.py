def convertor(num, base):
    convertString = "0123456789ABCDEF"

    if num < base:
        return convertString[num]
    else:
        return convertor(num//base,base)  + convertString[num%base]   
        

print(convertor(1453,16))        