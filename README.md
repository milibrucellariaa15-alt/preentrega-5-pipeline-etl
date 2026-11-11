# Pipeline ETL - Ausentismo Laboral

## Objetivo

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) utilizando Python y Pandas para automatizar el procesamiento de un dataset de ausentismo laboral.

El pipeline permite extraer los datos desde un archivo CSV, aplicar reglas de limpieza y transformación y almacenar el resultado en formato Parquet.

## Estructura del proyecto

preentrega-5-pipeline-etl/
- main.py
- requirements.txt
- README.md
- .gitignore
- src/
  - pipeline.py
- data/
- output/

## Etapas del pipeline

### 1. Extracción

El archivo CSV es leído utilizando Pandas. Durante el procesamiento se optimizan los tipos de datos numéricos para reducir el uso de memoria.

### 2. Transformación

La etapa de transformación realiza las siguientes tareas:

- Normalización de nombres de columnas.
- Conversión de la variable de fecha.
- Eliminación de registros duplicados.
- Tratamiento de posibles valores nulos.
- Optimización de tipos numéricos.

Para posibles valores faltantes en variables numéricas se utiliza la mediana, debido a que es menos sensible a valores extremos que la media.

Aunque el dataset utilizado actualmente no presenta valores nulos, esta lógica se incorpora para que el pipeline pueda manejar futuros archivos que sí los contengan.

### 3. Carga

Los datos procesados se exportan en formato Parquet.

Parquet utiliza almacenamiento columnar, permite una buena compresión, conserva los tipos de datos y facilita el acceso eficiente a las columnas. Estas características lo hacen adecuado para procesos de análisis de datos y Machine Learning.

## Instalación

Clonar el repositorio e instalar las dependencias con el siguiente comando:

    pip install -r requirements.txt

## Ejecución

El archivo CSV de entrada debe ubicarse en:

    data/dataset.csv

Para ejecutar el pipeline:

    python main.py

El resultado será generado automáticamente en:

    output/datos_procesados.parquet

## Dependencias

- pandas
- pyarrow

## Resultado obtenido

El dataset original utilizado contiene 700 registros y 12 variables.

Durante la transformación se eliminaron 8 registros duplicados, obteniendo un dataset procesado final de 692 registros y 12 variables.

La validación final confirmó que el resultado no contiene registros duplicados ni valores nulos.

## Buenas prácticas

Se utiliza un archivo .gitignore para evitar incluir en el repositorio el dataset original, los archivos generados por el pipeline, archivos temporales de Python y entornos virtuales.
