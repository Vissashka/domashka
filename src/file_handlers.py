import pandas as pd

def read_csv_transactions(file_path):
    """
    Читает финансовые операции из CSV файла и возвращает список словарей.

    :param file_path: строка, путь к CSV файлу
    :return: list of dicts, каждая запись представляет собой словарь с полями транзакций
    """
    try:
        df = pd.read_csv(file_path, delimiter=";")
        return df.to_dict('records')
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")
        return None

def read_excel_transactions(file_path):
    """
    Читает финансовые операции из Excel файла и возвращает список словарей.

    :param file_path: строка, путь к Excel файлу
    :return: list of dicts, каждая запись представляет собой словарь с полями транзакций
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict('records')
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")
        return None





