#You are given a 2D array of characters, and a target stringing. 
#Return whether or not the word target word exists in the matrix. Unlike a standard word search, 
#the word must be either going left-to-right, or top-to-bottom in the matrix.
# ==> I did also right to left and bottom to top

def findCharIndexes(matrix, char):
    coordinates = []
    for line in matrix:
        lastIndex = 0
        for item in line:
            if char == item:
                coordinates.append([matrix.index(line), line.index(char, lastIndex)])
                if lastIndex == 0:
                    lastIndex = line.index(char) + 1  
                else: 
                    lastIndex += 1
                print "This is my last index : " + str(lastIndex)
    return coordinates

def searchTopDown(matrix, string, coordinates):
    for group in coordinates:
        i = group[0]
        j = group[1]
        k = 0
        compstring = ""
#        print "i = " + str(i) + "  j = " + str(j) + "  k = " + str(k)
        while i < len(matrix) and j < len(matrix[i]) and k < len(string):
            if matrix[i][j] == string[k]:
                compstring += string[k] 
            i += 1
            k += 1
#            print compstring
        if compstring == string:
            return True
    return False

def searchDownTop(matrix, string, coordinates):
    for group in coordinates:
        i = group[0]
        j = group[1]
        k = 0
        compstring = ""
        print "i = " + str(i) + "  j = " + str(j) + "  k = " + str(k)
        while i >= 0 and j < len(matrix[i]) and k < len(string):
            if matrix[i][j] == string[k]:
                compstring += string[k] 
            i -= 1
            k += 1
            print compstring
        if compstring == string:
            return True
    return False

def searchLeftRight(matrix, string, coordinates):
    for group in coordinates:
        i = group[0]
        j = group[1]
        k = 0
        compstring = ""
#        print "i = " + str(i) + "  j = " + str(j) + "  k = " + str(k)
        while i < len(matrix) and j < len(matrix[i]) and k < len(string):
            if matrix[i][j] == string[k]:
                compstring += string[k] 
            j += 1   #only difference
            k += 1
#            print compstring
        if compstring == string:
            return True
    return False

def searchRightLeft(matrix, string, coordinates):
    for group in coordinates:
        i = group[0]
        j = group[1]
        k = 0
        compstring = ""
#        print coordinates
#        print "i = " + str(i) + "  j = " + str(j) + "  k = " + str(k)
        while i < len(matrix) and j >= 0 and k < len(string): #second difference for going left
            if matrix[i][j] == string[k]:
                compstring += string[k] 
            j -= 1   #only difference
            k += 1
#            print compstring
        if compstring == string:
            return True
    return False

def wordSearch(matrix, string):
    coordinates = findCharIndexes(matrix, string[0])
    TopDown = searchTopDown(matrix, string, coordinates)
    DownTop = searchDownTop(matrix, string, coordinates)
    LeftRight = searchLeftRight(matrix, string, coordinates)
    RightLeft = searchRightLeft(matrix, string, coordinates)

    return TopDown or LeftRight or RightLeft or DownTop

matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S'],
  ['O', 'O', 'O', 'O']]
#print searchLeftRight(matrix, 'FOAM')

mystring = 'OSOQC'

print wordSearch(matrix, mystring)
#print findCharIndexes(matrix, mystring[0])
#print searchTopDown(matrix, mystring, findCharIndexes(matrix, mystring[0]))

#print findCharIndexes(matrix, 'C')