def divisible(a: int, b: int) -> bool:
    """Renvoie si a est divisible par b"""
    return not a % b

def divisors(num: int, max: int = 10) -> list:
    """Renvoie les max premiers diviseurs de num"""
    count = 0
    list = []
    for i in range(1,num+1):
        if(divisible(num,i)):
            list.append(i)
            count += 1
            if(count == max):
                break
    return list

def evenNumbers(min: int=0, max: int=100) -> list:
    """Renvoie les nombre pairs >= min et < max"""
    list = []
    for i in range(min, max, 2):
        list.append(i)
    return list

def geometricSuite(u: float, q: float, count: int=10) -> list:
    """Renvoie les count premiers termes de la suite géométrique u(n)=u*q^n"""
    list = []
    for i in range(count):
        list.append(u)
        u *= q
    return list

def toBinary(number: int) -> str:
    """Renvoie la représentation binaire de number sous forme de string"""
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

def arrayToStr(array) -> str:
    """Une fonction toString pour listes"""
    string = ""
    for i in range(len(array)):
        if(i == len(array)-1 and i != 0): string += " et "
        elif(i != 0): string += ", "
        string += str(array[i])
    return string
