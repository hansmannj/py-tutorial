from pathlib import Path

import folium
import geopandas as gpd
import pandas as pd

RESOURCES = Path(__file__).parent.parent / "resources"

# 1. CSV laden und GeoDataFrame erstellen (LV95)
df = pd.read_csv(RESOURCES / "messpunkte.csv")

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["ost"], df["nord"]), crs="EPSG:2056")

# 2. Nach WGS84 umprojizieren
gdf_wgs84 = gdf.to_crs("EPSG:4326")

# 3. folium-Karte erstellen
mitte = gdf_wgs84.geometry.union_all().centroid
karte = folium.Map(location=[mitte.y, mitte.x], zoom_start=9)

for _, row in gdf_wgs84.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x], tooltip=f"{row['name']}: {row['hoehe']} m.ü.M."
    ).add_to(karte)

# 4. Karte speichern
karte.save("messpunkte.html")
print("Karte gespeichert als messpunkte.html")
