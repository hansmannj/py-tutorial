# Gegeben ist die Liste range(100)
# Welche Zahlen sind ohne Rest durch 9 und durch 6 aber nicht durch 8 teilbar?

# Idee: Wenn die Division von Zahl a durch eine Ganzzahl b dasselbe Resultat ergibt wie die Division durch
# dieselbe Zahl B als Dezimalzahl, dann ist Zahl A ohne Rest durch Zahl B teilbar

liste = range(100)
resultat = []

for zahl in liste:
    if zahl / 9 == zahl / 9.0:  # ohne Rest durch 9 teilbar
        if zahl / 6 == zahl / 6.0:  # ohne Rest durch 6 teilbar
            if not zahl / 8 == zahl / 8.0:  # NICHT ohne Rest durch 8 teilbar
                resultat.append(str(zahl))

print("Die Zahlen {} erfuellen alle Bedingungen".format(", ".join(resultat)))
