import math


def calc_diameter(r):
    return r * 2


def circumference(r):
    return r * 2 * math.pi


def calc_area(r):
    return r ** 2 * math.pi


while True:
    radius = input("Bitte Radius als Zahl eingeben: ")
    try:
        # Versuchen, Benutzereingabe in eine Flieskommazahl 'float' umzuwandeln...
        radius = float(radius)
        # ...wenn das klappt, while-Schleife abbrechen
        break
    except:
        # ...sonst Fehlermeldung
        print("Bitte eine Zahl eingeben")

# Ausgabe
print("Durchmesser:", calc_diameter(radius))
print("Umfang: " + str(circumference(radius)))
print("Fläche: {}".format(calc_area(radius)))
