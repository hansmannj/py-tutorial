import random

# # statisch
# tipp = {1, 2, 3, 4, 5, 6}

# dynamisch mit Benutzerabfrage

# leeres Set vorbereiten
tipp = set()

# Schleife solange noch nicht 6 gültige Zahlen getippt wurden
while len(tipp) < 6:

    # Benutzer auffordern, eine Zahl einzugeben.
    # Die Anzahl der bereits im Set enthaltenen Zahlen plus 1 zeigt an, die wievielte Zahl eingegeben werden muss
    zahl = input(f"Bitte {len(tipp) + 1}. Zahl eingeben: ")

    # prüfen, ob eine Zahl eingegeben wurde
    try:
        zahl = int(zahl)
    except:
        print("Nur Ganzzahlen eingeben!")
        # falls keine Zahl, Rest der Schleife überspringen und wieder oben beginnen
        continue

    # prüfen, ob die Zahl bereits getippt wurde
    if zahl in tipp:
        print("Diese Zahl wurde bereits getippt")
        continue

    # prüfen, ob die Zahl im zulässigen Bereich liegt
    elif zahl not in range(1, 43):  # elif zahl < 1 or zahl > 42:
        print("Nur Zahlen von 1 bis 42")
        continue

    # falls alle Prüfungen bestanden, Zahl zum Set hinzufügen
    tipp.add(zahl)


def ziehung():
    # leeres set vorbereiten (sets haben keine duplikate)
    zahlen = set()
    while len(zahlen) < 6:
        # solange es noch nicht sechs zahlen im set hat, neue zahlen generieren
        zahlen.add(random.randint(1, 42))
    return zahlen
    # return set(random.sample(range(1, 43), k=6))


i = 0  # Counter, der bei jeder Ziehung eins hochzählt.
while True:
    i += 1  # kurzschreibweise für i = i + 1
    gewinnzahlen = ziehung()
    print(i, gewinnzahlen)
    if gewinnzahlen == tipp:
        print("gewonnen")
        break
