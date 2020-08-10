import string

# Absteigende (Intervall -1) Liste mit den Ziffern von 8 bis 1 (ohne 0)
nrs = range(8, 0, -1)

# Erste 8 Buchstaben des Alphabets
abc = string.ascii_lowercase[:8]

# Äussere Schleife ist für die Zeilen. In einer Zeile ist immer dieselbe Nummer
for y in nrs:

    # Leere Liste, die wir pro Zeile vorbereiten
    row = []

    # Innere Schleife ist für die Buchstaben. In jeder Spalte steht ein anderer Buchstabe
    for x in abc:
        # Mit {} und .format können wir unseren String zusammenbasteln
        cell = "{}{}".format(x, y)

        # die Zelle füllen wir in die vorbereitete Liste für die Zeile
        row.append(cell)

    # Pro Zeile stellen wir die Liste dar.
    # "trennzeichen".join(liste) stellt eine Liste schön dar
    print(" ".join(row))
