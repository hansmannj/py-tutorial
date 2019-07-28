# -*- coding: utf-8 -*-

# Die oberste Zeile erlaubt, dass Sonderzeichen im Skript verwendet werden dürfen


# VARIABLEN UND EINFACHE DATENTYPEN
# =================================

var1 = "Ich bin ein String"
print(var1)
print(type(var1))

# Variable von Typ Integer (Ganzzahl)
var2 = 1234
print(var2)
print(type(var2))

# Variable von Typ Float/Double (Fliesskommazahl)
var3 = 3.141
print(var3)
print(type(var3))

# Variable vom Typ Boolean, immer nur True (wahr) oder False (falsch)
boolean = True
print(type(boolean))

# OPERATOREN
# =================================

# Mathematisch
# + - * /
print(5 * 8.587 + 7.11 - 3.1)

# Ganzzahldivision -> Nachkommanstellen werden weggeputzt
print(5 // 3)

# Fliesskommadivision -> Nachkommanstellen bleiben erhalten
print(5 / 3)

# Modulo % -> Rest einer Division
print(7 % 3)

# Textoperatoren
# Concatenation (+ zwischen Strings)
print("text1" + "text2")

# -> Fehler: verschiedene Datentypen mischen
try:
    print("1234" + 1234 + True)
except Exception as e:
    print(e)

# Lösung: Casting (Typumwandlung)
print(str(1234) + "1234")

# COLLECTIONS
# =================================

# Listen
# ---------------
liste = ["b", "a", "c"]

# Sortieren
print(sorted(liste))

# Elemente hinzufügen
liste.append("d")
liste.append(1)
liste.append(True)
liste.append(["x", "y"])  # Verschachtelungen sind möglich

# Ansprechen über Index (beginnt bei 0!!)
print(liste[0])  # -> "b"
print(liste[1])  # -> "a"

# Die Indexnummerierung kann auch am Ende der Liste beginnen, dann mit Minus
print(liste[-1])  # -> gibt das letzte Element in der Liste an

# Sublisten extrahieren über Startindex (inkl.) und Endindex (exkl.), mit Doppelpunkt getrennt
print(liste[2:4])  # -> Gibt den Bereich von inkl. 2 bis exkl. 4 zurück

# Veschachtelte Listen können genauso abgefragt werden. Einfach zweimal die []-Notation anwenden
print(liste[-1][0])

# Elemente über ihren Index aus einer Liste löschen
liste.pop(5)

# Elemente über ihren Wert aus einer Liste löschen
liste.remove("d")

# Sets
# ---------------

# 'Listen' ohne Duplikate
myset = set()
myset.add(4)
myset.add(4)
myset.add(5)
print(myset)

# Listen mit doppelten Werten können in set gecastet werden.
liste = ["a", "a", "a", "b"]
print(set(liste))

# Mit Sets können Mengenoperationen getätigt werden. Siehe Doku.

# Dictionaries
# ---------------

# Key-Value-Paare
mydict = {"key1": "wert1",
          "key2": "wert2",
          "key3": 1234}

# Wert abfragen
print(mydict["key3"])  # -> 1234

# Wert hinzufügen
mydict["key4"] = False

# Alle Keys/Values/Paare auflisten
print(mydict.keys())
print(mydict.values())
print(mydict.items())

# Tupel
# ---------------

# 'Liste' mit uneränderlicher Anzahl Elementen
# Häufig verwendet z.B. für Koordinaten oder Key/Value-Paare
tupel = (600000, 200000)

# KONTROLLSTURKTUREN
# =================================

# Schleifen
# ---------------

# For Schleife: Für eine bekannte Anzahl Elementen
liste = ["b", "a", "c", "d"]
for element in liste:
    # Anweisungsblock. Hier steht, was bei jedem Durchlauf passieren soll
    print(element)

# While Schleife: Läuft, solange eine Bedingung erfüllt ist
# ACHTUNG: Wenn kein Abbruchkriterium definiert, dann endlos!
counter = 0
while counter < 10:
    print(counter)
    counter += 1  # Kurzschreibweise für 'counter = counter + 1'

# Verzweigungen
# ---------------

# Prüfen auf Bedingungen und je nach Ausgang den Programmablauf steuern

var1 = 40

if var1 < 10:
    # Grundbedingung
    print(var1, "ist kleiner als 10")

elif var1 > 50:
    # Falls 'if' nicht zutrifft, dann elif
    # elif kann null bis belibige Male vorkommen
    print(var1, "ist grösser als 50")

else:
    # Wenn bis hierhin keine Bedingung erfüllt, dann else
    # else kann fehlen
    print("weder noch")

# Bedingungen und Schleifen kombinieren
counter = 0
while True:
    if counter > 10:
        break  # Unterbricht die Schleife sofort
    print(counter)
    counter += 1

# BENUTZEREINGABEN
# =================================

# Parameter während Laufzeit abfragen
benutzereingabe = input("Bitte irgendetwas eintippen: ")
print("Du hast {} eingegeben".format(benutzereingabe))
# Benutzereingaben sind immer vom Typ String


# Parameter beim Starten des Skripts von aussen übergeben

# benutzereingabe = sys.argv[1]
# print "Du hast {} dem Skript als Parameter übergeben".format(benutzereingabe)
# ACHTUNG: Dateien mit Endung py müssen mit der Standardanwendung python.exe verknüpft sein


# FEHLERBEHANDLUNG
# =================================
try:
    print(1 / 0)
except Exception as e:
    print("Division durch null ist verboten!")
    print(e)  # Fehlermeldung des Systems
finally:
    print("Ich erscheine immer, ob try erfolgreich war oder nicht")

# DATEIEN LESEN UND SCHREIBEN
# =================================

datei = r"..\sources\participants.txt"
# Das kleine r vor dem Pfad bedeutet,
# dass die Backslashes keine Sonderbedeutung haben
# wie z.B. \n -> Neue Zeile ; \t -> Tabulator

with open(datei, "r") as lesezugriff:
    # Hier bedeutet das kleine r "read"
    inhalt = lesezugriff.readlines()

for zeile in inhalt:
    print(zeile.strip())  # strip => Zeilenumbruch entfernen

neue_datei = "result.txt"
with open(neue_datei, "w") as schreibzugriff:
    # Das kleine w bedeutet "write"
    # Die neue Datei wird automatisch angelegt
    schreibzugriff.write("blabla")

# FUNKTIONEN
# =================================

# Built-in Funktionen, z.B.
liste = [1, 2, 3, 4]
print(sum(liste))
print(len(liste))


# Eigene Funtionen definieren

#   Funktionsname  Parameter
#          |         |
#          v         v
def meine_funktion(zahl):
    # Ich als Funktion kann die Quadratzahl berechnen
    # Meistens kommt noch viel mehr Logik in eine Funktion
    return zahl ** 2


#       ^
#       |
#  Rückgabewert

# Funktion aufrufen
# WICHTIG: Funktionen müssen immer definiert werden, BEVOR sie aufgerufen werden
print(meine_funktion(5))

# ZEIT UND DATUM
# =================================

import time

# Weitere mögliche Module:
# import datetime
# import calendar

# Zeit kann auf 3 verschiedene Arten in Python verarbeitet werden
# 1. menschenlesbar -> z.B. 02.02.2018
# 2. Sekunden seit 01.01.1970 (since the Epoch) -> einfach zu rechen
# 3. Zeittupel aus 9 Elementen (YYYY, MM, DD, .....)

# Beispiele aus dem Skript:
# Current time in seconds since the Epoch
print(time.time())

# Current time as time tuple
print(time.localtime())

# Conversion of a time given in seconds since Epoch to time tuple
print(time.localtime(1517562915))

# Conversion of a text string to time tuple
print(time.strptime("02.02.2018", "%d.%m.%Y"))

# Conversion of a time given as time tuple to seconds since Epoch
print(time.mktime((2016, 4, 29, 0, 0, 0, 4, 120, -1)))

# Conversion of a text string to seconds since Epoch
print(time.mktime(time.strptime("29.04.2016", "%d.%m.%Y")))

# WEBDIENSTE NUTZEN
# =================================

# Module für Webzugriff importieren
import urllib

# import urllib2

# Mein Suchtext
text = "Seftigenstrasse 264"

# URL, die den Service anbietet
url = "https://api3.geo.admin.ch/rest/services/api/SearchServer"

# Die verlangten Parameter -> Siehe Doku des jeweiligen Services
params = {"searchText": text,
          "type": "locations"}

# Parameter in webtaugliches Format bringen
params = urllib.urlencode(params)

try:
    pass
    # Anfrage an Service abfeuern
    # response = urllib2.urlopen(url=url, data=params)

    # Resultate in lesbare Form bringen
    # results = json.load(response)

    # print results
except:
    print("Leider kein Internetzugriff")

# Viel Vergnügen mit Python!
