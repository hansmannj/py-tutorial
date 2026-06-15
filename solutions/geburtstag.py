import locale
import time

while True:
    t0 = input("Geburtstag [dd.mm.YYYY]: ")
    try:
        # versuchen, die Benutzereingabe in ein Zeittupel umzuwandeln
        t0 = time.strptime(t0, "%d.%m.%Y")
        break
    except ValueError:
        print("Bitte ein gültiges Datum eingeben")

# Aus den einzelnen Komponenten des Zeittupels einen neuen String zusammensetzen,
# mit Jahr = Geburtsjahr + 30
s30 = f"{t0.tm_mday}.{t0.tm_mon}.{t0.tm_year + 30}"

# Aus dem neuen String wieder ein Zeittuple erstellen
t30 = time.strptime(s30, "%d.%m.%Y")

# Sprache einstellen für die Ausgabe des Wochentags
# locale.setlocale(locale.LC_ALL, "deu_deu")

# Ausgabe
print(time.strftime("Du wurdest an einem %A geboren", t0))
# Je nachdem of vergangen oder zukünftig den Platzhalter {} befüllen
print(
    time.strftime(
        f"Dein 30. Geburtstag {'ist' if t30 > time.localtime() else 'war'} an einem %A",
        t30))
