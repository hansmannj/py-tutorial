# Kreisberechnungen mit Benutzereingabe
import math

# Benutzereingabe
user_input = input("Bitte eine Zahl eingeben: ")


# Funktionen definieren
def check_input(value_to_check):
    try:
        radius = float(value_to_check)
    except Exception:
        radius = 0
    return radius


def calc_diameter(radius):
    return radius * 2


def calc_circumference(radius):
    return radius * 2 * math.pi


def calc_area(radius):
    return radius ** 2 * math.pi


# Funktionen aufrufen
print("Durchmesser: ", calc_diameter(check_input(user_input)))
print("Umfang: ", calc_circumference(check_input(user_input)))
print("Flaeche: ", calc_area(check_input(user_input)))
