\# Arquitectura del proyecto



\## Descripción general



El proyecto integra múltiples fuentes de datos abiertos de biodiversidad y monitoreo ambiental para construir un modelo de inteligencia artificial capaz de identificar municipios con mayor riesgo de generación de alertas de deforestación y analizar su relación con la presencia de palmas amenazadas en Colombia.



Toda la metodología fue desarrollada utilizando herramientas de código abierto y un flujo de procesamiento reproducible implementado principalmente en Python.



\---



\# Arquitectura general



El flujo de trabajo del proyecto se divide en seis etapas principales:



```

\&#x20;                 DATOS ABIERTOS

\&#x20;                        │

\&#x20;       ┌────────────────┼────────────────┐

\&#x20;       │                │                │

\&#x20;       │                │                │

\&#x20;  Datos.gov.co       GBIF         iNaturalist

\&#x20;       │                │                │

\&#x20;       │                │                │

\&#x20;Especies amenazadas  Registros      Fotografías

\&#x20;  de palmas         de ocurrencia    de especies

\&#x20;       │                │

\&#x20;       └────────────┬───┘

\&#x20;                    │

\&#x20;            Preparación de datos

\&#x20;                    │

\&#x20;     Limpieza, depuración y validación

\&#x20;                    │

\&#x20;     Integración de variables espaciales

\&#x20;                    │

\&#x20;         Ingeniería de características

\&#x20;                    │

\&#x20;     Variables por municipio

\&#x20;                    │

\&#x20;       Modelo Random Forest

\&#x20;                    │

\&#x20;Predicción del riesgo de alertas 2026

\&#x20;                    │

\&#x20;         Exportación de resultados

\&#x20;                    │

\&#x20;       GeoPackage + GitHub Pages

\&#x20;                    │

\&#x20;                Geovisor web

```



\---



\# Componentes del proyecto



\## 1. Datos de biodiversidad



Se utilizaron registros de ocurrencia de especies de palmas amenazadas descargados desde GBIF.



Los registros fueron filtrados utilizando el listado oficial de especies amenazadas de Colombia (Resolución 0126 de 2024), obteniendo únicamente las especies pertenecientes a la familia Arecaceae incluidas en alguna categoría de amenaza.



Posteriormente se realizó un proceso de limpieza y depuración para eliminar registros duplicados y estandarizar la información espacial.



\---



\## 2. Fotografías de especies



Las imágenes utilizadas para ilustrar las fichas de especies del geovisor fueron descargadas automáticamente mediante scripts desarrollados en Python a partir de observaciones públicas disponibles en la plataforma iNaturalist.



Este componente complementa la información biológica presentada al usuario final.



\---



\## 3. Alertas de deforestación



Se utilizaron las Alertas Tempranas de Deforestación publicadas por el IDEAM para el período 2017–2025.



Los archivos fueron procesados automáticamente mediante Python para:



\- leer cada trimestre;

\- integrar los registros de cada año;

\- realizar la unión espacial con los municipios;

\- calcular el número anual de alertas por municipio;

\- construir la serie histórica utilizada por el modelo.



\---



\## 4. Ingeniería de variables



A partir de los registros de biodiversidad y de las alertas históricas se construyó un conjunto de variables predictoras, entre ellas:



\- riqueza de especies de palmas;

\- porcentaje de registros en bosque natural;

\- porcentaje de registros en uso productivo;

\- número de alertas anuales de deforestación (2017–2024).



Estas variables fueron consolidadas en un único conjunto de datos para el entrenamiento del modelo.



\---



\## 5. Modelo de inteligencia artificial



Se implementó un modelo Random Forest Regressor utilizando la biblioteca Scikit-learn.



El modelo fue entrenado para estimar el número esperado de alertas de deforestación durante 2026 utilizando como referencia el comportamiento histórico observado entre 2017 y 2025 y las variables derivadas de los registros de biodiversidad.



Posteriormente se calcularon métricas de desempeño e importancia de variables para evaluar el comportamiento del modelo.



\---



\## 6. Productos finales



Los resultados generados por el proyecto incluyen:



\- conjunto de datos consolidado para entrenamiento;

\- modelo predictivo de riesgo;

\- predicción municipal de alertas para 2026;

\- capas geográficas en formato GeoPackage;

\- gráficos de importancia de variables;

\- geovisor web publicado mediante GitHub Pages;

\- documentación técnica completamente reproducible en GitHub.



\---



\# Tecnologías utilizadas



El proyecto fue desarrollado utilizando herramientas de código abierto:



\- Python

\- Pandas

\- GeoPandas

\- Scikit-learn

\- Matplotlib

\- QGIS

\- Git

\- GitHub

\- GitHub Pages



\---



\# Reproducibilidad



Todos los procesos de descarga, integración, limpieza, análisis espacial, modelado y generación de productos fueron implementados mediante scripts en Python, permitiendo reproducir completamente el flujo de trabajo a partir de los datos abiertos utilizados en el proyecto.



La organización del repositorio facilita la actualización futura de la información y la reutilización de la metodología para otros grupos biológicos o nuevas versiones de los datos.

