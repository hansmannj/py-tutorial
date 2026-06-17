import random
from collections import Counter


def ziehung():
    # leeres set vorbereiten (sets haben keine Duplikate)
    zahlen = set()
    while len(zahlen) < 6:
        # solange es noch nicht sechs Zahlen im set hat, neue Zahlen generieren
        zahlen.add(random.randint(1, 42))
    return zahlen
    # return set(random.sample(range(1, 43), k=6))


# Eingabe des Tips durch den Nutzer:
# entweder statisch:
# tipp = {1, 2, 3, 4, 5, 6}

# oder:
# dynamisch mit Benutzerabfrage

# leeres Set vorbereiten
tipp = set()

# Schleife solange noch nicht 6 gültige Zahlen getippt wurden
while len(tipp) < 6:
    # Benutzer auffordern, eine Zahl einzugeben.
    # Die Anzahl der bereits im Set enthaltenen Zahlen plus 1 zeigt an,
    # die wievielte Zahl eingegeben werden muss
    zahl = input(f"Bitte {len(tipp) + 1}. Zahl eingeben: ")

    # prüfen, ob eine Zahl eingegeben wurde
    try:
        zahl = int(zahl)
    except Exception:
        print("Nur Ganzzahlen eingeben!")
        # falls keine Zahl, Rest der Schleife überspringen und wieder oben beginnen
        continue

    # prüfen, ob die Zahl bereits getippt wurde
    if zahl in tipp:
        print("Diese Zahl wurde bereits getippt")
        continue

    # prüfen, ob die Zahl im zulässigen Bereich liegt
    if zahl not in range(1, 43):
        print("Nur Zahlen von 1 bis 42")
        continue

    # falls alle Prüfungen bestanden, Zahl zum Set hinzufügen
    tipp.add(zahl)

i = 0  # Counter, der bei jeder Ziehung eins hochzählt.
zaehler_richtige = Counter()
while True:
    i += 1  # kurzschreibweise für i = i + 1
    gewinnzahlen = ziehung()
    richtige = len(gewinnzahlen.intersection(tipp))
    zaehler_richtige[richtige] += 1
    print(
        f"{i:,} {richtige} richtige Zahlen, aktuelle Gewinnzahlen: {gewinnzahlen}, Dein Tip: {tipp}"
    )
    if gewinnzahlen == tipp:
        print("gewonnen")
        print(f"Gesamtstatistik: {zaehler_richtige}")
        break
