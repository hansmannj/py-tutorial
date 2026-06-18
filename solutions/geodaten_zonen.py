from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd

RESOURCES = Path(__file__).parent.parent / "resources"

# Messpunkte laden und GeoDataFrame erstellen (LV95)
df = pd.read_csv(RESOURCES / "messpunkte.csv")
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["ost"], df["nord"]), crs="EPSG:2056")

# Messgebiete (Polygone) laden
zonen = gpd.read_file(RESOURCES / "messgebiete.geojson")

# Räumlicher Join: welcher Punkt liegt in welcher Zone?
result = gpd.sjoin(gdf, zonen, how="left", predicate="within")

print("Zonenauswertung:")
for _, row in result.iterrows():
    zone = row["name_right"] if pd.notna(row["name_right"]) else "- keine Zone"
    print(f"  {row['name_left']}: {zone}")

# Karte erstellen
gdf_wgs84 = gdf.to_crs("EPSG:4326")
zonen_wgs84 = zonen.to_crs("EPSG:4326")

mitte = gdf_wgs84.geometry.union_all().centroid

# swisstopo-Pixelkarte als Basemap
karte = folium.Map(
    location=[mitte.y, mitte.x],
    zoom_start=9,
    tiles="https://wmts.geo.admin.ch/1.0.0/ch.swisstopo.pixelkarte-farbe/default/current/3857/{z}/{x}/{y}.jpeg",
    attr="swisstopo",
)

# Zonen als eingefärbte Polygone zeichnen
farben = {"Zone Nord": "blue", "Zone Süd": "green", "Zone Ost": "orange"}

for _, zone in zonen_wgs84.iterrows():
    farbe = farben.get(zone["name"], "gray")
    # folium erwartet (Breite, Länge), Shapely liefert (Länge, Breite)
    koordinaten = []
    for lon, lat in zone.geometry.exterior.coords:
        koordinaten.append((lat, lon))
    folium.Polygon(
        locations=koordinaten,
        color="black",
        fill_color=farbe,
        fill_opacity=0.3,
        tooltip=zone["name"],
    ).add_to(karte)

# Messpunkte als Marker
for _, row in gdf_wgs84.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        tooltip=row["name"],
    ).add_to(karte)

karte.save("messpunkte_zonen.html")
print("\nKarte gespeichert als messpunkte_zonen.html")
