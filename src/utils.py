import json
from typing import List, Dict, Union


def load_json(file_path: str) -> List[Dict]:
    """
    Загружает JSON-файл и возвращает список объектов,
    представляющих финансовые транзакции.

    :param file_path: Путь к файлу JSON
    :return: Список словарей с данными о транзакциях
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            return data
        else:
            print("Ошибка: Неправильный формат файла.")
            return []
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []
