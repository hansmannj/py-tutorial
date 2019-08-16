height = 4

# rechtsschief
for i in range(height):
    print("X" * (i + 1))

# linksschief
for i in range(height):
    print(" " * (height - (i + 1)) + "X" * (i + 1))

# symmetrisch
for i in range(height):
    print(" " * (height - (i + 1)) + "X" * (2 * i + 1))
