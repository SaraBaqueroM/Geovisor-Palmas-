"""
===========================================================================
08_Enriquecimiento_espacial.py
---------------------------------------------------------------------------

Enriquecer el dataset con información de: Resguardos Indigenas, departamentos, municipios, Areas naturales
protegidas nacionales, alertas de deforestacion GLAD, coberturas y uso del suelo de MapBiomas Colombia Coleccion 3

Autor: Equipo 302 Datos al Ecosistema 2026
Proyecto: Concurso Datos al Ecosistema 2026
===========================================================================
"""

import pandas as pd
import geopandas as gpd
import rasterio

from pathlib import Path
from shapely.geometry import Point

# ============================================================
# RUTAS
# ============================================================

CSV_OCURRENCIAS = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas_clean.csv"
)

DEPARTAMENTOS = Path(
    r"C:\Users\User\Documents\MapBiomas Alerta Colombia\Unidades de analisis\nivel-politico-2\nivel-politico-2.shp"
)

MUNICIPIOS = Path(
    r"C:\Users\User\Documents\MapBiomas Alerta Colombia\Unidades de analisis\nivel-politico-3\nivel-politico-3.shp"
)

AREAS_PROTEGIDAS = Path(
    r"C:\Users\User\Documents\MapBiomas Alerta Colombia\Unidades de analisis\area-natural-protegida-nacional\area-natural-protegida-nacional.shp"
)

RESGUARDOS = Path(
    r"C:\Users\User\Documents\MapBiomas Alerta Colombia\Unidades de analisis\resguardo-indigena\resguardo-indigena.shp"
)

MAPBIOMAS = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\INTEGRACION-COLOMBIA-COL3-2024.tif"
)

GLAD_FOLDER = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Alertas"
)

OUTPUT_CSV = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_enriquecido.csv"
)

OUTPUT_GPKG = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_enriquecido.gpkg"
)
# -------------------------------------------------------------------------
# Leer datos
# -------------------------------------------------------------------------

print("Leyendo ocurrencias...")

df = pd.read_csv(CSV_OCURRENCIAS)

gdf = gpd.GeoDataFrame(

    df,

    geometry=gpd.points_from_xy(
        df.decimalLongitude,
        df.decimalLatitude
    ),

    crs="EPSG:4326"

)

print(f"Ocurrencias: {len(gdf):,}")
print(f"CRS: {gdf.crs}")

# -------------------------------------------------------------------------
# Leer todas las capas
# -------------------------------------------------------------------------

departamentos = gpd.read_file(DEPARTAMENTOS)

municipios = gpd.read_file(MUNICIPIOS)

anp = gpd.read_file(AREAS_PROTEGIDAS)

resguardos = gpd.read_file(RESGUARDOS)

# -------------------------------------------------------------------------
# Reproyectar capas 
# -------------------------------------------------------------------------

departamentos = departamentos.to_crs(gdf.crs)

municipios = municipios.to_crs(gdf.crs)

anp = anp.to_crs(gdf.crs)

resguardos = resguardos.to_crs(gdf.crs)

# -------------------------------------------------------------------------
# Uniones espaciales
# -------------------------------------------------------------------------

# ============================================================
# Función para Spatial Join
# ============================================================

def agregar_campo_espacial(gdf, capa, campo_origen, campo_destino):
    """
    Agrega un atributo mediante Spatial Join.

    Parameters
    ----------
    gdf : GeoDataFrame
    capa : GeoDataFrame
    campo_origen : str
    campo_destino : str
    """

    resultado = gpd.sjoin(
        gdf,
        capa[[campo_origen, "geometry"]],
        how="left",
        predicate="within"
    )

    resultado.rename(
        columns={campo_origen: campo_destino},
        inplace=True
    )

    if "index_right" in resultado.columns:
        resultado.drop(columns="index_right", inplace=True)

    return resultado

print("Asignando departamentos...")

gdf = agregar_campo_espacial(
    gdf,
    departamentos,
    "LEVEL_2",
    "departamento"
)

print("Asignando municipios...")

gdf = agregar_campo_espacial(
    gdf,
    municipios,
    "LEVEL_3",
    "municipio"
)

print("Asignando resguardos...")

gdf = agregar_campo_espacial(
    gdf,
    resguardos,
    "LEVEL_3",
    "resguardo"
)

def agregar_anp(gdf, anp):

    resultado = gpd.sjoin(
        gdf,
        anp[
            [
                "LEVEL_2",
                "LEVEL_3",
                "geometry"
            ]
        ],
        how="left",
        predicate="within"
    )

    resultado.rename(
        columns={
            "LEVEL_2":"categoria_anp",
            "LEVEL_3":"nombre_anp"
        },
        inplace=True
    )

    if "index_right" in resultado.columns:
        resultado.drop(columns="index_right", inplace=True)

    return resultado

print("Asignando Áreas Protegidas...")

gdf = agregar_anp(
    gdf,
    anp
)

print(gdf.columns)

# ============================================================
# Unir datos desde el raster de MapBiomas Colombia
# ============================================================

print("Extrayendo cobertura MapBiomas...")

with rasterio.open(MAPBIOMAS) as src:

    valores = [
        valor[0]
        for valor in src.sample(
            zip(
                gdf.geometry.x,
                gdf.geometry.y
            )
        )
    ]

gdf["codigo_cobertura"] = valores

CLASES_MAPBIOMAS = {

    3: "Bosque",
    5: "Manglar",
    6: "Bosque inundable",
    49: "Vegetación leñosa sobre arena",

    11: "Formación natural no forestal inundable",
    12: "Formación herbácea",
    32: "Planicie de marea hipersalina",
    29: "Afloramiento rocoso",
    50: "Vegetación herbácea sobre arena",
    13: "Otra formación natural no forestal",
    81: "Herbazales o arbustales andinos",
    82: "Herbazales o arbustales andinos inundables",

    9: "Silvicultura",
    35: "Palma aceitera",
    74: "Plátano y banano",
    21: "Mosaico de agricultura o pasto",

    23: "Playas, dunas y bancos de arena",
    24: "Infraestructura urbana",
    30: "Minería",
    68: "Otra área natural sin vegetación",
    25: "Otra área sin vegetación",
    75: "Parques solares",

    33: "Río, lago u océano",
    31: "Acuicultura",
    34: "Glaciar y nival",

    27: "No observado"

}

gdf["clase_cobertura"] = (
    gdf["codigo_cobertura"]
    .map(CLASES_MAPBIOMAS)
)

CATEGORIAS = {

    3: "Bosque natural",
    5: "Bosque natural",
    6: "Bosque natural",
    49: "Bosque natural",

    11: "Vegetación natural",
    12: "Vegetación natural",
    13: "Vegetación natural",
    29: "Vegetación natural",
    32: "Vegetación natural",
    50: "Vegetación natural",
    81: "Vegetación natural",
    82: "Vegetación natural",

    9: "Uso productivo",
    21: "Uso productivo",
    74: "Uso productivo",

    35: "Palma aceitera", 

    23: "Área transformada",
    24: "Área transformada",
    25: "Área transformada",
    30: "Área transformada",
    68: "Área transformada",
    75: "Área transformada",

    31: "Agua",
    33: "Agua",
    34: "Agua",

    27: "Sin información"

}

gdf["categoria_cobertura"] = (
    gdf["codigo_cobertura"]
    .map(CATEGORIAS)
)

print()

print(gdf["clase_cobertura"].value_counts())

print()

print(gdf["categoria_cobertura"].value_counts())

# ============================================================
# Distancia a la alerta GLAD más cercana
# ============================================================

print("Leyendo alertas GLAD...")

glad_lista = []

for archivo in sorted(GLAD_FOLDER.rglob("*.shp")):

    print(f"  • {archivo.name}")

    temp = gpd.read_file(archivo)

    temp = temp.to_crs(9377)

    glad_lista.append(temp)

glad = pd.concat(glad_lista, ignore_index=True)

glad = gpd.GeoDataFrame(
    glad,
    geometry="geometry",
    crs=9377
)

print(f"Alertas GLAD: {len(glad):,}")

# ------------------------------------------------------------
# Renombrar campos
# ------------------------------------------------------------

glad = glad.rename(columns={
    "year": "glad_year",
    "area_ha": "glad_area_ha",
    "state": "glad_region",
    "view_date": "glad_view_date"
})

# ------------------------------------------------------------
# Ocurrencias en mismo CRS
# ------------------------------------------------------------

gdf_9377 = gdf.to_crs(9377)

print("Buscando alerta más cercana...")

nearest = gpd.sjoin_nearest(
    gdf_9377,
    glad[
        [
            "glad_year",
            "glad_area_ha",
            "glad_region",
            "glad_view_date",
            "geometry"
        ]
    ],
    how="left",
    distance_col="dist_glad_m"
)

# ------------------------------------------------------------
# Copiar atributos al GeoDataFrame original
# ------------------------------------------------------------

gdf["dist_glad_m"] = nearest["dist_glad_m"].round(1)

gdf["glad_year"] = nearest["glad_year"].astype("Int64")

gdf["glad_area_ha"] = nearest["glad_area_ha"].round(2)

gdf["glad_region"] = nearest["glad_region"]

gdf["glad_view_date"] = nearest["glad_view_date"]

# ============================================================
# Resumen
# ============================================================

print("\n===========================================")
print("Enriquecimiento GLAD")
print("===========================================")

print(f"Ocurrencias: {len(gdf):,}")

print()

print(
    gdf["dist_glad_m"]
    .describe()
)
print("\nDistancia a la alerta GLAD más cercana (m):")

print(f"Mínima : {gdf['dist_glad_m'].min():,.1f}")
print(f"Media  : {gdf['dist_glad_m'].mean():,.1f}")
print(f"Mediana: {gdf['dist_glad_m'].median():,.1f}")
print(f"Máxima : {gdf['dist_glad_m'].max():,.1f}")
print()
print()

print("Ocurrencias cerca de alertas:")

for d in [100,500,1000,5000,10000]:

    n = (gdf["dist_glad_m"] <= d).sum()

    print(f"< {d:>5} m : {n:,}")
print("Alerta más reciente:")

print(
    gdf["glad_year"]
    .value_counts(dropna=False)
    .sort_index()
)

# ============================================================
# Guardar resultados
# ============================================================

OUTPUT = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas_enriquecido.csv"
)
# ==========================================================
# Corregir codificación
# ==========================================================

# ==========================================================
# Corregir problemas de codificación
# ==========================================================

def reparar_texto(valor):

    if pd.isna(valor):
        return valor

    try:
        return valor.encode("latin1").decode("utf-8")
    except Exception:
        return valor


columnas_corregir = [
    "departamento",
    "municipio",
    "resguardo",
    "categoria_anp",
    "nombre_anp"
]

for columna in columnas_corregir:

    if columna in gdf.columns:

        gdf[columna] = gdf[columna].apply(reparar_texto)

gdf.to_csv(
    OUTPUT,
    index=False,
    encoding="utf-8-sig"
)


print()
print("===========================================")
print("Archivo guardado correctamente")
print("===========================================")
print(OUTPUT)

OUTPUT_GPKG = Path(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas_enriquecido.gpkg"
)

gdf.to_file(
    OUTPUT_GPKG,
    layer="ocurrencias",
    driver="GPKG"
)

print("GeoPackage guardado.")