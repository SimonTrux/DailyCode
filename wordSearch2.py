#You are given a 2D array of characters, and a target stringing. 
#Return whether or not the word target word exists in the matrix. Unlike a standard word search, 
#the word must be either going left-to-right, or top-to-bottom in the matrix.
# ==> I did also right to left and bottom to top

def lineString(array):
    resStr = ""
    for c in array:
        resStr = resStr + c
    return resStr
    
def colString(matrix):
    resArr = []
    resStr = ""
    i = 0
    j = 0
    while j < len(matrix[i]):
        while i < len(matrix):
            resStr = resStr + matrix[i][j]
            i += 1
        resArr.append(resStr)
        resStr = ""
        i = 0
        j += 1
    return resArr

def wordSearch(matrix, string):
#    print colString(matrix)
    for line in matrix:
#        print lineString(line)
        if string in lineString(line) or string in (lineString(line))[::-1]:
            return True
    for item in colString(matrix):
        if string in item or string in (item)[::-1]:
            return True
    return False

matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S'],
  ['O', 'O', 'O', 'O']]

mystring = 'OSBP'
print wordSearch(matrix, mystring)