from datetime import datetime
from typing import Tuple
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:

    # Делим строку по последнему пробелу
    parts = data.rsplit(maxsplit=1)

    # Проверяем, чтобы в результате получилось ровно два элемента
    if len(parts) != 2:
        raise ValueError("Некорректный ввод")

    name_part, number_part = parts

    # Проверяем корректность номера
    if not number_part.isdigit():
        raise ValueError("Некорректный номер карты/счета")

    # Определяем, какой тип операции выполняем (маскировка карты или счета)
    if name_part.lower().startswith("счет"):
        masked_value = get_mask_account(int(number_part))
    else:
        masked_value = get_mask_card_number(int(number_part))

    return f"{name_part} {masked_value}"

def get_date(date_string: str) -> str:


    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
