liste = [1, 2, 3, 4, 5, 6]
# oder liste = range(1, 7)

# Solution 1: for-loop
summe = 0
for zahl in liste:
    summe = summe + zahl
    # Kurzschreibweise wäre: summe += zahl
print(summe)




# Solution 2 etwas gemogelt ;-)
# wir benutzen eine built-in function:
print(sum(liste))
