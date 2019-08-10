# Berechne mit einer for-Schleife die Summe der Elemente in der Liste [1, 2, 3, 4, 5, 6]

liste = [1, 2, 3, 4, 5, 6]

# Solution 1: for-loop
summe = 0
for zahl in liste:
    summe += zahl
print(summe)

# Solution 2: use function
print(sum(liste))
