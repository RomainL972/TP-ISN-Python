import utils

print("Bienvenue dans le TP de Python de Romain")
print("Voici la liste des exercices")
print("1: Divisibilité de deux nombres")
print("2: 10 premiers diviseurs d'un nombre")
print("3: Liste des nombres pairs inferieurs à 100")
print("4: 10 premiers termes d'une suite géométrique")
print("5: Convertisseur de décimal à binaire")
exo = 0
while exo < 1 or exo > 5:
    exo = int(input("Choisissez un exercice (1-5) : "))

if(exo == 1):
    num1 = int(input("Nombre 1 : "))
    num2 = int(input("Nombre 2 : "))
    if(utils.divisible(num1, num2)):
        print(num1, "est divisible par", num2)
    else:
        print(num1, "n'est pas divisible par", num2)
elif(exo == 2):
    num = int(input("Nombre : "))
    result = utils.arrayToStr(utils.divisors(num))
    print("Les diviseurs de", num, "sont", result)
elif(exo == 3):
    result = utils.arrayToStr(utils.evenNumbers())
    print("Les nombres pairs inférieurs à 100 sont", result)
elif(exo == 4):
    u = int(input("u(0) : "))
    q = int(input("q : "))
    result = utils.arrayToStr(utils.geometricSuite(u, q))
    print("Les dix premiers termes de cette suite sont", result)
else:
    num = int(input("Nombre : "))
    print(num, "en binaire fait", utils.toBinary(num))
