import requests
from pathlib import Path


def fetch_daily_data(url: str, save_path: Path) -> None:
    """
    Descarga un archivo desde la URL dada y lo guarda en la ruta especificada.

    :param url: URL del archivo a descargar.
    :param save_path: Ruta donde se guardará el archivo descargado.
    :return: None
    """
    response = requests.get(url)
    save_path.parent.mkdir(parents=True, exist_ok=True)

    if response.status_code == 200:
        try:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Archivo descargado con éxito en {save_path}.")
        except FileNotFoundError:
            print("El path del archivo a salvar no existe")

    else:
        print(
            f"Error al descargar el archivo. Código de estado: {response.status_code}"
        )
