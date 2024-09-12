from datetime import datetime, timedelta


def generate_dates_until_today(start_year: int) -> list[str]:
    """
    Genera una lista de fechas en el formato YYYYMMDD desde el 1 de enero del año dado hasta hoy.

    :param start_year: El año desde el cual empezar a generar fechas.
    :return: Una lista de strings con fechas en el formato YYYYMMDD.
    """
    start_date = datetime(start_year, 1, 1)
    end_date = datetime.now()

    dates = []
    current_date = start_date

    while current_date.date() < end_date.date():
        dates.append(current_date.strftime("%Y%m%d"))
        current_date += timedelta(days=1)

    return dates
