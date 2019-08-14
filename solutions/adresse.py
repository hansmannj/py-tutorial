import json

import requests

# Service und Parameter definieren
url = "https://api3.geo.admin.ch/rest/services/api/SearchServer"
text = "Denzlerstrasse 8 Bern"
params = {"searchText": text,
          "type": "locations",
          "limit": 1}

# Service aufrufen
response = requests.get(url=url, params=params, verify=False)

# Antwortcode des Servers
print(response)

# Antwort des Servers (im Format 'json') in Python dictionary umwandeln
result_dict = response.json()

# Python dictionary strukturiert anzeigen
print(json.dumps(result_dict, indent=2))

# Verschachtelte Elemente aus dem dictionary auslesen
x = result_dict["results"][0]["attrs"]["x"]
y = result_dict["results"][0]["attrs"]["y"]

print("Die Adresse '{adr}' hat die Koordinaten {e}/{n}".format(adr=text, e=round(y), n=round(x)))
