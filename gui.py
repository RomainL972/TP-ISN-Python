from appJar import gui
import utils

app = gui("Mon TP Python")

def showSubWindow(button):
    app.showSubWindow(button)

def exo1_exec():
    try:
        num1 = int(app.getEntry("one_num1"))
        num2 = int(app.getEntry("one_num2"))
        if(utils.divisible(num1, num2)):
            app.setLabel("one_result", str(num1)+" est divisible par "+str(num2))
        else:
            app.setLabel("one_result", str(num1)+" n'est pas divisible par "+str(num2))
    except TypeError:
        app.setLabel("one_result", "Un champ est vide!")

def exo2_exec():
    try:
        num = int(app.getEntry("two_num"))
        result = utils.divisors(num)
        resultStr = utils.arrayToStr(result)
        app.setLabel("two_result", resultStr)
    except TypeError:
        app.setLabel("two_result", "Un champ est vide!")

def exo3_exec():
    result = utils.evenNumbers()
    resultStr = utils.arrayToStr(result)
    app.setLabel("three_result", resultStr)

def exo4_exec():
    try:
        u = int(app.getEntry("four_num1"))
        q = int(app.getEntry("four_num2"))
        result = utils.geometricSuite(u, q)
        resultStr = utils.arrayToStr(result)
        app.setLabel("four_result", resultStr)
    except TypeError:
        app.setLabel("four_result", "Un champ est vide!")

def exo5_exec():
    try:
        num = int(app.getEntry("five_num"))
        result = utils.toBinary(num)
        app.setLabel("five_result", str(num)+" en binaire fait "+result)
    except TypeError:
        app.setLabel("five_result", "Un champ est vide!")

#Main Windows
app.addLabel("title", "Quel exercice voulez-vous tester?")
app.addButton("Exercice 1: Divisibilité", showSubWindow)
app.addButton("Exercice 2: Diviseurs", showSubWindow)
app.addButton("Exercice 3: Nombres pairs", showSubWindow)
app.addButton("Exercice 4: Suite géométrique", showSubWindow)
app.addButton("Exercice 5: Décimal à Binaire", showSubWindow)

#Exercice 1
app.startSubWindow("Exercice 1: Divisibilité", modal=True)
app.addLabel("one_num1_label", "Nombre 1 :")
app.addNumericEntry("one_num1")
app.addLabel("one_num2_label", "Nombre 2 :")
app.addNumericEntry("one_num2")
app.addNamedButton("Lancer", "one_run", exo1_exec)
app.addEmptyLabel("one_result")
app.stopSubWindow()

#Exercice 2
app.startSubWindow("Exercice 2: Diviseurs", modal=True)
app.addLabel("two_num_label", "Nombre :")
app.addNumericEntry("two_num")
app.addNamedButton("Lancer", "two_run", exo2_exec)
app.addEmptyLabel("two_result")
app.stopSubWindow()

#Exercice 3
app.startSubWindow("Exercice 3: Nombres pairs", modal=True)
app.addNamedButton("Lancer","three_run", exo3_exec)
app.addEmptyLabel("three_result")
app.stopSubWindow()

#Exercice 4
app.startSubWindow("Exercice 4: Suite géométrique", modal=True)
app.addLabel("four_num1_label", "u(0) :")
app.addNumericEntry("four_num1")
app.addLabel("four_num2_label", "Raison :")
app.addNumericEntry("four_num2")
app.addNamedButton("Lancer", "four_run", exo4_exec)
app.addEmptyLabel("four_result")
app.stopSubWindow()

#Exercice 5
app.startSubWindow("Exercice 5: Décimal à Binaire", modal=True)
app.addLabel("five_num_label", "Nombre :")
app.addNumericEntry("five_num")
app.addNamedButton("Lancer", "five_run", exo5_exec)
app.addEmptyLabel("five_result")
app.stopSubWindow()

app.go()
