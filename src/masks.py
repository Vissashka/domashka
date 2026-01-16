def get_mask_card_number(card_number: int) -> str:
    """
    Функция получает номер банковской карты и возвращает её маской формата 'XXXX XX** **** XXXX'.

    :param card_number: Целое число — номер карты
    :return: Строка с маской номера карты
    """
    number_str = (
        f"{card_number:016d}"  # Приводим к строке фиксированной длины 16 символов
    )
    return f"{number_str[:4]} {number_str[4:6]}** **** {number_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Функция получает номер банковского счёта и возвращает его маской формата '**XXXX'.

    :param account_number: Целое число — номер счёта
    :return: Строка с маской номера счёта
    """
    number_str = f"{account_number:d}"  # Преобразуем целое число в строку
    return f"**{number_str[-4:]}"


import logging
from pathlib import Path

# Вычисляем путь к папке logs относительно местоположения этого файла
LOG_DIR = Path(__file__).parent.parent / "logs"

# Путь к файлу лога для масок
MASK_LOG_FILE = LOG_DIR / "masks.log"

# Получаем логгер для конкретного модуля
logger_masks = logging.getLogger('masks')

# Установим минимальный уровень логирования
logger_masks.setLevel(logging.DEBUG)

# Создаём формат вывода логов
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(module)-10s | %(message)s')

# Настраиваем хендлер для записи в файл
file_handler = logging.FileHandler(MASK_LOG_FILE)
file_handler.setFormatter(formatter)

# Присоединяем хендлер к логгеру
logger_masks.addHandler(file_handler)
