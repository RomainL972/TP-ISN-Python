def divisible(a, b):
    return not a % b

def divisors(num, max=10):
    count = 0
    list = []
    for i in range(1,num+1):
        if(divisible(num,i)):
            list.append(i)
            count += 1
            if(count == max):
                break
    return list

def evenNumbers(min=0, max=100):
    list = []
    for i in range(min, max, 2):
        list.append(i)
    return list

def geometricSuite(u, q, count=10):
    list = []
    for i in range(count):
        list.append(u)
        u *= q
    return list

def toBinary(number):
    base = 2
    result = ""
    if(number < 0):
        number = abs(number)
        result += "-"
    test = 1
    while (test*base) <= number:
        test *= base
    while True:
        digitToAdd = 0
        while test <= number:
            number -= test
            digitToAdd += 1
        result += str(digitToAdd)
        if(test == 1): break
        test /= base
    return result

def arrayToStr(array):
    string = ""
    for i in range(len(array)):
        if(i == len(array)-1 and i != 0): string += " et "
        elif(i != 0): string += ", "
        string += str(array[i])
    return string
