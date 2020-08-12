import math

import requests

service = "https://geodesy.geo.admin.ch/reframe/wgs84tolv03"

# E / N
lt_wgs84 = (7.452, 46.928)
azb_lv03 = (600050, 198760)

parameter = {
    "easting": lt_wgs84[0],
    "northing": lt_wgs84[1]
}

response = requests.get(url=service, params=parameter, verify=False)
result = response.json()
lt_lv03 = result["coordinates"]

distance = math.sqrt((azb_lv03[0] - lt_lv03[0]) ** 2 + (azb_lv03[1] - lt_lv03[1]) ** 2)

print(round(distance, -1))
