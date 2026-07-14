\# Limitaciones



\## Introducción



Los resultados obtenidos en este proyecto deben interpretarse considerando las características y limitaciones propias de las fuentes de información utilizadas, así como de la metodología implementada. Aunque el modelo desarrollado proporciona una aproximación útil para identificar municipios con mayor riesgo de generación de alertas de deforestación y su posible relación con la presencia de palmas amenazadas, no constituye una representación absoluta de la realidad ni reemplaza estudios ecológicos o evaluaciones de campo.



\---



\# 1. Registros de biodiversidad



Los registros de ocurrencia obtenidos desde GBIF presentan limitaciones inherentes a los datos de biodiversidad de acceso abierto.



Entre ellas se encuentran:



\- distribución espacial desigual del esfuerzo de muestreo;

\- diferencias en la precisión de las coordenadas geográficas;

\- variación en la calidad de los registros según la institución que los reporta;

\- ausencia de registros en zonas con baja intensidad de investigación.



Por esta razón, la ausencia de registros en un municipio no implica necesariamente la ausencia de especies de palmas amenazadas.



\---



\# 2. Alertas tempranas de deforestación



El modelo utiliza como fuente principal las Alertas Tempranas de Deforestación del IDEAM correspondientes al período 2017–2025.



Estas alertas representan un sistema de monitoreo basado en sensores remotos y constituyen una aproximación temprana a posibles eventos de pérdida de cobertura vegetal.



De acuerdo con las condiciones de uso publicadas por el IDEAM, estos productos corresponden a información destinada al monitoreo ambiental y pueden contener incertidumbres propias del procesamiento de imágenes satelitales.



En consecuencia, las alertas utilizadas en este proyecto no deben interpretarse como una cuantificación definitiva de la deforestación ocurrida.



\---



\# 3. Variables utilizadas



El modelo fue construido utilizando un conjunto limitado de variables derivadas de la información disponible.



Entre ellas se incluyen:



\- riqueza de especies de palmas amenazadas;

\- proporción de registros sobre bosque natural;

\- proporción de registros sobre uso productivo;

\- historial municipal de alertas de deforestación.



No se incorporaron variables adicionales que podrían influir sobre la dinámica de la deforestación, tales como:



\- variables climáticas;

\- elevación y pendiente;

\- accesibilidad;

\- infraestructura vial;

\- actividades productivas;

\- características socioeconómicas;

\- presencia de áreas protegidas;

\- conflictos de uso del suelo.



La incorporación de estas variables podría mejorar la capacidad predictiva del modelo.



\---



\# 4. Modelo de aprendizaje automático



El modelo Random Forest identifica relaciones estadísticas presentes en los datos históricos disponibles.



Sin embargo, las predicciones obtenidas corresponden a estimaciones basadas en patrones observados entre 2017 y 2025.



Eventos extraordinarios, cambios en las políticas públicas, fenómenos ambientales futuros pueden alterar significativamente estos patrones y afectar la capacidad predictiva del modelo.



En consecuencia, las predicciones deben interpretarse como escenarios de riesgo y no como una predicción exacta del comportamiento futuro de la deforestación.



\---



\# 5. Escala de análisis



El análisis fue desarrollado utilizando el municipio como unidad espacial.



Esta decisión facilita la integración de múltiples fuentes de información y la comunicación de los resultados, pero implica una pérdida de detalle espacial.



Dentro de un mismo municipio pueden coexistir zonas con condiciones ecológicas y niveles de presión muy diferentes, las cuales no pueden ser diferenciadas mediante un análisis agregado a escala municipal.



\---



\# 6. Alcance de los resultados



El modelo predice el número esperado de alertas tempranas de deforestación para cada municipio, utilizando como referencia el comportamiento histórico observado.



Por lo tanto, los resultados no representan una predicción directa sobre la pérdida de individuos o poblaciones de palmas amenazadas, sino una aproximación al contexto territorial en el que estas especies podrían enfrentar mayores presiones derivadas de la transformación del paisaje.



La interpretación de los resultados debe realizarse en conjunto con información ecológica, inventarios de biodiversidad y conocimiento local.



\---



\# Consideraciones finales



A pesar de estas limitaciones, el proyecto demuestra el potencial de integrar datos abiertos, análisis espacial e inteligencia artificial para generar herramientas de apoyo a la toma de decisiones en conservación.



La metodología desarrollada es reproducible, escalable y puede fortalecerse mediante la incorporación de nuevas fuentes de información y la actualización periódica de los datos utilizados, contribuyendo a mejorar la identificación de territorios prioritarios para la protección de la biodiversidad en Colombia.

