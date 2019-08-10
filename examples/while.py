# for zahl in [0, 1, 2, 3, 4, 5 ,6 ,7 ,8, 9]:
for zahl in range(10):

    # Erste Bedingung
    if zahl == 3:
        print("juhu 3")

    # Alternative Bedingung (mehrere elif's moeglich)
    elif zahl == 7:
        print("jess, 7")

    # Wenn gar nichts zutrifft
    else:
        print("irgendeine andere Zahl", zahl)
