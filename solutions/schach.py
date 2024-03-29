# Basisfunktionalität erweitern, indem ein Modul aktiviert (=importiert) wird
import string

# Absteigende (Intervall -1) Liste mit den Ziffern von 8 bis 1 (ohne 0)
numbers = range(8, 0, -1)

# Erste 8 Buchstaben des Alphabets
abc = string.ascii_lowercase[:8]

# Äussere Schleife ist für die Zeilen. In einer Zeile ist immer dieselbe Nummer
for n in numbers:

    # Innere Schleife ist für die Buchstaben. In jeder Spalte steht ein anderer Buchstabe
    for letter in abc:
        # Ein Feld auf dem Schachbrett setzt sich zusammen aus Buchstabe+Zahl (Achtung: casting)
        cell = letter + str(n)

        # Print fügt normalerweise automatisch einen Zeilenumbruch ein. Dies wollen wir aber
        # übersteuern mit einem Leerschlag.
        print(cell, end=" ")

    # Sobald im äusseren Loop eine neue Ziffer kommt, wollen wir einen Leerschlag erzwingen:
    print("")
