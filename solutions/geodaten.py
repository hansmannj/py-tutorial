import folium
import geopandas as gpd
import pandas as pd

# 1. CSV laden und GeoDataFrame erstellen (LV95)
df = pd.read_csv("../resources/messpunkte.csv")

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["ost"], df["nord"]), crs="EPSG:2056")

# 2. Nach WGS84 umprojizieren
gdf_wgs84 = gdf.to_crs("EPSG:4326")

# 3. Puffer (2 km) berechnen und Überschneidungen prüfen
gdf["buffer"] = gdf.geometry.buffer(2000)

print("Überschneidungen zwischen Puffern:")
for i, row_i in gdf.iterrows():
    for j, row_j in gdf.iterrows():
        if i >= j:
            continue
        if row_i["buffer"].intersects(row_j["buffer"]):
            print(f"  {row_i['name']} ↔ {row_j['name']}")

# 4. folium-Karte erstellen
mitte = gdf_wgs84.geometry.unary_union.centroid
karte = folium.Map(location=[mitte.y, mitte.x], zoom_start=9)

for _, row in gdf_wgs84.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x], tooltip=f"{row['name']}: {row['hoehe']} m.ü.M."
    ).add_to(karte)

# 5. Karte speichern
karte.save("messpunkte.html")
print("Karte gespeichert als messpunkte.html")
