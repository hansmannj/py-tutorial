import math

import folium
import pandas as pd
import requests


def profile_lv95(punkt1, punkt2, n):
    """Calculates coordinates along a line between two given points, so that
    the line consist of n points in the end, and gets z-coordinates for the n
    points from webservice.

    Args:
        punkt1: Tupel of two float coordinates in LV95 format. Starting point.
        punkt2: Tupel of two float coordinates in LV95 format. Terminal point.
        n: Integer. Number of points for the returned DataFrame.

    Returns:
        A pandas DataFrame with Easting, Northing, Z-value and distance from
        start for n points on a line from punkt1 to punkt2 in LV95 format.
    """
    service = "https://api3.geo.admin.ch/rest/services/height"

    # leeren pandas DataFrame initialisieren. In der Spalte "km from start" wird die Entfernung
    # von jedem Punkt auf der Linie zum Startpunkt gespeichert.
    df = pd.DataFrame(columns=['Easting', 'Northing', 'Z', 'km from start'], dtype=float)
    delta_easting = punkt2[0] - punkt1[0]
    delta_northing = punkt2[1] - punkt1[1]

    for i in range(n):
        easting = punkt1[0] + i * delta_easting / (n - 1)
        northing = punkt1[1] + i * delta_northing / (n - 1)

        params = {"easting": easting, "northing": northing, "sr": 2056}

        # Höhe des aktuellen Punkts vom Webdienst abfragen
        response = requests.get(url=service, params=params, verify=True)
        z = float(response.json()["height"]) / 1000  # umgerechnet in km
        km_from_start = math.sqrt(
            (i * delta_easting / (n - 1))**2 + (i * delta_northing / (n - 1))**2
        ) / 1000
        # neuer kleiner DataFrame mit den aktuellen X-, Y- und Z-Koordinaten und Distanz zum Start:
        current_XYZ = pd.DataFrame(
            {
                "Easting": [easting],
                "Northing": [northing],
                "Z": [z],
                "km from start": [km_from_start]
            },
            dtype=float
        )
        df = pd.concat([df, current_XYZ], ignore_index=True)

    return df


def lv95_in_wgs84(df_lv95):
    """Transforms lv95 eastings and northings of given DataFrame into wgs84 coordinates
    and returns those in a new DataFrame. The Z-value is kept from the input frame.

    Args:
        df_lv95: pandas DataFrame with coordinates in LV95 format.

    Returns:
        A pandas DataFrame with the converted coordinates in WGS84 format.
    """
    # Transformation von LV95 zu WGS84
    service = "http://geodesy.geo.admin.ch/reframe/lv95towgs84"
    in_wgs84 = pd.DataFrame(columns=['Easting', 'Northing', 'Z'], dtype=float)

    for _, row in df_lv95.iterrows():
        params = {"easting": row[0], "northing": row[1], "format": "json"}
        response = requests.get(url=service, params=params, verify=False)
        easting = response.json()["easting"]
        northing = response.json()["northing"]

        # neuer kleiner DataFrame mit den aktuellen X-, Y- und Z-Koordinaten:
        current_XYZ = pd.DataFrame(
            {
                "Easting": [easting], "Northing": [northing], "Z": [row[2]]
            }, dtype=float
        )
        in_wgs84 = pd.concat([in_wgs84, current_XYZ], ignore_index=True)

    return in_wgs84


def generate_folium_map(df_to_plot):
    """Creates a folium map and plots the points of the provided DataFrame in this map.
    Saves this map under the name "index.html".

    Args:
        df_to_plot: pandas DataFrame with points to be plotted (in WGS84 format).

    """
    # Bei der Wahl des Referenzsystems (crs=EPSG3857), war ich nicht 100% sicher, ob es komplett
    # kompatibel mit den Daten ist, die wir vom web-service haben umwandeln lassen. Aber es sieht
    # schonmal nicht schlecht aus.
    m = folium.Map(location=[46.170018, 8.77492038], zoom_start=8, crs="EPSG3857")

    for _, row in df_to_plot.iterrows():
        folium.CircleMarker(location=[row["Northing"], row["Easting"]], radius=5).add_to(m)

    m.save("my_map.html")


def plot_Hoehenprofil(df_to_plot):
    """Plots a vertical profile, taking 'km from start' as x axis and 'Z' as y axis.
    Export this profile to the file Hoehenprofil.png.

    Args:
        df_to_plot: pandas DataFrame with points to be plotted.

    """
    ax = df_to_plot.plot(x='km from start', y='Z', figsize=(15, 15))
    ax.set_aspect(8)
    fig = ax.get_figure()
    fig.savefig("Hoehenprofil.png")


# Abgefragt über Search-Service mit sr=2056
# Bern: https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=Bern&type=locations&limit=1&sr=2056
# Locarno: https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=Locarno&type=locations&limit=1&sr=2056
Bern = [2598633.75, 1200386.75]
Locarno = [2711536, 1113566.625]

# pandas DataFrame mit den Punkten entlang der Linie zwischen Bern und Locarno in LV95:
profillinie_lv95 = profile_lv95(Bern, Locarno, 50)

# pandas DataFrame mit den Punkten entlang der Linie zwischen Bern und Locarno umwandeln in WGS84:
profillinie_wgs84 = lv95_in_wgs84(profillinie_lv95)

# Höhenprofil und Folium-Karte erstellen:
plot_Hoehenprofil(profillinie_lv95)
generate_folium_map(profillinie_wgs84)
