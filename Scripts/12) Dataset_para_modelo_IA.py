# ============================================================
# SCRIPT 12
# VARIABLES DE PALMAS POR MUNICIPIO
#
# Genera:
# - riqueza_palmas
# - bosque_pct
# - agro_pct
#
# a partir del CSV enriquecido.
# ============================================================

import pandas as pd
from pathlib import Path

# ============================================================
# RUTAS
# ============================================================

RUTA_CSV = r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas_enriquecido.csv"

OUTPUT = Path("Output_analisis")
OUTPUT.mkdir(exist_ok=True)

# ============================================================
# LEER
# ============================================================

print("Leyendo archivo...")

df = pd.read_csv(RUTA_CSV)

print(f"Registros originales: {len(df):,}")

# ============================================================
# ELIMINAR DUPLICADOS
# ============================================================

duplicados = [
    "species",
    "decimalLatitude",
    "decimalLongitude",
    "eventDate"
]

antes = len(df)

df = df.drop_duplicates(
    subset=duplicados,
    keep="first"
)

despues = len(df)

print(f"Registros originales : {antes:,}")
print(f"Registros depurados  : {despues:,}")
print(f"Duplicados eliminados: {antes-despues:,}")

# ============================================================
# LIMPIAR MUNICIPIOS
# ============================================================

df["municipio"] = (
    df["municipio"]
    .fillna("SIN INFORMACION")
    .astype(str)
    .str.strip()
)

# eliminar municipios sin información
df = df[df["municipio"] != "SIN INFORMACION"]

# ============================================================
# RIQUEZA DE ESPECIES
# ============================================================

riqueza = (
    df.groupby("municipio")["NOMBRE CIENTIFICO"]
      .nunique()
      .reset_index(name="riqueza_palmas")
)

# ============================================================
# PORCENTAJES DE COBERTURA
# ============================================================

tabla = pd.crosstab(
    df["municipio"],
    df["categoria_cobertura"],
    normalize="index"
) * 100

tabla = tabla.reset_index()

# asegurar columnas

for c in ["Bosque natural", "Uso productivo"]:

    if c not in tabla.columns:
        tabla[c] = 0

tabla = tabla.rename(columns={
    "Bosque natural": "bosque_pct",
    "Uso productivo": "agro_pct"
})

# ============================================================
# UNIR
# ============================================================

dataset = riqueza.merge(
    tabla[["municipio", "bosque_pct", "agro_pct"]],
    on="municipio",
    how="left"
)

# ============================================================
# REDONDEAR
# ============================================================

dataset["bosque_pct"] = dataset["bosque_pct"].round(2)
dataset["agro_pct"] = dataset["agro_pct"].round(2)

# ============================================================
# ORDENAR
# ============================================================

dataset = dataset.sort_values(
    "riqueza_palmas",
    ascending=False
)

# ============================================================
# EXPORTAR
# ============================================================

salida = OUTPUT / "Variables_palmas_por_municipio.csv"

dataset.to_csv(
    salida,
    index=False,
    encoding="utf-8-sig"
)

print("\n========================================")
print("VARIABLES GENERADAS")
print("========================================")

print(f"Municipios: {len(dataset)}")
print(dataset.head(20))

print(f"\nArchivo guardado en:\n{salida}")