"""
-------------------------------------------------------
06_limpiar_ocurrencias.py

Limpieza de registros de ocurrencia descargados desde GBIF
para las especies de palmas amenazadas de Colombia.

Autor: Santiago Baquero
Proyecto: Datos al Ecosistema 2026
-------------------------------------------------------
"""

import pandas as pd
from pathlib import Path

# ======================================================
# RUTAS
# ======================================================

INPUT = Path(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas.csv")
OUTPUT = Path(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas_clean.csv")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

# ======================================================
# CARGAR DATOS
# ======================================================

print("Cargando datos...")

df = pd.read_csv(INPUT)

print(f"Registros originales: {len(df):,}")

# ======================================================
# LIMPIEZA BÁSICA
# ======================================================

# Eliminar filas sin especie
df = df[df["species"].notna()]

# Eliminar filas sin coordenadas
df = df[df["decimalLatitude"].notna()]
df = df[df["decimalLongitude"].notna()]

# Convertir coordenadas a numéricas
df["decimalLatitude"] = pd.to_numeric(df["decimalLatitude"], errors="coerce")
df["decimalLongitude"] = pd.to_numeric(df["decimalLongitude"], errors="coerce")

# Eliminar coordenadas inválidas
df = df[df["decimalLatitude"].between(-90, 90)]
df = df[df["decimalLongitude"].between(-180, 180)]

# Eliminar coordenadas (0,0)
df = df[
    ~(
        (df["decimalLatitude"] == 0) &
        (df["decimalLongitude"] == 0)
    )
]

# Mantener únicamente Colombia
df = df[df["country"].str.upper() == "COLOMBIA"]

# ======================================================
# LIMPIEZA DE TEXTO
# ======================================================

# Quitar espacios sobrantes
columnas_texto = [
    "species",
    "scientificName",
    "stateProvince",
    "municipality",
    "locality",
    "institutionCode",
    "datasetName"
]

for c in columnas_texto:
    if c in df.columns:
        df[c] = df[c].astype(str).str.strip()

# ======================================================
# FECHAS
# ======================================================

df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
df["month"] = pd.to_numeric(df["month"], errors="coerce").astype("Int64")

# ======================================================
# CREAR VARIABLES NUEVAS
# ======================================================

# Edad del registro
df["edad_registro"] = (2026 - df["year"]).astype("Int64")

# Década
df["decada"] = ((df["year"] // 10) * 10).astype("Int64")

# Registro reciente (<10 años)
df["registro_reciente"] = df["edad_registro"] <= 20

# Fuente ciudadana
df["fuente_ciudadana"] = (
    df["institutionCode"]
    .fillna("")
    .str.contains("iNaturalist", case=False)
)

# ======================================================
# MARCAR POSIBLES DUPLICADOS
# ======================================================

duplicados = [
    "species",
    "decimalLatitude",
    "decimalLongitude",
    "eventDate"
]

df["duplicado_coordenada_fecha"] = df.duplicated(
    subset=duplicados,
    keep=False
)

# ======================================================
# GUARDAR
# ======================================================

df.to_csv(OUTPUT, index=False)

print("\nLimpieza finalizada")

print(f"Registros finales: {len(df):,}")

print(f"Posibles duplicados: {df['duplicado_coordenada_fecha'].sum():,}")

print(f"Archivo guardado en:\n{OUTPUT}")