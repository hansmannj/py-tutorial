def primzahl(zahl):
    if zahl < 2:
        return False
    else:
        for i in range(2, zahl):
            if zahl % i == 0:
                return False
    return True


for z in range(100):
    if primzahl(z):  # Kurzschreibweise für 'primzahl(z) == True'
        print("{} ist eine Primzahl".format(z))
