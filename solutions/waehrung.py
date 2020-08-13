import requests

# Benutzereingabe base
while True:
    base = input("Bitte die Quellwährung eingeben: ").upper()

    # Webdienst für base-Währung aufrufen
    service = r"https://api.exchangeratesapi.io/latest"
    parameters = {
        "base": base
    }
    response = requests.get(url=service, params=parameters, verify=False)
    result = response.json()

    if "error" in result.keys():
        print(result["error"])
    else:
        break

# Benutzereingabe symbol
while True:
    symbol = input("Bitte die Zielwährung eingeben: ").upper()
    if symbol in result["rates"].keys():
        rate = result["rates"][symbol]
        break
    else:
        print("Bitte eine gültige Wärung eingeben!")

# Benutzereingabe amount
while True:
    amount = input("Bitte Betrag eingeben: ")
    try:
        amount = float(amount)
        break
    except:
        print("Bitte eine Zahl eingeben!")

# Berechnung und Ausgabe
print("{a} {b} = {a2} {s}".format(a=amount, b=base, a2=round(amount * rate, 2), s=symbol))
