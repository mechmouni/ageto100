from datetime import date

name = input("What is your name?")
age = int(input("What is your age"))

def calcto100(name, age):
    
    year100 = int(date.today().strftime("%Y")) + (100 - age)

    return print ("{} will turn 100 in {}".format(name, year100))
    
calcto100(name, age)