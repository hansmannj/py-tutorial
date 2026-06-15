def Koordinaten_eingabe(Koordinate: str) -> float:
    while True:
        try:
            return float(input(f"LV95 {Koordinate} eingeben: "))
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")


# grobe, rechteckige bounding box um die Schweiz
def inCH(ost: float, nord: float) -> bool:
    return 2_480_000 <= ost <= 2_840_000 and 1_070_000 <= nord <= 1_300_000


ost = Koordinaten_eingabe("LV95 Ostwert eingeben: ")
nord = Koordinaten_eingabe("LV95 Nordwert eingeben: ")

# Formatierung mit Apostroph als Tausendertrennzeichen
ost_fmt = f"{ost:,.0f}".replace(",", "'")
nord_fmt = f"{nord:,.0f}".replace(",", "'")

print(f"\nKoordinaten: E {ost_fmt} / N {nord_fmt}")

if inCH(ost, nord):
    print("Der Punkt liegt innerhalb der Schweiz.")
else:
    print("Achtung: Der Punkt liegt ausserhalb der Schweizer Landesgrenzen.")
