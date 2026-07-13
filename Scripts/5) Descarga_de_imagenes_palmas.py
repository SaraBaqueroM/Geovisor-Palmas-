"""
04_descargar_imagenes_inaturalist.py

Descarga imágenes desde iNaturalist para cada especie
de palmas amenazadas de Colombia.

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

CSV = r"C:\Users\User\Documents\Datos IA al ecosistema\Palmas\palmas.csv"   

CARPETA_SALIDA = r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\Imagenes iNaturalist Palmas"

N_IMAGENES = 5

QUALITY = "research"

PAUSA = 1       # segundos entre consultas

# ==========================================================

os.makedirs(CARPETA_SALIDA, exist_ok=True)

df = pd.read_csv(CSV)

especies = sorted(df["NOMBRE CIENTIFICO"].dropna().unique())

print("="*60)
print("DESCARGA DE IMÁGENES DESDE INATURALIST")
print("="*60)
print(f"Especies encontradas: {len(especies)}")
print()

metadata_general = []

# ==========================================================

for especie in tqdm(especies):

    nombre_carpeta = especie.replace(" ", "_")

    carpeta = os.path.join(
        CARPETA_SALIDA,
        nombre_carpeta
    )

    os.makedirs(carpeta, exist_ok=True)

    metadata_especie = []

    try:

        respuesta = requests.get(

            "https://api.inaturalist.org/v1/observations",

            params={

                "taxon_name": especie,

                "photos": "true",

                "quality_grade": QUALITY,

                "per_page": 30

            },

            timeout=30

        )

        respuesta.raise_for_status()

        resultados = respuesta.json()["results"]

        contador = 0

        for observacion in resultados:

            if contador >= N_IMAGENES:
                break

            fotos = observacion.get("photos", [])

            if len(fotos) == 0:
                continue

            foto = fotos[0]

            url = foto["url"].replace("square", "large")

            obs_id = observacion["id"]

            nombre_archivo = f"obs_{obs_id}.jpg"

            ruta_imagen = os.path.join(
                carpeta,
                nombre_archivo
            )

            if os.path.exists(ruta_imagen):
                contador += 1
                continue

            try:

                imagen = requests.get(
                    url,
                    timeout=30
                )

                imagen.raise_for_status()

                with open(ruta_imagen, "wb") as f:
                    f.write(imagen.content)

                fila = {

                    "species": especie,

                    "archivo": nombre_archivo,

                    "ruta": ruta_imagen,

                    "observacion_id": obs_id,

                    "usuario": observacion["user"]["login"],

                    "fecha": observacion.get("observed_on"),

                    "licencia": foto.get("license_code"),

                    "atribucion": foto.get("attribution"),

                    "url_imagen": url,

                    "url_observacion":
                        f"https://www.inaturalist.org/observations/{obs_id}"

                }

                metadata_especie.append(fila)

                metadata_general.append(fila)

                contador += 1

            except Exception:

                continue

        # ------------------------------------------
        # Guardar metadata de la especie
        # ------------------------------------------

        if len(metadata_especie) > 0:

            pd.DataFrame(metadata_especie).to_csv(

                os.path.join(
                    carpeta,
                    "metadata.csv"
                ),

                index=False,

                encoding="utf-8-sig"

            )

    except Exception as e:

        print(f"\nError con {especie}")

        print(e)

    time.sleep(PAUSA)

# ==========================================================
# Guardar metadata general
# ==========================================================

pd.DataFrame(metadata_general).to_csv(

    os.path.join(
        CARPETA_SALIDA,
        "metadata_general.csv"
    ),

    index=False,

    encoding="utf-8-sig"

)

print()
print("="*60)
print("DESCARGA FINALIZADA")
print("="*60)
print(f"Especies procesadas : {len(especies)}")
print(f"Imágenes descargadas: {len(metadata_general)}")
print("="*60)