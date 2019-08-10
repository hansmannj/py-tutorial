import json
import math

import urllib2

# Aus dem Bundesnetz ist manchmal ein Proxy notwendig
# proxy_support = urllib2.ProxyHandler({"http": "proxy-bvcol.admin.ch:8080"})
# opener = urllib2.build_opener(proxy_support)
# urllib2.install_opener(opener)

E = 7.452
N = 46.928

url = "http://geodesy.geo.admin.ch/reframe/wgs84tolv03"

url += "?easting=" + str(E)
url += "&northing=" + str(N)
url += "&format=json"

response = urllib2.urlopen(url=url)
result = json.load(response)

X = float(result["easting"])
Y = float(result["northing"])

print("X", X)
print("Y", Y)

ltX = 600050
ltY = 198760

distance = math.sqrt((abs(ltX - X)) ** 2 + (abs(ltY - Y)) ** 2)

print(distance)
