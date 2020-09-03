#You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.
#
#Example:
#Given [4, 7, 1 , -3, 2] and k = 5, 
#return true since 4 + 1 = 5.

def two_sum(list, k):
    i = 0
    j = 1
    while i < len(list):
        val = list[i]
        while j < len(list):
            if val + list[j] == k:
                return val, list[j]
            j += 1
        i += 1
        j = i + 1


myList = [4,7,1,-3,2]
print (two_sum(myList, 8))