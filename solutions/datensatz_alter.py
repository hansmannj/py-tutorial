import time

while True:
    eingabe = input("Aufnahmedatum des Datensatzes (TT.MM.JJJJ): ")
    try:
        aufnahme = time.strptime(eingabe, "%d.%m.%Y")
        break
    except ValueError:
        print("Ungültiges Format. Bitte TT.MM.JJJJ eingeben.")

sekunden_aufnahme = time.mktime(aufnahme)
alter_tage = (time.time() - sekunden_aufnahme) / 86400

print(f"\nDatumstand: {time.strftime('%A, %d. %B %Y', aufnahme)}")
print(f"Datensatz ist {alter_tage:.0f} Tage alt.")

if alter_tage > 365:
    print("Achtung: Datensatz ist älter als 1 Jahr - bitte auf Aktualität prüfen.")
