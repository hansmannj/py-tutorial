import random

runden = 2
versuche = 3

richtige = 0

for runde in range(runden):
    print(f"Runde {runde + 1}")
    erste_zahl = random.randint(1, 100)
    zweite_zahl = random.randint(1, 100)
    operator = random.choice(["+", "-", "*"])
    rechnung = f"{erste_zahl}{operator}{zweite_zahl}"
    resultat = eval(rechnung)
    print(resultat)

    for versuch in range(versuche):
        if float(input(f"Was ergibt {rechnung}? ")) == resultat:
            print("Korrekt! Weiter geht's")
            richtige += 1
            break
        else:
            if versuch == versuche - 1:
                print(f"Leider falsch. Keine Versuche mehr übrig. Weiter mit der nächsten Aufgabe")
            else:
                print(f"Leider falsch. Noch {versuche - versuch - 1} Versuche übrig")

print(f"Deine Note: {6 * (richtige / runden)}")
