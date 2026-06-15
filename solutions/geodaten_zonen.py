import folium
import geopandas as gpd
import pandas as pd

# Messpunkte laden und GeoDataFrame erstellen (LV95)
df = pd.read_csv("../resources/messpunkte.csv")
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["ost"], df["nord"]), crs="EPSG:2056")

# Messgebiete (Polygone) laden
zonen = gpd.read_file("../resources/messgebiete.geojson")

# Räumlicher Join: welcher Punkt liegt in welcher Zone?
result = gpd.sjoin(gdf, zonen, how="left", predicate="within")

print("Zonenauswertung:")
for _, row in result.iterrows():
    zone = row["name_right"] if pd.notna(row["name_right"]) else "— keine Zone"
    print(f"  {row['name_left']}: {zone}")

# Punkte ohne Zone
ohne_zone = result[result["name_right"].isna()]
print(f"\n{len(ohne_zone)} Punkt(e) ohne Zonenzuordnung:")
for _, row in ohne_zone.iterrows():
    print(f"  {row['name_left']}")

# Karte mit Zonen und Messpunkten
gdf_wgs84 = gdf.to_crs("EPSG:4326")
zonen_wgs84 = zonen.to_crs("EPSG:4326")

mitte = gdf_wgs84.geometry.unary_union.centroid
karte = folium.Map(location=[mitte.y, mitte.x], zoom_start=9)

farben = {"Zone Nord": "blue", "Zone Süd": "green", "Zone Ost": "orange"}

folium.GeoJson(
    zonen_wgs84,
    style_function=lambda f: {
        "fillColor": farben.get(f["properties"]["name"], "gray"),
        "fillOpacity": 0.3,
        "color": "black",
        "weight": 1,
    },
    tooltip=folium.GeoJsonTooltip(fields=["name"]),
).add_to(karte)

for _, row in result.iterrows():
    point_wgs84 = gdf_wgs84[gdf_wgs84["name"] == row["name_left"]].iloc[0]
    zone = row["name_right"] if pd.notna(row["name_right"]) else "keine Zone"
    folium.Marker(
        location=[point_wgs84.geometry.y, point_wgs84.geometry.x],
        tooltip=f"{row['name_left']} ({zone})",
    ).add_to(karte)

karte.save("messpunkte_zonen.html")
print("\nKarte gespeichert als messpunkte_zonen.html")
