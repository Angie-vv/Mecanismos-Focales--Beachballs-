
!pip install numpy pandas

#Lee los datos guardados de mecanismos focales
import pandas as pd

df = pd.read_csv('/content/valparaiso_focal_mechanisms.csv')
print(df.columns)

import numpy as np


def classify_regime(row):
    # Crea la matriz de moment tensor
    M = np.array([
        [row['Mrr'], row['Mrt'], row['Mrp']],
        [row['Mrt'], row['Mtt'], row['Mtp']],
        [row['Mrp'], row['Mtp'], row['Mpp']]
    ])

    # Decomposicion Eigen
    eigvals, eigvecs = np.linalg.eigh(M)

    # Sort eigenvalues descendente
    idx = eigvals.argsort()[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]

    # T-axis = eigenvector of smallest eigenvalue (last), P-axis = largest (first)
    T_axis = eigvecs[:, 2]
    P_axis = eigvecs[:, 0]

    # Compute plunge (angle from vertical) in degrees
    def calc_plunge(vector):
        return np.degrees(np.arccos(abs(vector[2])))  # z-component = vertical

    T_plunge = calc_plunge(T_axis)
    P_plunge = calc_plunge(P_axis)

    # Clasificacion basada en el plunge
    if P_plunge < 35 and T_plunge > 52:
        return 'Extension'
    elif P_plunge > 52 and T_plunge < 35:
        return 'Compression'
    elif P_plunge < 35 and T_plunge < 35:
        return 'Strike-slip'
    else:
        return 'Oblique'

# Aplica la clasificacion
df['regime'] = df.apply(classify_regime, axis=1)

# Guarda el resultado
df.to_csv('beachballs_classified_Tarapaca.csv', index=False)

print("Classification complete. Output saved to beachballs_classified.csv")

# Revisa que no existan valores Nulos
print(df.isnull().sum())

#instala obspy si no lo tienes
!pip install obspy

#instala cartopy para crear el mapa
!pip install cartopy

#crea tu mapa de mecanismos focales
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from obspy.imaging.beachball import beach

# carga tu CSV con columnas: latitude, longitude, Mrr(Mxx), Mtt(Myy), Mpp(Mzz), Mrt(Mxy), Mrp(Mxz), Mtp(Myz), regime
df = pd.read_csv('/content/beachballs_classified_Tarapaca.csv')

color_map = {
    'Extension': 'blue',
    'Compression': 'red',
    'Oblique': 'orange'
}

# Crea una figura con PlateCarree projection (simple lat/lon)
fig = plt.figure(figsize=(12, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

# Añade map features: coastlines, borders, gridlines, land, ocean, etc.
ax.coastlines(resolution='10m')
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.gridlines(draw_labels=True)

# Plotea cada pelota de playa (beachball) en el map usando latitude/longitude
for idx, row in df.iterrows():
    mt = [row['Mrr'], row['Mrt'], row['Mrp'], row['Mtt'], row['Mtp'], row['Mpp']]
    color = color_map.get(row['regime'], 'gray')

    # Beachball tamaño en degrees (ajusta width para cambiar el tamaño)
    b = beach(mt, width=0.1, linewidth=1, facecolor=color, xy=(row['longitude'], row['latitude']))
    ax.add_collection(b)

# Leyenda para los regimenes
for label, color in color_map.items():
    ax.plot([], [], marker='o', linestyle='', label=label, color=color)
ax.legend(loc='lower right')

#Plotea tu mapa final
plt.title("Mecanismos Focales Region de Valparaiso")
plt.show()