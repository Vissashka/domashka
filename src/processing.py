from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Отфильтровывает транзакции по состоянию."""
    filtered_transactions = [
        transaction for transaction in transactions
        if transaction.get('state') == state
    ]
    return filtered_transactions


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует операции по дате.

    Аргументы:
      transactions: Список словарей с операциями.
      reverse: Если True, сортируем по убыванию (новые раньше старых).

    Возвращает:
      Отсортированный список операций.
    """
    return sorted(transactions, key=lambda t: t["date"], reverse=reverse)
