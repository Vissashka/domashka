from typing import Generator, Optional, Union
from itertools import count


def filter_by_currency(transactions: list, currency_code: str) -> Generator:
    """
    Фильтрация транзакций по заданной валюте.

    :param transactions: Список транзакций, представленных словарями.
    :param currency_code: Валюта для фильтрации.
    :return: Итератор, содержащий подходящие транзакции.
    """
    for tx in transactions:
        try:
            amount_data = tx.get("operationAmount") or {}
            currency_data = amount_data.get("currency") or {}

            if currency_data.get("code") == currency_code:
                yield tx
        except Exception as e:
            pass  # Или можно записать ошибку куда-то дополнительно


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """
    Получение описаний транзакций.

    :param transactions: Список транзакций.
    :return: Итератор строковых описаний транзакций.
    """
    for tx in transactions:
        try:
            yield tx["description"]
        except KeyError:
            continue  # Пропускаем транзакции без описания

def card_number_generator(start: int = 1, stop: Optional[int] = None) -> Generator[str, None, None]:
    """
    Генерирует номера банковских карт в указанном диапазоне.

    Parameters:
        start (int): Начальное значение генерации номеров (по умолчанию 1).
        stop (Optional[int]): Конечное значение генерации номеров (если None, генерация продолжается бесконечно).

    Yields:
        str: Форматированный номер кредитной карты вида 'XXXX XXXX XXXX XXXX'.
    """
    for i in count(start=start):
        if stop is not None and i > stop:
            break
        formatted_num = f'{i:016}'
        yield f'{formatted_num[:4]} {formatted_num[4:8]} {formatted_num[8:12]} {formatted_num[12:]}'

