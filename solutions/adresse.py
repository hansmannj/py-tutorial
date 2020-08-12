import json
import webbrowser

import requests

# Service und Parameter definieren
service = "https://api3.geo.admin.ch/rest/services/api/SearchServer"
search = "Eigerstrasse 71 Bern"
params = {"searchText": search,
          "type": "locations",
          "limit": 1}

# Service aufrufen, verify=False innerhalb Bundesnetz
response = requests.get(url=service, params=params, verify=False)

# Antwortcode des Servers (200=ok)
print(response)

# Antwort des Servers (im Format 'json') in Python dictionary umwandeln
result = response.json()

# Python dictionary strukturiert anzeigen
print(json.dumps(result, indent=2))

# Verschachtelte Elemente aus dem dictionary auslesen
x = result["results"][0]["attrs"]["x"]
y = result["results"][0]["attrs"]["y"]

# Resultat ausgeben
print("Die Adresse '{adr}' hat die Koordinaten {e}/{n}".format(adr=search, e=round(y), n=round(x)))

# Webbrowser öffnen und Pin anzeigen
webbrowser.open_new_tab(r"https://map.geo.admin.ch/?X={x}&Y={y}&zoom=12&crosshair=marker".format(x=x, y=y))
