import json
from pathlib import Path
import logging
from typing import List, Dict


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
    except PermissionError:
        print("Ошибка: Нет доступа к файлу.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


# Вычисляем путь к папке logs относительно местоположения этого файла
LOG_DIR = Path(__file__).parent.parent / "logs"

# Путь к файлу лога для утилит
UTILS_LOG_FILE = LOG_DIR / "utils.log"

# Получаем логгер для конкретного модуля
logger_utils = logging.getLogger('utils')

# Устанавливаем минимальный уровень логирования
logger_utils.setLevel(logging.DEBUG)

# Создаём формат вывода логов
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(module)-10s | %(message)s')

# Настраиваем хендлер для записи в файл
file_handler = logging.FileHandler(UTILS_LOG_FILE)
file_handler.setFormatter(formatter)

# Присоединяем хендлер к логгеру
logger_utils.addHandler(file_handler)






