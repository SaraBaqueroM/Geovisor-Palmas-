# ============================================================
# SCRIPT 15
# Comprimir Geojson para cargar en GitHub Pages
# ============================================================

import geopandas as gpd
import pandas as pd
from pathlib import Path

import geopandas as gpd
from shapely import set_precision
from shapely.ops import transform

# ==========================
# CONFIGURACIÓN
# ==========================

archivo_entrada = r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\Municipios_con_palmas_con_riesgo_alertas_2026.geojson"
archivo_salida  = r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\Municipios_con_palmas_con_riesgo_alertas_2026_COMPRESSED.geojson"

# Simplificación en unidades del CRS.
# Si el CRS es EPSG:4674 (grados), 0.0002 ≈ 20 m.
tolerancia = 0.0002

# Mantener únicamente campos necesarios
campos = [
    "LEVEL_2",
    "LEVEL_3",
    "riqueza_palmas",
    "bosque_pct",
    "agro_pct",
    "alertas_2020",
    "alertas_2021",
    "alertas_2022",
    "alertas_2023",
    "alertas_2024",
    "alertas_2025",
    "pred_alertas_2026",
    "riesgo"
]

# ==========================
# FUNCIONES
# ==========================

def quitar_z(geom):
    """Elimina coordenadas Z."""
    if geom is None:
        return None

    def f(x, y, z=None):
        return (x, y)

    return transform(f, geom)


# ==========================
# PROCESO
# ==========================

print("Leyendo archivo...")
gdf = gpd.read_file(archivo_entrada)

print("Eliminando coordenada Z...")
gdf.geometry = gdf.geometry.apply(quitar_z)

print("Simplificando geometrías...")
gdf.geometry = gdf.geometry.simplify(
    tolerance=tolerancia,
    preserve_topology=True
)

print("Redondeando coordenadas (6 decimales)...")
# grid_size=1e-6 equivale aproximadamente a 6 decimales
gdf.geometry = gdf.geometry.apply(lambda g: set_precision(g, grid_size=1e-6))

print("Eliminando columnas innecesarias...")
campos_existentes = [c for c in campos if c in gdf.columns]
gdf = gdf[campos_existentes + ["geometry"]]

print("Exportando GeoJSON...")
gdf.to_file(
    archivo_salida,
    driver="GeoJSON"
)

print("Proceso terminado.")
print("Archivo generado:")
print(archivo_salida)