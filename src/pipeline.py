
from pathlib import Path
import re
import pandas as pd


def extraer_datos(ruta_entrada):
    """
    Lee el archivo CSV de entrada utilizando detección
    automática del separador.
    """

    df = pd.read_csv(
        ruta_entrada,
        sep=None,
        engine="python"
    )

    print(
        f"Extracción completada: "
        f"{df.shape[0]} filas y {df.shape[1]} columnas."
    )

    return df


def normalizar_nombre(nombre):
    """
    Normaliza los nombres de columnas utilizando
    minúsculas y guiones bajos.
    """

    nombre = nombre.strip().lower()
    nombre = re.sub(r"[^a-z0-9]+", "_", nombre)

    return nombre.strip("_")


def transformar_datos(df):
    """
    Realiza la limpieza y transformación de los datos.
    """

    df = df.copy()

    # Normalización de nombres de columnas
    df.columns = [
        normalizar_nombre(columna)
        for columna in df.columns
    ]

    # Conversión de la fecha
    df["date"] = pd.to_datetime(
        df["date"],
        format="%d/%m/%Y",
        errors="coerce"
    )

    # Eliminación de duplicados
    duplicados = df.duplicated().sum()
    df = df.drop_duplicates().copy()

    # Tratamiento de valores nulos numéricos
    columnas_numericas = df.select_dtypes(
        include="number"
    ).columns

    for columna in columnas_numericas:
        if df[columna].isna().any():
            mediana = df[columna].median()
            df[columna] = df[columna].fillna(mediana)

    # Eliminación de fechas inválidas
    fechas_invalidas = df["date"].isna().sum()

    if fechas_invalidas > 0:
        df = df.dropna(subset=["date"]).copy()

    # Optimización de tipos numéricos
    columnas_enteras = df.select_dtypes(include=["int64"]).columns
    columnas_decimales = df.select_dtypes(include=["float64"]).columns

    for columna in columnas_enteras:
        df[columna] = pd.to_numeric(
            df[columna],
            downcast="integer"
        )

    for columna in columnas_decimales:
        df[columna] = pd.to_numeric(
            df[columna],
            downcast="float"
        )

    print(f"Duplicados eliminados: {duplicados}")
    print(f"Fechas inválidas eliminadas: {fechas_invalidas}")
    print(f"Valores nulos restantes: {df.isna().sum().sum()}")

    return df


def cargar_datos(df, ruta_salida):
    """
    Guarda los datos procesados en formato Parquet.
    """

    ruta_salida = Path(ruta_salida)

    ruta_salida.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_parquet(
        ruta_salida,
        engine="pyarrow",
        index=False
    )

    print(f"Archivo Parquet generado en: {ruta_salida}")


def ejecutar_pipeline(ruta_entrada, ruta_salida):
    """
    Ejecuta las etapas de extracción,
    transformación y carga.
    """

    print("Iniciando pipeline ETL...")

    df = extraer_datos(ruta_entrada)
    df = transformar_datos(df)
    cargar_datos(df, ruta_salida)

    print("Pipeline ETL finalizado correctamente.")
