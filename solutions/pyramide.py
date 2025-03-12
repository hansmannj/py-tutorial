height = 75

# rechtsschief
for i in range(height):
    xxxx = "X" * (i + 1)
    print(xxxx)

# linksschief
for i in range(height):
    leer = " " * (height - (i + 1))
    xxxx = "X" * (i + 1)
    print(leer + xxxx)

# symmetrisch
for i in range(height):
    leer = " " * (height - (i + 1))
    xxxx = "X" * (2 * i + 1)
    print(leer + xxxx)
