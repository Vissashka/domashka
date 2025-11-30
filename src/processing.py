from typing import List, Dict

def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Отфильтровывает транзакции по состоянию."""
    filtered_transactions = [
        transaction for transaction in transactions
        if transaction.get('state') == state
    ]
    return filtered_transactions

def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует транзакции по дате."""
    sorted_transactions = sorted(
        transactions,
        key=lambda x: x['date'],
        reverse=reverse
    )
    return sorted_transactions