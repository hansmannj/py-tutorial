HEIGHT = 20

# rechtsschief
for i in range(HEIGHT):
    xxxx = "X" * (i + 1)
    print(xxxx)

# linksschief
for i in range(HEIGHT):
    leer = " " * (HEIGHT - (i + 1))
    xxxx = "X" * (i + 1)
    print(leer + xxxx)

# symmetrisch
for i in range(HEIGHT):
    leer = " " * (HEIGHT - (i + 1))
    xxxx = "X" * (2 * i + 1)
    print(leer + xxxx)
