from pathlib import Path
import numpy as np
import pandas as pd

# ============================================================
# Rutas
# ============================================================

ROOT = Path(__file__).resolve().parent.parent

INPUT = r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas_enriquecido.csv"
OUTPUT = r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\municipios_dataset_modelo.csv"

print("Leyendo ocurrencias...")

df = pd.read_csv(INPUT)

print(f"Ocurrencias: {len(df):,}")

# ============================================================
# Variables auxiliares
# ============================================================

df["CR"] = (df["ESTADO DE AMENAZA"] == "CR").astype(int)
df["EN"] = (df["ESTADO DE AMENAZA"] == "EN").astype(int)
df["VU"] = (df["ESTADO DE AMENAZA"] == "VU").astype(int)

# ============================================================
# Agrupar por municipio
# ============================================================

municipios = []

grupos = df.groupby(["departamento", "municipio"])

print(f"Municipios: {len(grupos):,}")

for (departamento, municipio), g in grupos:

    riqueza = g["NOMBRE CIENTIFICO"].nunique()

    especies_CR = (
        g.loc[g["ESTADO DE AMENAZA"] == "CR",
              "NOMBRE CIENTIFICO"]
        .nunique()
    )

    especies_EN = (
        g.loc[g["ESTADO DE AMENAZA"] == "EN",
              "NOMBRE CIENTIFICO"]
        .nunique()
    )

    especies_VU = (
        g.loc[g["ESTADO DE AMENAZA"] == "VU",
              "NOMBRE CIENTIFICO"]
        .nunique()
    )

    indice_amenaza = (
        especies_CR * 3 +
        especies_EN * 2 +
        especies_VU
    )

    indice_biodiversidad = (
        riqueza *
        indice_amenaza
    )

    coberturas = (
        g["clase_cobertura"]
        .value_counts(normalize=True)
    )

    pct_bosque = coberturas.get("Bosque", 0)

    pct_palma = coberturas.get("Palma aceitera", 0)

    pct_agro = coberturas.get(
        "Mosaico de agricultura o pasto",
        0
    )

    pct_otras = (
        1 -
        pct_bosque -
        pct_palma -
        pct_agro
    )

    anp = int(
        g["nombre_anp"]
        .notna()
        .any()
    )

    resguardo = int(
        g["resguardo"]
        .notna()
        .any()
    )

    dist_media = g["dist_glad_m"].mean()

    glad_presion = 1 / (dist_media + 1)

    municipios.append({

        "departamento": departamento,

        "municipio": municipio,

        "riqueza_especies": riqueza,

        "especies_CR": especies_CR,

        "especies_EN": especies_EN,

        "especies_VU": especies_VU,

        "indice_amenaza": indice_amenaza,

        "indice_biodiversidad": indice_biodiversidad,

        "pct_bosque": pct_bosque,

        "pct_palma": pct_palma,

        "pct_agro": pct_agro,

        "pct_otras": pct_otras,

        "anp": anp,

        "resguardo": resguardo,

        "dist_glad_media": dist_media,

        "glad_presion": glad_presion

    })

# ============================================================
# DataFrame final
# ============================================================

municipios = pd.DataFrame(municipios)

municipios.to_csv(
    OUTPUT,
    index=False,
    encoding="utf-8-sig"
)

print("\n========================================")
print("Dataset municipal generado")
print("========================================")

print(f"Municipios: {len(municipios):,}")

print()

print(municipios.describe())

print()

print("Archivo guardado en:")

print(OUTPUT)