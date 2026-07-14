\# Fuentes de datos



\## Introducción



El proyecto integra diferentes conjuntos de datos abiertos relacionados con biodiversidad, monitoreo ambiental y variables espaciales. Todas las fuentes utilizadas son de acceso público y fueron obtenidas a través de portales oficiales, principalmente datos.gov.co, en cumplimiento de los lineamientos del Concurso Datos al Ecosistema 2026.



Las diferentes fuentes fueron procesadas mediante scripts desarrollados en Python para construir un conjunto de datos integrado que sirvió como base para el entrenamiento del modelo de inteligencia artificial.



\---



\# 1. Especies de palmas amenazadas



La identificación de las especies de interés se realizó utilizando el conjunto de datos oficial:



\*\*Listado oficial de las especies silvestres amenazadas de la diversidad biológica colombiana continental y marino costera – Resolución 0126 de 2024\*\*



Fuente:



\- Ministerio de Ambiente y Desarrollo Sostenible (MinAmbiente)

\- Portal datos.gov.co

\- Última actualización: 18 de mayo de 2026



Este conjunto de datos contiene el listado oficial de especies silvestres clasificadas bajo alguna categoría de amenaza en Colombia, constituyendo la referencia oficial utilizada para seleccionar las especies de palmas incluidas en el proyecto.



A partir de este listado se identificaron las especies pertenecientes a la familia \*\*Arecaceae\*\*, las cuales fueron utilizadas como base para la descarga de registros de ocurrencia desde GBIF.



\---



\# 2. Registros de ocurrencia (GBIF)



Una vez identificadas las especies de palmas amenazadas, sus registros de ocurrencia fueron descargados desde el Global Biodiversity Information Facility (GBIF), la mayor infraestructura mundial de datos abiertos sobre biodiversidad.



Los registros incluyen información como:



\- nombre científico;

\- coordenadas geográficas;

\- fecha del registro;

\- municipio y departamento;

\- institución responsable;

\- tipo de registro;

\- conjunto de datos de origen.



Posteriormente los registros fueron depurados mediante Python para eliminar duplicados, corregir inconsistencias e integrar variables espaciales adicionales.



\---



\# 3. Alertas tempranas de deforestación



Para representar la dinámica histórica de pérdida de cobertura vegetal se utilizó el conjunto de datos oficial:



\*\*Monitoreo de Bosques\*\*



Fuente:



\- Instituto de Hidrología, Meteorología y Estudios Ambientales (IDEAM)

\- Portal datos.gov.co

\- Última actualización: 18 de mayo de 2026



Este conjunto de datos reúne los productos generados por el Sistema Nacional de Monitoreo de Bosques, incluyendo los boletines de detecciones tempranas de deforestación, capas geográficas y demás productos asociados al monitoreo de la cobertura de bosque natural.



Para este proyecto se utilizaron específicamente las \*\*Alertas Tempranas de Deforestación\*\* correspondientes al período \*\*2017–2025\*\*, organizadas por año y trimestre.



Los archivos fueron procesados mediante scripts desarrollados en Python para:



\- leer automáticamente todos los archivos disponibles;

\- consolidar la información espacial;

\- asignar cada alerta al municipio correspondiente mediante análisis espacial;

\- calcular el número anual de alertas para cada municipio.



Esta serie histórica constituye la principal variable utilizada para el entrenamiento del modelo de aprendizaje automático.



\---



\# 4. División político-administrativa



Para integrar la información espacial se utilizó la capa de municipios de Colombia, empleando el campo \*\*LEVEL\_3\*\* como identificador municipal.



Esta capa permitió:



\- asignar registros biológicos a municipios;

\- contabilizar alertas de deforestación;

\- consolidar todas las variables en una única unidad de análisis.



\---



\# 5. Cobertura del suelo



Cada registro biológico fue enriquecido espacialmente mediante la incorporación de información de cobertura del suelo de MapBiomas Colombia.



A partir de esta información se calcularon variables municipales relacionadas con la proporción de registros ubicados sobre:



\- Bosque natural.

\- Uso productivo.



Estas variables fueron utilizadas posteriormente como variables predictoras dentro del modelo de inteligencia artificial.



\---



\# 6. Recursos visuales



Con el propósito de enriquecer el geovisor desarrollado como producto final del proyecto, se implementó un proceso automatizado para obtener imágenes representativas de las especies de palmas amenazadas.



Mediante scripts desarrollados en Python se consultó la API pública de \*\*iNaturalist\*\*, descargando automáticamente fotografías asociadas a las especies presentes en el análisis.



Estas imágenes fueron incorporadas al geovisor para facilitar la interpretación de la información y complementar la visualización de las especies por parte de los usuarios.



\---



\# 7. Integración de las fuentes



Las diferentes fuentes fueron integradas mediante un flujo de procesamiento desarrollado completamente en Python.



El proceso general consistió en:



1\. Identificación de las especies de palmas amenazadas a partir del listado oficial del Ministerio de Ambiente.

2\. Descarga de registros de ocurrencia desde GBIF.

3\. Depuración y control de calidad de los registros biológicos.

4\. Descarga y procesamiento de las Alertas Tempranas de Deforestación del IDEAM (2017–2025).

5\. Integración espacial con la división político-administrativa.

6\. Cálculo de variables municipales derivadas.

7\. Construcción del conjunto de datos para el modelo de aprendizaje automático.

8\. Generación de productos cartográficos y del geovisor interactivo.



\---



\# 8. Consideraciones sobre calidad de los datos



Durante la preparación de la información se implementaron diferentes procedimientos de control de calidad, entre ellos:



\- eliminación de registros biológicos duplicados;

\- estandarización de nombres de municipios;

\- verificación de geometrías válidas;

\- homologación de sistemas de referencia espacial;

\- control de codificación de caracteres especiales;

\- integración espacial mediante análisis geográfico.



Los registros provenientes de GBIF pueden presentar sesgos asociados al esfuerzo de muestreo y a la distribución desigual de las observaciones. Por su parte, las Alertas Tempranas de Deforestación del IDEAM corresponden a productos derivados de sensores remotos que, de acuerdo con las condiciones de uso publicadas por la entidad, constituyen información preliminar destinada al monitoreo y apoyo a la gestión del territorio.



A pesar de estas limitaciones, ambas fuentes corresponden a conjuntos de datos abiertos ampliamente utilizados en investigación ambiental y constituyen una base sólida para el desarrollo del presente proyecto.

