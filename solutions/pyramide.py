height = 4

# rechtsschief
for i in range(height):
    print("X" * (2 * i + 1))

# linksschief
for i in range(height):
    print(" " * ((height - (1 + i)) * 2) + "X" * (2 * i + 1))

# symmetrisch
for i in range(height):
    print(" " * (height - (1 + i)) + "X" * (2 * i + 1))
