from typing import List, Dict


def filter_by_state(transactions: List[Dict], state="EXECUTED") -> List[Dict]:
    """
    Возвращает список транзакций, соответствующих заданному состоянию (по умолчанию EXECUTED).

    :param transactions: Список словарей-транзакций
    :param state: Имя состояния ('EXECUTED', 'CANCELED')
    :return: Отфильтрованный список транзакций
    """
    return [transaction for transaction in transactions if transaction["state"] == state]


from typing import List, Dict


def sort_by_date(transactions: List[Dict], ascending=False) -> List[Dict]:
    """
    Сортирует список транзакций по дате (по умолчанию в порядке убывания).

    :param transactions: Список словарей-транзакций
    :param ascending: Порядок сортировки (True — возрастающая, False — убывающая)
    :return: Отсортированный список транзакций
    """
    return sorted(transactions, key=lambda t: t["date"], reverse=not ascending)