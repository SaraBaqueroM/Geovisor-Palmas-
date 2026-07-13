"""
===========================================================================
05_generar_metricas_especies.py
---------------------------------------------------------------------------

Genera un dataset resumen con métricas por especie a partir de las
ocurrencias descargadas desde GBIF.

Entrada:
    data/processed/palmas_ocurrencias_limpio.csv

Salida:
    data/processed/palmas_metricas_especies.csv

Autor: Santiago Baquero
Proyecto: Concurso Datos al Ecosistema 2026
===========================================================================
"""

import pandas as pd
from pathlib import Path

# -------------------------------------------------------------------------
# Rutas
# -------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT = Path(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas_clean.csv")
OUTPUT = Path(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\metricas_por_especie.csv")

# -------------------------------------------------------------------------
# Leer datos
# -------------------------------------------------------------------------

print("Leyendo ocurrencias...")

df = pd.read_csv(INPUT)

print(f"Registros leídos: {len(df):,}")

# -------------------------------------------------------------------------
# Función resumen por especie
# -------------------------------------------------------------------------

def resumir(grupo):

    return pd.Series({

        # Información taxonómica
        "nombre_vernaculo":
            grupo["NOMBRE VERNACULO"].dropna().iloc[0]
            if grupo["NOMBRE VERNACULO"].notna().any()
            else None,

        "genero":
            grupo["GENERO"].iloc[0],

        "familia":
            grupo["FAMILIA"].iloc[0],

        "estado_amenaza":
            grupo["ESTADO DE AMENAZA"].iloc[0],

        # Ocurrencias
        "total_ocurrencias":
            len(grupo),

        "primer_registro":
            grupo["year"].min(),

        "ultimo_registro":
            grupo["year"].max(),

        "años_monitoreados":
            grupo["year"].max() - grupo["year"].min(),

        "edad_ultimo_registro":
            2026 - grupo["year"].max(),

        # Registros recientes
        "registros_recientes":
            grupo["registro_reciente"].sum(),

        "porcentaje_recientes":
            round(grupo["registro_reciente"].mean() * 100, 2),

        # Distribución
        "departamentos":
            grupo["stateProvince"].nunique(),

        "municipios":
            grupo["municipality"].nunique(),

        # Información disponible
        "instituciones":
            grupo["institutionCode"].nunique(),

        "datasets":
            grupo["datasetName"].nunique(),

        # Calidad
        "posibles_duplicados":
            grupo["duplicado_coordenada_fecha"].sum(),

        "porcentaje_duplicados":
            round(grupo["duplicado_coordenada_fecha"].mean() * 100, 2),

        # Ciencia ciudadana
        "registros_inaturalist":
            (grupo["institutionCode"] == "iNaturalist").sum(),

        "porcentaje_inaturalist":
            round((grupo["institutionCode"] == "iNaturalist").mean() * 100, 2),

        # Tipo de registro
        "human_observation":
            (grupo["basisOfRecord"] == "HUMAN_OBSERVATION").sum(),

        "preserved_specimen":
            (grupo["basisOfRecord"] == "PRESERVED_SPECIMEN").sum(),

        "living_specimen":
            (grupo["basisOfRecord"] == "LIVING_SPECIMEN").sum(),

        "machine_observation":
            (grupo["basisOfRecord"] == "MACHINE_OBSERVATION").sum(),

    })

# -------------------------------------------------------------------------
# Generar métricas
# -------------------------------------------------------------------------

print("Calculando métricas por especie...")

metricas = (
    df
    .groupby("NOMBRE CIENTIFICO")
    .apply(resumir)
    .reset_index()
)

# -------------------------------------------------------------------------
# Ordenar
# -------------------------------------------------------------------------
columnas_enteras = [
    "total_ocurrencias",
    "primer_registro",
    "ultimo_registro",
    "años_monitoreados",
    "edad_ultimo_registro",
    "registros_recientes",
    "departamentos",
    "municipios",
    "instituciones",
    "datasets",
    "posibles_duplicados",
    "registros_inaturalist",
    "human_observation",
    "preserved_specimen",
    "living_specimen",
    "machine_observation"
]

metricas[columnas_enteras] = (
    metricas[columnas_enteras]
    .astype("Int64")
)
metricas = metricas.sort_values(
    by="total_ocurrencias",
    ascending=False
)

# -------------------------------------------------------------------------
# Guardar
# -------------------------------------------------------------------------

metricas.to_csv(OUTPUT, index=False)

# -------------------------------------------------------------------------
# Resumen
# -------------------------------------------------------------------------

print("\n========================================")
print(" MÉTRICAS GENERADAS")
print("========================================")

print(f"Especies: {len(metricas)}")
print(f"Archivo: {OUTPUT}")

print("\nTop 10 especies por número de ocurrencias:\n")

print(
    metricas[
        ["NOMBRE CIENTIFICO",
         "estado_amenaza",
         "total_ocurrencias"]
    ].head(10)
)

print("\nProceso finalizado correctamente.")