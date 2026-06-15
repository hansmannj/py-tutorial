datei = "../resources/messpunkte.csv"

punkte = []

with open(datei) as f:
    zeilen = f.readlines()

for zeile in zeilen[1:]:  # Kopfzeile überspringen
    teile = zeile.strip().split(",")
    punkte.append(
        {
            "name": teile[0],
            "ost": float(teile[1]),
            "nord": float(teile[2]),
            "hoehe": float(teile[3]),
        }
    )

hoehen = [p["hoehe"] for p in punkte]
min_hoehe = min(hoehen)

with open("hoehendifferenzen.csv", "w") as f:
    f.write("name,hoehe,differenz\n")
    for p in punkte:
        differenz = round(p["hoehe"] - min_hoehe, 1)
        f.write(f"{p['name']},{p['hoehe']},{differenz}\n")
        print(f"{p['name']}: {p['hoehe']} m.ü.M., Differenz zum tiefsten: {differenz} m")
