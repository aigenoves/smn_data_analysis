import sys
from pathlib import Path
from datetime import datetime

from src.daily_data_fetcher import fetch_daily_data
from src.utils import generate_dates_until_today
from src.parser.daily_data import daily_data_parser


def main() -> None:
    # URL del archivo que deseas descargar
    main_path = Path(__file__).resolve()

    # Obtener el directorio que contiene main.py
    main_directory = main_path.parent

    # Si necesitas un path relativo a main.py, por ejemplo, a una carpeta 'data' dentro del mismo directorio
    relative_path = main_directory / "data"

    start_date = datetime(2024, 9, 12)

    dates_list = generate_dates_until_today(start_date=start_date)
    for day in dates_list:
        url: str = (
            f"https://ssl.smn.gob.ar/dpd/descarga_opendata.php?file=observaciones/datohorario{day}.txt"
        )

        save_path: Path = (
            relative_path / f"{day[0:4]}" / f"{day[4:6]}" / f"datohorario{day}.txt"
        )
        if not save_path.exists():
            # Llama a la función para descargar el archivo
            fetch_daily_data(url, save_path)
        else:
            print(f"Ya existe el archivo: datohorario{day}.txt")

    # Ejemplo de uso
    data_directory = "data"
    output_csv_file = "all_smn_daily_data.csv"

    daily_data_parser(data_directory, output_csv_file)


if __name__ == "__main__":
    main()


# (\d{8})\s+(\d+)\s+([\d.]+)\s+(\d+)\s+([\d.]+)\s+(\d+)\s+(\d+)\s+(.+)
