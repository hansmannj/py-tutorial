import random


def ziehung():
    zahlen = set()
    while len(zahlen) < 6:
        zahlen.add(random.randint(1, 42))
    return zahlen


gewinnzahlen = ziehung()
print(sorted(gewinnzahlen))

versuch = 1
while gewinnzahlen != ziehung():
    versuch += 1
print(versuch)
