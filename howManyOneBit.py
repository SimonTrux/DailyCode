#date : 24 fev 2021

# Problem : Given an integer, find the number of 1 bits it has.

def convertDecToBin(num, arr):
    if num >= 1:
        convertDecToBin(num / 2, arr)
        arr.append(num % 2)
        return(arr)

def one_bits(num):

    arr = convertDecToBin(num, [])

    i = 0
    for item in arr:
        if item == 1:
            i = i + 1
    return i

x = 191

print ("Number is : " + str(x))
print ("Binary version = 0b " + ''.join(map(str, convertDecToBin(x, []))))
print("Numbers of one bits : " + str(one_bits(x)))