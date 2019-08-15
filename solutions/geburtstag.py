import time

while True:
    try:
        # Benutzereingabe in Zeit-Tupel umwandeln
        t_tupel = time.strptime(input("Wie lautet dein Genurtstag? "), "%d.%m.%Y")
        break
    except Exception as e:
        print(e)

# Zeittupel nach String konvertieren, aber beim Pattern nur '%A' angeben. Dann wird nur der Wochentag angezeigt
t_string = time.strftime("%A", t_tupel)
print("Du wurdest an einem {} geboren".format(t_string))

# Einzelne Elemente aus dem Zeittupel lesen und in einen String schreiben. Dabei das Jahr um 30 erhöhen
t30_string = "{}.{}.{}".format(t_tupel.tm_mday, t_tupel.tm_mon, t_tupel.tm_year + 30)

# Neuen String in Tupel umwandeln
t30_tupel = time.strptime(t30_string, "%d.%m.%Y")

# Ausgabe des Wochentags wie oben ('%A')
# 'war' wenn der 30. Genurtstag zurückliegt sonst 'ist'
print("Dein 30. Geburtstag {} an einem {}".format("war" if t30_tupel < time.localtime() else "ist",
                                                  time.strftime("%A", t30_tupel)))
