muster = 2
limit = 100

liste = range(limit)

for zahl in liste:
    text = str(zahl)
    if str(muster) in text:
        print(zahl, "beinhaltet das gesuchte Zeichen", muster)
