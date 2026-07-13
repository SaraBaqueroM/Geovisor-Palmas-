# ============================================================
# SCRIPT 14
# UNIR PREDICCIONES AL SHAPEFILE DE MUNICIPIOS
# ============================================================

import geopandas as gpd
import pandas as pd
from pathlib import Path

# ============================================================
# RUTAS
# ============================================================

RUTA_MUNICIPIOS = Path(
    r"C:\Users\User\Documents\MapBiomas Alerta Colombia\Unidades de analisis\nivel-politico-3\nivel-politico-3.shp"
)

RUTA_CSV = Path(
    r"C:\Users\User\Documents\GitHub\Geovisor-Palmas-\Output_analisis\Prediccion_alertas_2026.csv"
)

OUTPUT = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis"
)

# ============================================================
# LEER
# ============================================================

print("Leyendo municipios...")

municipios = gpd.read_file(RUTA_MUNICIPIOS,
    encoding="utf-8")

print("Leyendo predicciones...")

pred = pd.read_csv(RUTA_CSV)
# ============================================================
# LIMPIAR NOMBRES
# ============================================================

municipios["LEVEL_3"] = (
    municipios["LEVEL_3"]
    .astype(str)
    .str.strip()
)

pred["municipio"] = (
    pred["municipio"]
    .astype(str)
    .str.strip()
)

# ============================================================
# JOIN
# ============================================================



resultado = municipios.merge(
    pred,
    left_on="LEVEL_3",
    right_on="municipio",
    how="left"
)

resultado = resultado.drop(columns="municipio")
resultado["riesgo"] = pd.cut(
    resultado["pred_alertas_2026"],
    bins=[-1,50,200,500,1000,100000],
    labels=[
        "Muy bajo",
        "Bajo",
        "Medio",
        "Alto",
        "Muy alto"
    ]
)
# ============================================================
# EXPORTAR SHAPEFILE
# ============================================================
resultado = resultado[[
    "LEVEL_3",
    "geometry",
    "riqueza_palmas",
    "bosque_pct",
    "agro_pct",
    "alertas_2025",
    "pred_alertas_2026",
    "riesgo"
]]

riesgo_alertas = resultado[[
    "LEVEL_3",
    "geometry",
    "pred_alertas_2026",
    "riesgo"
]].copy()

riesgo_alertas.to_file(
    OUTPUT / "Municipios_Riesgo_Alertas_2026.gpkg", driver="GPKG",
    encoding="utf-8"
)

riesgo_palmas = resultado[
    resultado["riqueza_palmas"] > 0
].copy()

riesgo_palmas = riesgo_palmas[[
    "LEVEL_3",
    "geometry",
    "riqueza_palmas",
    "bosque_pct",
    "agro_pct",
    "alertas_2025",
    "pred_alertas_2026",
    "riesgo"
]]

riesgo_palmas.to_file(
    OUTPUT / "Municipios_Riesgo_Palmas_2026.gpkg", driver="GPKG",
    encoding="utf-8"
)

print("\n======================================")
print("JOIN COMPLETADO")
print("======================================")

print(f"Municipios: {len(resultado)}")

print(
    resultado[
        [
            "LEVEL_3",
            "pred_alertas_2026"
        ]
    ].head()
)

print("\nCapas generadas:")

print(OUTPUT / "Municipios_Riesgo_Alertas_2026.gpkg")
print(OUTPUT / "Municipios_Riesgo_Palmas_2026.gpkg")