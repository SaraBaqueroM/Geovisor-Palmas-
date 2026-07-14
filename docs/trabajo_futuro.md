\# Trabajo futuro



\## Introducción



El presente proyecto constituye una primera aproximación para integrar información de biodiversidad, monitoreo forestal e inteligencia artificial con el fin de identificar territorios prioritarios para la conservación de palmas amenazadas en Colombia.



La metodología desarrollada es flexible y puede ampliarse mediante la incorporación de nuevas fuentes de información, variables ambientales y técnicas de modelado que permitan mejorar la capacidad predictiva y el alcance de los análisis.



\---



\# 1. Incorporación de nuevas variables



Una de las principales oportunidades de mejora consiste en ampliar el conjunto de variables utilizadas por el modelo.



Entre las variables que podrían incorporarse se encuentran:



\- variables bioclimáticas (temperatura y precipitación);

\- elevación y pendiente;

\- distancia a carreteras y centros poblados;

\- distancia a áreas protegidas;

\- territorios indígenas y comunidades locales;

\- cambios históricos en coberturas de la tierra;

\- incendios forestales;

\- actividades mineras;

\- infraestructura vial;

\- información socioeconómica y demográfica.



La incorporación de estas variables permitiría representar con mayor detalle los factores que influyen sobre la pérdida de cobertura vegetal.



\---



\# 2. Mejoramiento del modelo de inteligencia artificial



El modelo Random Forest presentó un desempeño satisfactorio para los objetivos del proyecto; sin embargo, futuras investigaciones podrían evaluar otros algoritmos de aprendizaje automático, tales como:



\- XGBoost;

\- LightGBM;

\- CatBoost;

\- Redes Neuronales;

\- Ensambles de modelos.



Asimismo, podrían implementarse procedimientos adicionales como:



\- optimización automática de hiperparámetros;

\- validación cruzada espacial;

\- análisis de incertidumbre;

\- comparación sistemática entre diferentes modelos predictivos.



\---



\# 3. Actualización automática de la información



El flujo de trabajo desarrollado puede automatizarse para incorporar periódicamente nuevas versiones de las bases de datos utilizadas.



En particular, sería posible automatizar:



\- descarga de nuevas alertas tempranas de deforestación del IDEAM;

\- actualización de registros de ocurrencia desde GBIF;

\- incorporación de nuevas especies incluidas en los listados oficiales de especies amenazadas;

\- reentrenamiento automático del modelo con información actualizada.



Esto permitiría mantener el sistema permanentemente actualizado sin necesidad de repetir manualmente cada etapa del procesamiento.



\---



\# 4. Ampliación a otros grupos biológicos



Aunque el presente trabajo se centró en especies de palmas amenazadas, la metodología puede adaptarse fácilmente a otros grupos taxonómicos.



Entre ellos:



\- orquídeas;

\- árboles amenazados;

\- anfibios;

\- reptiles;

\- aves;

\- mamíferos;

\- plantas endémicas;

\- especies prioritarias para programas de conservación.



De esta manera, el flujo de trabajo desarrollado podría convertirse en una herramienta de apoyo para diferentes iniciativas de monitoreo de biodiversidad.



\---



\# 5. Fortalecimiento del geovisor



El geovisor desarrollado representa una primera versión funcional de consulta de resultados.



Entre las posibles mejoras futuras se encuentran:



\- búsqueda por especie;

\- filtros dinámicos por categoría de amenaza;

\- visualización de estadísticas municipales;

\- descarga directa de datos geográficos;

\- incorporación de nuevas capas ambientales;

\- conexión con servicios geográficos en línea (WMS y WFS);

\- actualización automática de la información publicada.



Estas mejoras permitirían ampliar las posibilidades de consulta y facilitarían el uso del proyecto por parte de investigadores, autoridades ambientales y público en general.



\---



\# 6. Reproducibilidad y colaboración



El proyecto fue desarrollado utilizando herramientas y datos abiertos, favoreciendo su reproducibilidad.



Como trabajo futuro se propone fortalecer este enfoque mediante:



\- publicación de nuevas versiones del repositorio;

\- documentación continua del flujo de trabajo;

\- incorporación de pruebas automáticas para los scripts;

\- mejora de la organización del código;

\- generación de nuevas contribuciones por parte de la comunidad.



El uso de plataformas como GitHub facilita el trabajo colaborativo y permite que otros investigadores adapten la metodología a diferentes regiones, especies o problemáticas ambientales.



\---



\# Consideraciones finales



El proyecto demuestra el potencial de integrar datos abiertos, análisis espacial e inteligencia artificial para apoyar la conservación de la biodiversidad.



Las mejoras propuestas permitirán incrementar la precisión de los modelos, ampliar el número de variables consideradas y fortalecer las herramientas de visualización y consulta, consolidando una metodología escalable que pueda ser aplicada en diferentes contextos de monitoreo ambiental y toma de decisiones para la conservación.

