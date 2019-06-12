from datetime import date

name = input("What is your name?")
age = input("What is your age")

def calcto100(name, age):
    100-age
    year100 = date.today().strftime("%Y") + (100 - age)

    return print ("{} will turn 100 in {}".format(name, year100))
    
