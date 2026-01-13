import csv
from typing import Dict, List

import pandas as pd


def read_csv_transactions(file_path):
    """
    Функция читает финансовые операции из CSV файла и возвращает список словарей.

    :param file_path: строка, путь к CSV файлу
    :return: list of dicts, каждая запись представляет собой словарь с полями транзакций
    """
    df = pd.read_csv(file_path)
    return df.to_dict('records')


def read_excel_transactions(file_path):
    """
    Функция читает финансовые операции из Excel файла и возвращает список словарей.

    :param file_path: строка, путь к Excel файлу
    :return: list of dicts, каждая запись представляет собой словарь с полями транзакций
    """
    df = pd.read_excel(file_path)
    return df.to_dict('records')

