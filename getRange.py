#Given a sorted array, A, with possibly duplicated elements, 
#find the indices of the first and last occurrences of a target element, x. 
#Return -1 if the target is not found.

def getRange(arr, target):
    resArr = []
    i = 0
    while i < len(arr) and len(resArr) == 0:
        if arr[i] == target:
            resArr.append(i)
        i += 1
    j = len(arr) - 1
    while j > 0 and len(resArr) == 1:
        if arr[j] == target:
            resArr.append(j)
        j -= 1
    if len(resArr) == 0:
        return [-1, -1]
    else:
        return resArr

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 5

print getRange(arr, x)