# ============================================================
# ALERTAS IDEAM POR MUNICIPIO (2017-2025)
#
# Lee automáticamente todos los KML organizados por año:
#
# IDEAM/
# ├── 2017/
# │   ├── T1.kml
# │   ├── T2.kml
# │   ├── T3.kml
# │   └── T4.kml
# ├── 2018/
# └── ...
#
# Resultado:
# LEVEL_3 | alertas_2017 | ... | alertas_2025 | alertas_total
#
# ============================================================

import geopandas as gpd
import pandas as pd
from pathlib import Path

# ============================================================
# RUTAS
# ============================================================

CARPETA_IDEAM = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Alertas\IDEAM"
)

MUNICIPIOS = (
    r"C:\Users\User\Documents\MapBiomas Alerta Colombia"
    r"\Unidades de analisis\nivel-politico-3\nivel-politico-3.shp"
)

SALIDA = Path("Output_analisis")
SALIDA.mkdir(exist_ok=True)

# ============================================================
# MUNICIPIOS
# ============================================================

print("\nLeyendo municipios...")

municipios = gpd.read_file(MUNICIPIOS)

municipios = municipios[["LEVEL_3", "geometry"]].copy()

municipios["LEVEL_3"] = (
    municipios["LEVEL_3"]
    .astype(str)
    .str.strip()
)

# DataFrame base
resultado = pd.DataFrame({
    "LEVEL_3": sorted(municipios["LEVEL_3"].unique())
})

# ============================================================
# RECORRER AÑOS
# ============================================================

for carpeta in sorted(CARPETA_IDEAM.iterdir()):

    if not carpeta.is_dir():
        continue

    año = carpeta.name

    print("\n===================================")
    print(f"AÑO {año}")
    print("===================================")

    kmls = sorted(carpeta.glob("*.kml"))

    if len(kmls) == 0:
        print("No se encontraron KML.")
        continue

    lista = []

    # --------------------------------------------------------

    for archivo in kmls:

        print(f"Leyendo {archivo.name}")

        try:

            gdf = gpd.read_file(
                archivo,
            )

            if len(gdf) > 0:
                lista.append(gdf)

        except Exception as e:

            print(f"Error leyendo {archivo.name}")
            print(e)

    if len(lista) == 0:
        continue

    # --------------------------------------------------------
    # Unir todos los trimestres
    # --------------------------------------------------------

    puntos = gpd.GeoDataFrame(
        pd.concat(lista, ignore_index=True),
        crs=lista[0].crs
    )

    # eliminar geometrías inválidas

    puntos = puntos[
        puntos.geometry.notnull()
    ]

    puntos = puntos[
        puntos.is_valid
    ]

    # mismo sistema de coordenadas

    if puntos.crs != municipios.crs:
        puntos = puntos.to_crs(municipios.crs)

    print(f"Total puntos: {len(puntos):,}")

    # --------------------------------------------------------
    # Spatial Join
    # --------------------------------------------------------

    join = gpd.sjoin(
        puntos,
        municipios,
        how="left",
        predicate="intersects"
    )

    # --------------------------------------------------------
    # Conteo
    # --------------------------------------------------------

    conteo = (
        join
        .groupby("LEVEL_3")
        .size()
        .reset_index(name=f"alertas_{año}")
    )

    resultado = resultado.merge(
        conteo,
        on="LEVEL_3",
        how="left"
    )

# ============================================================
# RELLENAR CEROS
# ============================================================

for c in resultado.columns:

    if c.startswith("alertas_"):

        resultado[c] = (
            resultado[c]
            .fillna(0)
            .astype(int)
        )

# ============================================================
# TOTAL
# ============================================================

cols = [
    c
    for c in resultado.columns
    if c.startswith("alertas_")
]

resultado["alertas_total"] = resultado[cols].sum(axis=1)

# ============================================================
# ORDENAR
# ============================================================

resultado = resultado.sort_values(
    "alertas_total",
    ascending=False
)

# ============================================================
# EXPORTAR
# ============================================================

archivo_salida = (
    SALIDA /
    "Alertas_IDEAM_por_municipio_2017_2025.csv"
)
resultado["LEVEL_3"] = (
    resultado["LEVEL_3"]
    .str.encode("latin1")
    .str.decode("utf-8")
)
resultado.to_csv(
    archivo_salida,
    index=False,
    encoding="utf-8-sig"
)

print("\n========================================")
print("PROCESO FINALIZADO")
print("========================================")
print(resultado.head(20))
print(f"\nArchivo guardado en:\n{archivo_salida}")