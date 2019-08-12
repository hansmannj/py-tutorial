# -*- coding: utf-8 -*-

# Dateipfad für bestehende Datei als Variable
personen = r"C:\Pythonkurs\resources\personen.txt"

# Alle zeilen aus der Datei lesen und in der Variable 'namen' speichern
with open(personen, "r") as r:
    namen = r.readlines()

# leere Liste vorbereiten
nachnamen = []

# durch die Liste 'namen' iterieren
for name in namen:
    # ausführliche Variante
    name_ohne_umbruch = name.strip()  # Zeilenumbruch entfernen
    vorname_nachname = name_ohne_umbruch.split(" ")  # Vor- und Nachnamen beim Leerschlag splitten
    vorname = vorname_nachname[0]  # Vorname steht an Index 0
    nachname = vorname_nachname[1]  # Nachname steht an Index 1

    # schlanke Variante, aber schlechter nachvollziehbar
    # vorname, nachname = name.strip().split(" ")

    # Nachname in die vorbereitete Liste 'nachnamen' schreiben
    nachnamen.append(nachname)

# Liste 'nachnamen' sortiert ausgeben
print(sorted(nachnamen))

# Dateipfad für neue Datei als Variable
nachnamen_abc = r"C:\Pythonkurs\resources\nachnamen_alphabetisch.txt"
with open(nachnamen_abc, "w") as w:  # Schreibzugriff öffnen
    for nachname in sorted(nachnamen):  # sortierter Loop
        w.write(nachname + "\n")  # Name und Umbruch in die Datei schreiben
