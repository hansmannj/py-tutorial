def primzahl(zahl):
    if zahl < 2:
        return False
    else:
        for i in range(2, zahl):
            if zahl % i == 0:
                return False
        return True


for i in range(1000):
    if primzahl(i):
        print(i)
