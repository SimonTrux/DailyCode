#Given a sorted array, A, with possibly duplicated elements, 
#find the indices of the first and last occurrences of a target element, x. 
#Return -1 if the target is not found.

def getRange(arr, target):
    return [findFirstIndex(arr, target), findLastIndex(arr, target)]

def findFirstIndex(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target: return i
        i += 1
    return -1

def findLastIndex(arr, target):
    j = len(arr) - 1
    while j > 0:
        if arr[j] == target: return j
        j -= 1
    return -1

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
y = 5
z = 8
w = 4

print getRange(arr, x)
print getRange(arr, y)
print getRange(arr, z)
print getRange(arr, w)