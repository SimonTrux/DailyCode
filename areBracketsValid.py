#Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. 
#Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 


def isBraces(c):
    return c == '(' or c == ')'

def isCurly(c):
    return c == '{' or c == '}'

def isSquare(c):
    return c == '[' or c == ']'

def isOpening(c):
    return c == '(' or c == '{' or c == '['

def typedArray(bracketType, str):
    arr = []
    for c in str:
        if bracketType(c):
            arr.append(c)
    return arr

def areBracketsValid(str):
    i = 0
    types = [isBraces, isCurly, isSquare]
    for t in types:
        for c in typedArray(t, str):
            if isOpening(c):
                i += 1
            else:
                i -= 1
        if i != 0:
            return False
        i = 0
    return True
            

print areBracketsValid("[]{{{[[]]}}))(())((")
#print bracket().typedArray(isSquare, "{{(]]])})")
