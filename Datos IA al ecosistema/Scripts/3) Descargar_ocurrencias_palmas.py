"""
02_descargar_ocurrencias.py

Descarga automáticamente las ocurrencias de todas las especies de palmas
amenazadas usando la API pública de GBIF.

Autor: Equipo Datos al Ecosistema 2026
"""

import os
import time
import requests
import pandas as pd
from tqdm import tqdm

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

INPUT_CSV = r"C:\Users\User\Documents\Datos IA al ecosistema\Palmas\palmas.csv"
OUTPUT_CSV = r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas.csv"

COUNTRY = "CO"
HAS_COORDINATE = "true"

LIMIT = 300          # máximo permitido por consulta
PAUSE = 0.25         # segundos entre consultas

# ==========================================================
# COLUMNAS DE SALIDA
# ==========================================================

COLUMNAS = [

    # Información de la especie
    "NOMBRE CIENTIFICO",
    "NOMBRE VERNACULO",
    "GENERO",
    "FAMILIA",
    "ESTADO DE AMENAZA",

    # Información GBIF
    "gbifID",
    "species",
    "scientificName",
    "decimalLatitude",
    "decimalLongitude",
    "country",
    "stateProvince",
    "municipality",
    "locality",
    "year",
    "month",
    "eventDate",
    "basisOfRecord",
    "institutionCode",
    "datasetName"
]

# ==========================================================
# FUNCIONES
# ==========================================================

def extraer_taxonkey(url):

    """
    Extrae el taxonKey desde:

    gbif.org/species/2738692
    """

    return int(url.split("/")[-1])


# ----------------------------------------------------------

def descargar_ocurrencias(taxon_key):

    """
    Descarga TODAS las ocurrencias para un taxonKey.
    """

    resultados = []

    offset = 0

    while True:

        parametros = {

            "taxon_key": taxon_key,
            "country": COUNTRY,
            "has_coordinate": HAS_COORDINATE,
            "limit": LIMIT,
            "offset": offset

        }

        respuesta = requests.get(
            "https://api.gbif.org/v1/occurrence/search",
            params=parametros,
            timeout=60
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        registros = datos["results"]

        if len(registros) == 0:
            break

        resultados.extend(registros)

        offset += LIMIT

        time.sleep(PAUSE)

    return resultados


# ==========================================================
# SCRIPT PRINCIPAL
# ==========================================================

def main():

    especies = pd.read_csv(INPUT_CSV)

    todas_ocurrencias = []

    print("\nDescargando ocurrencias desde GBIF...\n")

    for _, especie in tqdm(especies.iterrows(),
                           total=len(especies),
                           colour="green"):

        try:

            taxon_key = extraer_taxonkey(especie["IDENTIFICACION"])

            ocurrencias = descargar_ocurrencias(taxon_key)

            for occ in ocurrencias:

                fila = {

                    # Información original
                    "NOMBRE CIENTIFICO": especie["NOMBRE CIENTIFICO"],
                    "NOMBRE VERNACULO": especie["NOMBRE VERNACULO"],
                    "GENERO": especie["GENERO"],
                    "FAMILIA": especie["FAMILIA"],
                    "ESTADO DE AMENAZA": especie["ESTADO DE AMENAZA"],

                    # Información GBIF
                    "gbifID": occ.get("gbifID"),
                    "species": occ.get("species"),
                    "scientificName": occ.get("scientificName"),
                    "decimalLatitude": occ.get("decimalLatitude"),
                    "decimalLongitude": occ.get("decimalLongitude"),
                    "country": occ.get("country"),
                    "stateProvince": occ.get("stateProvince"),
                    "municipality": occ.get("municipality"),
                    "locality": occ.get("locality"),
                    "year": occ.get("year"),
                    "month": occ.get("month"),
                    "eventDate": occ.get("eventDate"),
                    "basisOfRecord": occ.get("basisOfRecord"),
                    "institutionCode": occ.get("institutionCode"),
                    "datasetName": occ.get("datasetName")

                }

                todas_ocurrencias.append(fila)

        except Exception as e:

            print(f"\n⚠ Error con {especie['NOMBRE CIENTIFICO']}")
            print(e)

    print("\nGuardando archivo...")

    df = pd.DataFrame(todas_ocurrencias)

    df = df[COLUMNAS]

    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

    df.to_csv(OUTPUT_CSV,
              index=False,
              encoding="utf-8-sig")

    print("\n------------------------------------")
    print("Proceso finalizado.")
    print(f"Ocurrencias descargadas: {len(df):,}")
    print(f"Archivo: {OUTPUT_CSV}")
    print("------------------------------------")


if __name__ == "__main__":

    main()