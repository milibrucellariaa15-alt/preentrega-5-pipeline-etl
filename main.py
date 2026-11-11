
from src.pipeline import ejecutar_pipeline


if __name__ == "__main__":
    ejecutar_pipeline(
        ruta_entrada="data/dataset.csv",
        ruta_salida="output/datos_procesados.parquet"
    )
