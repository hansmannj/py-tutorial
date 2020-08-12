import locale
import time

while True:
    t0 = input("Geburtstag [dd.mm.YYYY]: ")
    try:
        # versuchen, die Benutzereingabe in ein Zeittupel umzuwandeln
        t0 = time.strptime(t0, "%d.%m.%Y")
        break
    except:
        print("Bitte ein gültiges Datum eingeben")

# Aus den einzelnen Komponenten des Zeittupels einen neuen String zusammensetzen
s30 = "{d}.{m}.{Y}".format(
    d=t0.tm_mday,
    m=t0.tm_mon,
    Y=t0.tm_year + 30  # Jahr um 30 erhöhen
)

# Aus dem neuen String wieder ein Zeittuple erstellen
t30 = time.strptime(s30, "%d.%m.%Y")

# Sprache einstellen für die Ausgabe des Wochentags
locale.setlocale(locale.LC_ALL, "deu_deu")

# Ausgabe
print(time.strftime("Du wurdest an einem %A geboren", t0))
# Je nachdem of vergangen oder zukünftig den Platzhalter {} befüllen
print(time.strftime("Dein 30. Geburtstag {} an einem %A".format(
    "ist" if t30 > time.localtime() else "war"
), t30))
