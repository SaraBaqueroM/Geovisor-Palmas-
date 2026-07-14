# \# Identificación de municipios prioritarios para la conservación de palmas amenazadas mediante inteligencia artificial y datos abiertos en Colombia

# 

## <p align="center">

## &#x20; <img src="RECURSOS/portada.png" width="900">

## </p>





# \## Concurso Datos al Ecosistema 2026

# 

# Este proyecto integra datos abiertos de biodiversidad y monitoreo ambiental para identificar municipios con mayor riesgo de generación de alertas de deforestación y analizar su relación con la presencia de palmas amenazadas en Colombia.

# 

# El flujo de trabajo combina registros de ocurrencia de especies, alertas históricas de deforestación, análisis espacial e inteligencia artificial para generar productos reproducibles que apoyen procesos de priorización territorial para la conservación.

# 

# \---

# 

# \# Objetivo

# 

# Desarrollar un modelo basado en inteligencia artificial que integre registros de ocurrencia de palmas amenazadas y alertas históricas de deforestación para identificar municipios con mayor riesgo de transformación del territorio.

# 

# \---

# 

# \# Problema abordado

# 

# Aunque Colombia dispone de grandes volúmenes de datos abiertos sobre biodiversidad y monitoreo ambiental, estas fuentes normalmente son utilizadas de manera independiente.

# 

# Este proyecto demuestra cómo integrar información proveniente de diferentes entidades para generar conocimiento útil sobre la relación entre biodiversidad amenazada y presión por deforestación.

# 

# \---

# 

# \# Fuentes de datos

# 

# El proyecto integra información proveniente de:

# 

# \- Datos Abiertos Colombia (datos.gov.co)

# &#x20; - Listado oficial de especies amenazadas (Resolución 0126 de 2024)

# &#x20; - Monitoreo de Bosques - IDEAM

# \- GBIF (Global Biodiversity Information Facility)

# \- iNaturalist

# \- Límites administrativos de Colombia

# 

# \---

# 

# \# Metodología

# 

# La metodología fue desarrollada siguiendo los principios de CRISP-ML e incluyó las siguientes etapas:

# 

# 1\. Selección de especies de palmas amenazadas.

# 2\. Descarga de registros de ocurrencia desde GBIF.

# 3\. Descarga automatizada de fotografías desde iNaturalist mediante Python.

# 4\. Procesamiento de alertas tempranas de deforestación del IDEAM (2017–2025).

# 5\. Integración espacial de todas las fuentes de información.

# 6\. Construcción de variables municipales.

# 7\. Entrenamiento de un modelo Random Forest.

# 8\. Predicción del riesgo de generación de alertas para 2026.

# 9\. Publicación de un geovisor web mediante GitHub Pages.

# 

# \---

# 

# \# Resultados

# 

# El proyecto generó:

# 

# \- Dataset consolidado para modelado.

# \- Variables espaciales por municipio.

# \- Modelo predictivo Random Forest.

# \- Predicción municipal del riesgo de generación de alertas de deforestación.

# \- Capas geográficas en formato GeoPackage y GeoJSON.

# \- Geovisor interactivo.

# \- Documentación técnica completamente reproducible.

# 

# \---

# 

# \# Tecnologías utilizadas

# 

# \- Python

# \- Pandas

# \- GeoPandas

# \- Scikit-learn

# \- Matplotlib

# \- QGIS

# \- Git

# \- GitHub

# \- GitHub Pages

# 

# \---

# 

# \# Estructura del repositorio

# 

# ```

# .

# ├── README.md

# ├── LICENSE

# ├── requirements.txt

# ├── environment.yml

# ├── docs/

# ├── Scripts/

# ├── data/

# ├── Output\_analisis/

# ├── Geovisor/

# └── RECURSOS/

# ```

# 

# \---

# 

# \# Documentación

# 

# La documentación técnica del proyecto se encuentra en la carpeta `docs/` e incluye:

# 

# \- Planteamiento del problema

# \- Fuentes de datos

# \- Marco metodológico

# \- Arquitectura

# \- Diccionario de datos

# \- Resultados

# \- Limitaciones

# \- Trabajo futuro

# \- Referencias

# 

# \---

# 

# \# Geovisor

# 

# El proyecto incluye un geovisor web desarrollado con Leaflet y publicado mediante GitHub Pages.

# 

# En él es posible explorar:

# 

# \- Distribución de registros de palmas amenazadas.

# \- Fotografías de las especies.

# \- Municipios con registros de ocurrencia.

# \- Riesgo predicho de generación de alertas de deforestación.

# \- Información espacial utilizada por el modelo.

# 

# \*\*Enlace al geovisor:\*\*

# 

# \*(Agregar aquí la URL de GitHub Pages cuando el repositorio sea publicado.)\*

# 

# \---

# 

# \# Reproducibilidad

# 

# Todo el flujo de trabajo fue implementado mediante scripts en Python.

# 

# A partir de los datos abiertos utilizados es posible reproducir completamente:

# 

# \- descarga de información;

# \- procesamiento de registros;

# \- análisis espacial;

# \- entrenamiento del modelo;

# \- generación de productos cartográficos;

# \- construcción del geovisor.

# 

# \---

# 

# \# Autores

# 

# \*\*Santiago Baquero\*\*

# 

# Universidad Nacional de Colombia

# 

# Fundación Gaia Amazonas

# 

# \*\*Sara Yineth Baquero\*\*





# Universidad Distrital Francisco José de Caldas





# Fundación Gaia Amazonas





# 

# \---

# 

# \## Licencia

# 

# Este proyecto se distribuye bajo la licencia incluida en el archivo `LICENSE`.

# 

# \---

# 

# \## Agradecimientos

# 

# Agradecemos a las entidades que promueven el acceso abierto a la información ambiental y de biodiversidad, especialmente al Ministerio de Ambiente y Desarrollo Sostenible, al IDEAM, GBIF, iNaturalist y Datos Abiertos Colombia, por facilitar el desarrollo de proyectos reproducibles de ciencia de datos para la conservación de la biodiversidad.

