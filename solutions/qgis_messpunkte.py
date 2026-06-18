# Dieses Skript läuft im QGIS Python Script Editor, nicht als normales Python-Skript.
# Voraussetzung: messpunkte.csv manuell laden (Layer → Layer hinzufügen → Getrennte Textdatei)
#
# iface ist ein QGIS-Builtin, das die Konsole automatisch bereitstellt - kein Import nötig.
# ruff: noqa: F821

layer = iface.activeLayer()

print(f"Layer: {layer.name()}, {layer.featureCount()} Features")
print(f"Felder: {layer.fields().names()}")

# Name und Höhe aller Messpunkte ausgeben
hoehen = []
for feature in layer.getFeatures():
    hoehe = float(feature["hoehe"])
    hoehen.append(hoehe)
    print(f"  {feature['name']}: {hoehe} m.ü.M.")

# Höhendifferenz berechnen
differenz = max(hoehen) - min(hoehen)
print(f"\nHöchster Punkt: {max(hoehen)} m.ü.M.")
print(f"Tiefster Punkt: {min(hoehen)} m.ü.M.")
print(f"Höhendifferenz: {differenz:.1f} m")
