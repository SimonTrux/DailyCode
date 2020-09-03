#VERSION 2 : Ugly but made in 5 min

def areBracketsValid(str):
    i = 0
    j = 0
    k = 0
    for c in str:
        if c == '(':
            i += 1
        elif c == ')':
            i -+ 1
        elif c == '{':
            j += 1
        elif c == '}':
            j -= 1
        elif c == '[':
            k += 1
        elif c == ']':
            k -= 1
    if i + j + k == 0:
        return True
    else:
        return False

print areBracketsValid('{}[]')