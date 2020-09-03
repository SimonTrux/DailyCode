#Given a list of numbers, where every number shows up twice except for one number, find that one number.

def singleNumber(arr):
    if type(arr) != type([]):
        return("Input not an array")
    tmpArr = []
    for n in arr:
        tmpArr.remove(n) if n in tmpArr else tmpArr.append(n)
    l = len(tmpArr)
    return tmpArr[0] if l == 1 else "No unique number found" if l == 0 else "More than 1 unique number found"

myArray = [4, 3, 2, 4, 5, 1, 5, 3, 2]

print (singleNumber(myArray))
