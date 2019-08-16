namen = ["Kevin", "Jonas", "Renas", "Lionel", "Gian Luca", "Salomè", "Nils", "Elias"]
zahlen = [1, 2, 3, 4, 5]

# Listen schön darstellen
# Der String vor dem '.join' kann beliebnige Zeichen enthalten.
# Diese werden dann als Trennzeichen zwischen die einzelnen Listenelemente eingesetzt
print(" * ".join(namen))

# falls Elemente in der Liste vorkommen, die keine Strings sind, müssen diese zuerst umgewandelt werden
# diese Umwandlung für die gesamte Liste funktioniert mit 'map'
print(" | ".join(map(str, zahlen)))

# Listen 'in place' verändern
# Dies heisst 'list comprehension'
quadratzahlen = [z ** 2 for z in zahlen]
print(quadratzahlen)

namen_gross = [n.upper() for n in namen]
print(namen_gross)

# Auch die oben genannte 'map'-funktion könnte mit einer list comprehension gelöst werden
zahlen_als_strings = [str(z) for z in zahlen]
print(" | ".join(zahlen_als_strings))