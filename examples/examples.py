import random


def ziehung():
    # leeres set vorbereiten
    zahlen = set()

    # solange noch nicht 6 unterschiedliche Zahlen im set sind, neue Zufallszahl generieren
    # und zum set hinzufügen
    while len(zahlen) < 6:
        zahlen.add(random.randint(1, 42))

    # die sechs Zufallszahlen zurückgeben
    return zahlen

    # andere Möglichkeit aus dem Modul random:
    # return set(random.sample(range(1, 43), 6))


# einmal die Funktion 'ziehung()' ausführen, um die Tippabgabe zu simulieren
tipp = ziehung()

# Counter initiieren
counter = 1

# Schleife für eine unbekannte Anzahl an Ziehungen
while True:
    # in jedem Durchlauf neue Gewinnzahlen generieren
    gewinnzahlen = ziehung()
    print(counter, tipp, gewinnzahlen)

    # Tipp mit Gewinnzahlen vergleichen
    if tipp == gewinnzahlen:
        print("Du hast nach {} Ziehungen gewonnen".format(counter))

        # Loop beenden, wenn gewonnen
        break
    else:
        # Sonst counter um 1 erhöhen
        counter += 1
