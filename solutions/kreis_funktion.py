import math


def check_input(value_to_check):
    try:
        # falls 'value_to_check' in einen float gecastet werden kann, ist dieser float gleich der Rückgabewert
        return float(value_to_check)
    except Exception as e:
        print(e)
        return None


while True:
    # Der User Input wird direkt als Argument 'value_to_check' an die Funktion 'check_input' übergeben
    # 'check_input' liefert entweder den Radius als float oder 'None' zurück
    radius = check_input(input("Bitte Radius als Zahl eingeben: "))
    if radius:  # kurz für: 'radius' hat irgendeinen Wert, aber nicht 'None' oder 'False'
        break  # Schleife beenden, wenn 'radius' einen gültigen Wert hat


def calc_diameter(r):
    return r * 2


def circumference(r):
    return r * 2 * math.pi


def calc_area(r):
    return r ** 2 * math.pi


# Ausgabe
print("Durchmesser:", calc_diameter(radius))
print("Umfang: " + str(circumference(radius)))
print("Fläche: {}".format(calc_area(radius)))
