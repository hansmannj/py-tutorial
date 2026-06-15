# Dieses Skript läuft im QGIS Python Script Editor, nicht als normales Python-Skript.
# Voraussetzung: messpunkte.csv wurde manuell geladen (Layer → Layer hinzufügen → Getrennte Textdatei)

layer = iface.activeLayer()

print(f"Layer: {layer.name()}, {layer.featureCount()} Features")
print(f"Felder: {layer.fields().names()}")

# Name und Höhe aller Messpunkte ausgeben
hoechen = []
for feature in layer.getFeatures():
    hoehe = float(feature["hoehe"])
    hoechen.append(hoehe)
    print(f"  {feature['name']}: {hoehe} m.ü.M.")

# Höhendifferenz berechnen
differenz = max(hoechen) - min(hoechen)
print(f"\nHöchster Punkt: {max(hoechen)} m.ü.M.")
print(f"Tiefster Punkt: {min(hoechen)} m.ü.M.")
print(f"Höhendifferenz: {differenz:.1f} m")
