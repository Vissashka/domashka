import re

def process_bank_search(transactions: list[dict], search_term: str) -> list[dict]:
    """
    Поиск банковских операций по заданному запросу в описании.

    :param transactions: Список словарей с информацией о транзакциях.
    :param search_term: Строка поиска, которую нужно найти в описании операций.
    :return: Список словарей с операциями, содержащими искомый термин в описании.
    """
    result = []
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)  # Регулярное выражение для нечувствительного к регистру поиска
    for transaction in transactions:
        if pattern.search(transaction.get('description', '')):  # Проверяем наличие строки в описании
            result.append(transaction)
    return result


from collections import Counter


def process_bank_operations(transactions: list[dict], categories: list[str]) -> dict:
    """
    Подсчет количества операций по заданным категориям.

    :param transactions: Список словарей с информацией о транзакциях.
    :param categories: Список категорий операций для подсчета.
    :return: Словарь, где ключи — это названия категорий, а значения — количество операций.
    """
    category_counts = Counter()
    for transaction in transactions:
        # Нормируем описание транзакции
        normalized_desc = transaction.get('description', '').strip().lower()

        # Просматриваем категории и смотрим, не входят ли они в описание транзакции
        for category in categories:
            normalized_category = category.strip().lower()

            # Частичное совпадение или точное совпадение — считаем достаточно
            if normalized_category in normalized_desc or normalized_desc.startswith(normalized_category):
                category_counts[category] += 1

    return dict(category_counts)












