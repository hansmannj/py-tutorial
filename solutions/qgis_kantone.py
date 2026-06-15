# Läuft im QGIS Python Script Editor (nicht als normales Python-Skript)
# Öffnen: Erweiterungen → Python-Konsole → Skript-Editor öffnen

import os
import urllib.request
import zipfile

from qgis.core import QgsProject
from qgis.core import QgsVectorLayer

# --- Schritt 1: GeoPackage von swisstopo herunterladen ---
url = (
    "https://data.geo.admin.ch/ch.swisstopo.swissboundaries3d/"
    "swissboundaries3d_2026-01/swissboundaries3d_2026-01_2056_5728.gpkg.zip"
)
zip_pfad = os.path.join(os.path.expanduser("~"), "swissboundaries3d.zip")
print("Herunterladen...")
urllib.request.urlretrieve(url, zip_pfad)
print(f"Gespeichert: {zip_pfad}")

# --- Schritt 2: Zip entpacken ---
ziel_ordner = os.path.join(os.path.expanduser("~"), "swissboundaries3d")
with zipfile.ZipFile(zip_pfad, "r") as z:
    z.extractall(ziel_ordner)
print(f"Entpackt nach: {ziel_ordner}")

# --- Schritt 3: GPKG-Datei finden ---
gpkg_pfad = None
for datei in os.listdir(ziel_ordner):
    if datei.endswith(".gpkg"):
        gpkg_pfad = os.path.join(ziel_ordner, datei)
        break
print(f"GeoPackage: {gpkg_pfad}")

# --- Schritt 4: Verfügbare Layer im GeoPackage anzeigen ---
# Ein GeoPackage kann mehrere Layer enthalten
temp = QgsVectorLayer(gpkg_pfad, "temp", "ogr")
layer_namen = [sublayer.split("!!::!!")[1] for sublayer in temp.dataProvider().subLayers()]
print("Verfügbare Layer:", layer_namen)

# --- Schritt 5: Kantonsgrenz-Layer laden ---
# Den Layer suchen, der "kant" im Namen hat
kanton_layer_name = next(n for n in layer_namen if "kant" in n.lower())
layer = QgsVectorLayer(f"{gpkg_pfad}|layername={kanton_layer_name}", "Kantone", "ogr")
QgsProject.instance().addMapLayer(layer)
print(f"Layer geladen: {layer.featureCount()} Kantone")

# --- Schritt 6: Name und Fläche jedes Kantons sammeln ---
kantone = []
for feature in layer.getFeatures():
    name = feature["NAME"]

    # Die Geometrie ist 3D — Z-Werte entfernen, damit area() korrekt rechnet
    geom = feature.geometry()
    abstract = geom.get()
    if abstract:
        abstract.dropZValue()
    flaeche_km2 = geom.area() / 1e6  # Quadratmeter → km²

    kantone.append((flaeche_km2, name))

# --- Schritt 7: Nach Fläche sortieren und Top 5 ausgeben ---
kantone.sort(reverse=True)
print("\nDie 5 flächengrössten Kantone:")
for flaeche, name in kantone[:5]:
    print(f"  {name}: {flaeche:.0f} km²")
