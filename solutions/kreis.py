# -*- coding: utf-8 -*-

import math

# Benutzereingabe
user_input = input("Bitte eine Zahl eingeben: ")

# Benutzereingaben sind immer Strings
# Deshalb casting nach Fliesskommazahl
radius = float(user_input)

# Berechnungen
diameter = radius * 2
circumference = radius * 2 * math.pi
area = radius ** 2 * math.pi

# Ausgabe
print("Durchmesser: ", diameter)
print("Umfang: ", circumference)
print("Flàche: ", area)
