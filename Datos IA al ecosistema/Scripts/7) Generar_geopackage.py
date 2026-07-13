"""
===========================================================================
06_generar_geopackage.py
---------------------------------------------------------------------------

Convierte las ocurrencias limpias en un GeoPackage.

Capas generadas:

1. ocurrencias
   - Un punto por registro del CSV.

2. ocurrencias_unicas
   - Elimina registros duplicados espacialmente
     (misma especie + mismas coordenadas).

3. especies
   - Una geometría MULTIPOINT por especie.

Entrada:
    ocurrencias_palmas_clean.csv

Salida:
    capa_palmas.gpkg

Autor: Equipo Datos al Ecosistema 2026
Proyecto: Concurso Datos al Ecosistema 2026
===========================================================================
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import MultiPoint
from pathlib import Path

# -------------------------------------------------------------------------
# Rutas
# -------------------------------------------------------------------------

INPUT = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas_clean.csv"
)

OUTPUT = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\capa_palmas.gpkg"
)

# -------------------------------------------------------------------------
# Leer datos
# -------------------------------------------------------------------------

print("\nLeyendo ocurrencias...")

df = pd.read_csv(INPUT)

# -------------------------------------------------------------------------
# Eliminar registros sin coordenadas
# -------------------------------------------------------------------------

df = df.dropna(subset=["decimalLatitude", "decimalLongitude"])

print(f"Registros con coordenadas: {len(df):,}")

# -------------------------------------------------------------------------
# Crear GeoDataFrame
# -------------------------------------------------------------------------

gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(
        df["decimalLongitude"],
        df["decimalLatitude"]
    ),
    crs="EPSG:4326"
)

# -------------------------------------------------------------------------
# Guardar capa de ocurrencias
# -------------------------------------------------------------------------

gdf.to_file(
    OUTPUT,
    layer="ocurrencias",
    driver="GPKG"
)

print("✓ Capa 'ocurrencias' creada.")

# -------------------------------------------------------------------------
# Crear capa de ocurrencias únicas
# -------------------------------------------------------------------------

print("Generando ocurrencias únicas...")

if "duplicado_espacial" in gdf.columns:

    gdf_unicas = gdf.loc[
        ~gdf["duplicado_espacial"]
    ].copy()

else:

    gdf_unicas = gdf.drop_duplicates(
        subset=[
            "NOMBRE CIENTIFICO",
            "decimalLatitude",
            "decimalLongitude"
        ]
    ).copy()

gdf_unicas.to_file(
    OUTPUT,
    layer="ocurrencias_unicas",
    driver="GPKG"
)

print("✓ Capa 'ocurrencias_unicas' creada.")

# -------------------------------------------------------------------------
# Crear capa MULTIPOINT por especie
# -------------------------------------------------------------------------

print("Generando capa de especies...")

registros = []

for especie, grupo in gdf.groupby("NOMBRE CIENTIFICO"):

    registro = {

        "NOMBRE CIENTIFICO":
            especie,

        "NOMBRE VERNACULO":
            grupo["NOMBRE VERNACULO"].dropna().iloc[0]
            if grupo["NOMBRE VERNACULO"].notna().any()
            else None,

        "GENERO":
            grupo["GENERO"].iloc[0],

        "FAMILIA":
            grupo["FAMILIA"].iloc[0],

        "ESTADO AMENAZA":
            grupo["ESTADO DE AMENAZA"].iloc[0],

        "TOTAL OCURRENCIAS":
            len(grupo),

        "geometry":
            MultiPoint(list(grupo.geometry))

    }

    registros.append(registro)

gdf_especies = gpd.GeoDataFrame(
    registros,
    geometry="geometry",
    crs="EPSG:4326"
)

gdf_especies.to_file(
    OUTPUT,
    layer="especies",
    driver="GPKG"
)

print("✓ Capa 'especies' creada.")

# -------------------------------------------------------------------------
# Resumen
# -------------------------------------------------------------------------

print("\n==========================================")
print("GeoPackage generado correctamente")
print("==========================================")

print(f"Archivo: {OUTPUT}")

print(f"Ocurrencias           : {len(gdf):,}")
print(f"Ocurrencias únicas    : {len(gdf_unicas):,}")
print(f"Especies              : {len(gdf_especies):,}")

print("\nCapas creadas:")
print("  • ocurrencias")
print("  • ocurrencias_unicas")
print("  • especies")