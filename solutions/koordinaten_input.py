def eingabe_zahl(aufforderung: str) -> float:
    while True:
        try:
            return float(input(aufforderung))
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")


def in_der_schweiz(ost: float, nord: float) -> bool:
    return 2_480_000 <= ost <= 2_840_000 and 1_070_000 <= nord <= 1_300_000


ost = eingabe_zahl("LV95 Ostwert eingeben: ")
nord = eingabe_zahl("LV95 Nordwert eingeben: ")

# Formatierung mit Apostroph als Tausendertrennzeichen
ost_fmt = f"{ost:,.0f}".replace(",", "'")
nord_fmt = f"{nord:,.0f}".replace(",", "'")

print(f"\nKoordinaten: E {ost_fmt} / N {nord_fmt}")

if in_der_schweiz(ost, nord):
    print("Der Punkt liegt innerhalb der Schweiz.")
else:
    print("Achtung: Der Punkt liegt ausserhalb der Schweizer Landesgrenzen.")
