woche = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']

print(woche)

to_remove_list = ["Dienstag", "Mittwoch"]

for wochentag in to_remove_list:
    woche.remove(wochentag)

print(woche)
