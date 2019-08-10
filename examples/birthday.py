import time

user_input = input("Wie lautet dein Geburtsdatum? ")

try:
    t = time.strptime(user_input, "%d.%m.%Y")
    print("Du wurdest an einem {} geboren".format(time.strftime("%A", t)))

    t30 = time.strptime(user_input[:-4] + str(int(user_input[-4:]) + 30), "%d.%m.%Y")

    print("Dein 30. Geburtstag wird an einem {} sein".format(time.strftime("%A", t30)))
except Exception:
    print("Bitte das Datum im Format 'DD.MM.YYYY' eingeben")
