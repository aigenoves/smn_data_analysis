import re
import pandas as pd
from pathlib import Path

# Definir la regex
pattern = re.compile(
    r"(\d{8})\s+(\d+)\s+([\d.]+)\s+(\d+)\s+([\d.]+)\s+(\d+)\s+([\d.]+)\s+(.+)"
)


def daily_data_parser(data_dir: str, output_csv: str) -> None:
    """
    Recorre todas las carpetas en la ruta dada, parsea los archivos de texto usando regex y
    genera un único archivo CSV de salida.

    :param data_dir: Ruta al directorio base (por ejemplo, "data").
    :param output_csv: Nombre del archivo CSV a generar.
    """
    daily_data_dir = Path(data_dir)
    all_data = []

    # Recorrer todas las subcarpetas y archivos .txt en el directorio
    for txt_file in daily_data_dir.rglob("*.txt"):
        # Parsear cada archivo
        print(f"Procesando archivo {txt_file}")
        with open(txt_file, "r", encoding="latin-1") as file:
            for line in file:
                # Aplicar la regex a cada línea
                match = pattern.match(line)
                if match:
                    # Extraer los grupos de la regex
                    date = match.group(1)  # Fecha en formato DDMMYYYY
                    hour = match.group(2)  # Hora
                    temperature = match.group(3)  # Temperatura
                    humidity = match.group(4)  # Humedad
                    pressure = match.group(5)  # Presión
                    wind_dir = match.group(6)  # Direccion del viento
                    wind_vel = match.group(7)  # Velocidad del viento
                    location = match.group(8)  # Ubicación

                    # Agregar los datos parseados a la lista
                    all_data.append(
                        [
                            date,
                            hour,
                            temperature,
                            humidity,
                            pressure,
                            wind_dir,
                            wind_vel,
                            location,
                        ]
                    )

    # Crear un DataFrame de Pandas con todos los datos
    df = pd.DataFrame(
        all_data,
        columns=[
            "fecha",
            "hora",
            "temperatura",
            "humedad",
            "presion",
            "viento_d",
            "viento_v",
            "ubicacion",
        ],
    )

    # Guardar todo en un único archivo CSV
    df.to_csv(output_csv, index=False)
    print(f"Archivo CSV generado en {output_csv}.")
