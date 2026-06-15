# Läuft im QGIS Python Script Editor
# Öffnen: Erweiterungen → Python-Konsole → Skript-Editor öffnen

from qgis.core import QgsProject  # noqa: F821
from qgis.core import QgsVectorLayer  # noqa: F821

# 1. Kantonsgrenz-Layer von swisstopo laden
url = (
    "https://data.geo.admin.ch/ch.swisstopo.swissboundaries3d-kanton-flaeche.fill/"
    "swissboundaries3d-kanton-flaeche.fill/"
    "swissboundaries3d-kanton-flaeche.fill_2056.json"
)
# "ogr" = Datenprovider für Vektordaten (GeoJSON, GPKG, Shapefile, ...)
layer = QgsVectorLayer(url, "Kantone", "ogr")
QgsProject.instance().addMapLayer(layer)
print(f"Layer geladen: {layer.featureCount()} Kantone")

# 2. Spaltennamen anzeigen
print("Spalten:", layer.fields().names())

# 3. Die 5 grössten Kantone ausgeben
kantone = []
for feature in layer.getFeatures():
    flaeche_km2 = feature.geometry().area() / 1000000  # m² → km²
    kantone.append((flaeche_km2, feature["NAME"]))

kantone.sort(reverse=True)
print("\nDie 5 grössten Kantone:")
for flaeche, name in kantone[:5]:
    print(f"  {name}: {flaeche:.0f} km²")

# 4. Alle Kantone selektieren, die an Bern grenzen
bern_geom = None
for feature in layer.getFeatures():
    if feature["NAME"] == "Bern":
        bern_geom = feature.geometry()
        break

nachbarn_ids = []
for feature in layer.getFeatures():
    if feature["NAME"] != "Bern" and feature.geometry().touches(bern_geom):
        nachbarn_ids.append(feature.id())

layer.selectByIds(nachbarn_ids)
print(f"\n{len(nachbarn_ids)} Kantone grenzen an Bern - in QGIS selektiert.")
