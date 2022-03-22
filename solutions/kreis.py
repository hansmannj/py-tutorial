import math

# Variante mit Parameter
# Wird beim Starten des Programms von aussen mitgegeben
# user_input = sys.argv[1]

# Variante mit Benutzereingabe
# Wird zur Laufzeit des Programms vom Benutzer verlangt
while True:
    radius = input("Bitte den Radius eingeben: ")
    try:
        # Benutzereingaben sind immer Strings
        # Deshalb casting nach Fliesskommazahl
        radius = float(radius)
        break
    except Exception as e:
        print(e)

# Berechnungen
diameter = radius * 2
circumference = radius * 2 * math.pi
area = round(radius**2 * math.pi, 3)

# Ausgabe (vier verschiedene Möglichkeiten für print)
print(f"Radius: {radius}")
print("Durchmesser:", diameter)
print("Umfang: " + str(circumference))
# Den Flächeninhalt unten auf 2 Nachkommastellen gerundet, damit es lesbarer ist.
# (Könnte man natürlich für den Umfang oben auch machen.)
print("Fläche: {}".format(round(area, 2)))
