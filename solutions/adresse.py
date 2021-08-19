import json
import webbrowser

import requests

adresse = input("Wo wohnst du? ")

# Service und Parameter definieren
service = "https://api3.geo.admin.ch/rest/services/api/SearchServer"

params = {
    "searchText": adresse,
    "type": "locations",
    "limit": 1
}

# Service aufrufen, verify=False innerhalb Bundesnetz
response = requests.get(url=service, params=params, verify=False)

# Antwortcode des Servers (200=ok)
# print(response)

# Antwort des Servers (im Format 'json') in Python dictionary umwandeln
result = response.json()

# Python dictionary strukturiert anzeigen
# print(json.dumps(result, indent=2))

# Verschachtelte Elemente aus dem dictionary auslesen
x = result["results"][0]["attrs"]["x"]
y = result["results"][0]["attrs"]["y"]

# Resultat ausgeben
# print(f"Die Adresse '{adresse}' hat die Koordinaten {round(y)}/{round(x)}")

# Webbrowser öffnen und Pin anzeigen
webbrowser.open_new_tab(fr"https://map.geo.admin.ch/?X={x}&Y={y}&zoom=12&crosshair=marker")
