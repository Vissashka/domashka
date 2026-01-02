import pandas as pd

def read_csv_transactions(file_path: str) -> list[dict]:
    """
    Читает финансовые операции из CSV-файла и возвращает список словарей,
    где каждая запись представляет собой одну операцию.

    :param file_path: Полный путь к файлу CSV
    :return: Список словарей с информацией о транзакциях
    """
    df = pd.read_csv(file_path)
    return df.to_dict('records')

def read_excel_transactions(file_path: str) -> list[dict]:
    """
    Читает финансовые операции из Excel-файла и возвращает список словарей,
    где каждая запись представляет собой одну операцию.

    :param file_path: Полный путь к файлу Excel
    :return: Список словарей с информацией о транзакциях
    """
    df = pd.read_excel(file_path)
    return df.to_dict('records')

