import pandas as pd

# Daten aus Excel-File in einen pandas DataFrame einlesen:
df = pd.read_excel("../resources/Zufallskoordinaten_WGS84.xlsx")

# filtern
# (siehe auch: https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)
df_gefiltert = df[(df['Z'] > 1000) & (df['Z'] < 2000)]

# Die gefilterten Daten wieder in ein Excel-File exportieren:
df_gefiltert.to_excel(("Koordinaten_gefiltert.xlsx"))

print(f"Ca. {100 * df_gefiltert.shape[0]/df.shape[0]} % der Koordinaten haben " \
    f"Z-Werte zwischen 1000 und 2000 m N.N.")
