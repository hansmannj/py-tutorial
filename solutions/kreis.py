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
        if radius < 0:
            raise Exception("Radius darf nicht negativ sein!")
        break

    except ValueError:
        print("Bitte einen Integer oder Float eingeben!")
    except Exception as err:
        print(err)

# Berechnungen
diameter = radius * 2
circumference = radius * 2 * math.pi
area = round(radius**2 * math.pi, 3)

# Ausgabe
print(f"Radius: {radius}")
print(f"Durchmesser: {diameter}")
print(f"Umfang: {str(circumference)}")
# Den Flächeninhalt unten auf 2 Nachkommastellen gerundet, damit es lesbarer ist.
# Auf zwei Möglichkeiten
# (Könnte man natürlich für den Umfang oben auch machen.)
print(f"Fläche: {round(area, 2)}")
print(f"Fläche: {area:.2f}")
