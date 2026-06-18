# Läuft im QGIS Python Script Editor
# Öffnen: Erweiterungen → Python-Konsole → Skript-Editor öffnen
#
# QgsVectorLayer, QgsProject & Co. müssen hier NICHT importiert werden: Die QGIS
# Python-Konsole (und der Skript-Editor, der dieselbe Umgebung nutzt) lädt qgis.core
# und qgis.utils automatisch vor. Siehe PyQGIS Cookbook:
# https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/intro.html#scripting-in-the-python-console
# ruff: noqa: F821

# 1. Kantonsgrenz-Layer von swisstopo laden
# /vsizip/vsicurl/ lässt GDAL die ZIP-Datei direkt über HTTP lesen,
# ohne sie vorher manuell herunterzuladen und zu entpacken.
url = (
    "/vsizip/vsicurl/https://data.geo.admin.ch/ch.swisstopo.swissboundaries3d/"
    "swissboundaries3d_2026-01/swissboundaries3d_2026-01_2056_5728.gpkg.zip"
)
# "ogr" = Datenprovider für Vektordaten (GeoJSON, GPKG, Shapefile, ...)
# |layername=... wählt den Kantons-Layer aus dem GeoPackage (das mehrere Layer enthält)
layer = QgsVectorLayer(f"{url}|layername=tlm_kantonsgebiet", "Kantone", "ogr")
QgsProject.instance().addMapLayer(layer)
print(f"Layer geladen: {layer.featureCount()} Kantone")

# 2. Spaltennamen anzeigen
print("Spalten:", layer.fields().names())



# 3. Die 5 grössten Kantone ausgeben
kantone = []
for feature in layer.getFeatures():
    flaeche_km2 = feature.geometry().area() / 1000000  # m² → km²
    kantone.append((flaeche_km2, feature["name"]))

kantone.sort(reverse=True)
print("\nDie 5 grössten Kantone:")
for flaeche, name in kantone[:5]:
    print(f"  {name}: {flaeche:.0f} km²")

# 4. Alle Kantone selektieren, die an Bern grenzen
bern_geom = None
for feature in layer.getFeatures():
    if feature["name"] == "Bern":
        bern_geom = feature.geometry()
        break

nachbarn_ids = []
for feature in layer.getFeatures():
    if feature["name"] != "Bern" and feature.geometry().touches(bern_geom):
        nachbarn_ids.append(feature.id())

layer.selectByIds(nachbarn_ids)
print(f"\n{len(nachbarn_ids)} Kantone grenzen an Bern - in QGIS selektiert.")
