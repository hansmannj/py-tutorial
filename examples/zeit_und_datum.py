import time

# Aktuelle Zeit in Sekunden seit 'the Epoch'
print(time.time())
time.sleep(1)
print(time.time())

# # Aktuelle Zeit als Tupel, und einzelne Elemente daraus
print(time.localtime())
print(time.localtime().tm_mon)  # Monat
print(time.localtime().tm_mday)  # Tag

# Umwandlung von Sekunden seit 'the Epoch' in Zeit-Tupel
print(time.localtime(10000000000))

# Umwandlung von Text, das einem bestimmten Muster entspricht, in Zeit-Tupel
print(time.strptime("02.05.2016", "%d.%m.%Y"))

# Umwandlung eines Zeit-Tupels in Sekunden
print(time.mktime((2016, 4, 29, 0, 0, 0, 4, 120, -1)))

# Umwandlung von Text in Sekunden seit 'the Epoch'
print(time.mktime(time.strptime("29.04.2016", "%d.%m.%Y")))
