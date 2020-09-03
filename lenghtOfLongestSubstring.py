## PROBLEM SOLVED : Given a string, find the length of the longest substring without repeating characters.
'''
@staticmethod
def funcname(self, s):
    pass
'''

def FunctionName(str):
    arr = []
    i = 0
    counter = 0
    while i < (len(str)):
        if str[i] in arr:
            if counter < len(arr):
                counter = len(arr)
            arr = []
        arr.append(str[i])
        i += 1
    return counter
    
print FunctionName('abcd  abdcef  -- abc')

## SOLUTION
class Solution:
    def lengthOfLongestSubstring(self, s):
        arr = []
        i = 0
        counter = 0
        while i < (len(s)):
            if s[i] in arr:
                if counter < len(arr):
                    counter = len(arr)
                arr = []
            arr.append(s[i])
            i += 1
        return counter
## END OF SOLUTION
    def hello(self):
        print("hello there")
        return 

print Solution().hello()
print("test")
print Solution().lengthOfLongestSubstring('abcd  abdcef  -- abc')
hey = Solution()
hey.hello()
# 10