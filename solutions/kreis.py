import math

# Variante mit Parameter
# Wird beim Starten des Programms von aussen mitgegeben
# user_input = sys.argv[1]

# Variante mit Benutzereingabe
# Wird zur Laufzeit des Programms vom Benutzer verlangt
while True:
    user_input = input("Bitte den Radius eingeben: ")
    try:
        # Benutzereingaben sind immer Strings
        # Deshalb casting nach Fliesskommazahl
        radius = float(user_input)
        break
    except Exception as e:
        print(e)

# Berechnungen
diameter = radius * 2
circumference = radius * 2 * math.pi
area = round(radius ** 2 * math.pi, 3)

# Ausgabe
print("Durchmesser:", diameter)
print("Umfang: " + str(circumference))
print("Flàche: {}".format(area))
