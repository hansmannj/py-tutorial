import math


def calc_diameter(r):
    return r * 2


def circumference(r):
    return r * 2 * math.pi


def calc_area(r):
    return r**2 * math.pi


def check_radius_input():
    """Fetches radius from user input and checks, if it is a valid float.

    Returns:
        A float value of the radius from the user input.
    """
    while True:
        r = input("Bitte Radius als Zahl eingeben: ")
        try:
            # Versuchen, Benutzereingabe in eine Flieskommazahl 'float' umzuwandeln...
            r = float(r)
            # ...wenn das klappt, while-Schleife abbrechen
            if r < 0:
                raise Exception("Radius darf nicht negativ sein")
            break
        except ValueError:
            # ...sonst den User um erneute Eingabe bitten
            print("Bitte eine Zahl eingeben")
        except Exception as e:
            print("Bitte eine positive Zahl eingeben")
    return r


radius = check_radius_input()

# Ausgabe
print("Durchmesser:", calc_diameter(radius))
print("Umfang: " + str(circumference(radius)))
print(f"Fläche: {calc_area(radius)}")
