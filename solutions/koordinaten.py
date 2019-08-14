import math

import requests

# Koordinaten AZB in wgs84
azb_lon = 7.452
azb_lat = 46.928

# Koordinaten L+T in LV95
lt_e = 2600050
lt_n = 1198760

# Service und Parameter
service = "http://geodesy.geo.admin.ch/reframe/wgs84tolv95"
parameters = {"easting": azb_lon,
              "northing": azb_lat,
              "format": "json"}

# Abfrage
response = requests.get(url=service, params=parameters, verify=False)

# Resultat in Python Dictionary umwandeln
result = response.json()

# Elemente aus Dictionary lesen und in floats umwandeln
azb_e = float(result["easting"])
azb_n = float(result["northing"])

# Berechnung der Distanz mit Pythagoras
distance = math.sqrt((lt_e - azb_e) ** 2 + (lt_n - azb_n) ** 2)

# Alternative: Berechnung der Distanz mit math.hypot
# distance = math.hypot(lt_e - azb_e, lt_n - azb_n)

# Gerundete Ausgabe
print(round(distance, -1))
