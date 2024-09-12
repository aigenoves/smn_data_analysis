import sys
from pathlib import Path
from src.daily_data_fetcher import fetch_daily_data
from src.utils import generate_dates_until_today


def main() -> None:
    # URL del archivo que deseas descargar
    main_path = Path(__file__).resolve()

    # Obtener el directorio que contiene main.py
    main_directory = main_path.parent

    # Si necesitas un path relativo a main.py, por ejemplo, a una carpeta 'data' dentro del mismo directorio
    relative_path = main_directory / "data"

    start_year = 2023
    dates_list = generate_dates_until_today(start_year)
    for day in dates_list:
        url: str = (
            f"https://ssl.smn.gob.ar/dpd/descarga_opendata.php?file=observaciones/datohorario{day}.txt"
        )
        save_path: Path = (
            relative_path / f"{day[0:4]}" / f"{day[4:6]}" / f"datohorario{day}.txt"
        )

        # Llama a la función para descargar el archivo
        fetch_daily_data(url, save_path)


if __name__ == "__main__":
    main()
