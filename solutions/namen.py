# Dateipfad für bestehende Datei als Variable
PERSONEN = r"../resources/personen.txt"

# Alle Zeilen aus der Datei lesen und in der Variable 'namen' speichern.
# Encoding hilft bei Umlauten.
with open(PERSONEN, "r", encoding="utf-8") as r:
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

    # Nach- und Vorname formattiert in die vorbereitete Liste 'nachnamen' schreiben
    nachnamen.append(f"{nachname} {vorname}")

# Liste 'nachnamen' sortiert ausgeben
print(sorted(nachnamen))

# Dateipfad für neue Datei als Variable
nachnamen_abc = r"nachnamen_alphabetisch.txt"
with open(nachnamen_abc, "w", encoding="utf-8") as w:  # Schreibzugriff öffnen
    for nachname in sorted(nachnamen):  # sortierter Loop
        w.write(nachname + "\n")  # Name und Umbruch in die Datei schreiben
