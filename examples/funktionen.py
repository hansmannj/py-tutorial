# Definition
def subtraction(zahl1, zahl2):
    return zahl1 - zahl2


# Aufruf mit named parameters (Reihenfolge spielt keine Rolle)
print(subtraction(zahl2=4, zahl1=5))

# Aufruf OHNE named parameters (=positional arguments, Reihenfolge ist wichtig)
print(subtraction(4, 5))
