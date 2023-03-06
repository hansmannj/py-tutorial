import random

RUNDEN = 2
VERSUCHE = 3
RICHTIGE = 0

for runde in range(RUNDEN):
    print(f"Runde {runde + 1}")
    erste_zahl = random.randint(1, 100)
    zweite_zahl = random.randint(1, 100)
    operator = random.choice(["+", "-", "*"])
    rechnung = f"{erste_zahl}{operator}{zweite_zahl}"
    resultat = eval(rechnung)

    for versuch in range(VERSUCHE):
        if float(input(f"Was ergibt {rechnung}? ")) == resultat:
            print("Korrekt! Weiter geht's")
            RICHTIGE += 1
            break
        else:
            if versuch == VERSUCHE - 1:
                print(f"Leider falsch. Keine VERSUCHE mehr übrig. Weiter mit der nächsten Aufgabe")
            else:
                print(f"Leider falsch. Noch {VERSUCHE - versuch - 1} VERSUCHE übrig")

print(f"Deine Note: {6 * (RICHTIGE / RUNDEN)}")
