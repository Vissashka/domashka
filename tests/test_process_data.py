import pytest
from src.process_data import process_bank_search, process_bank_operations

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "description": "Оплата товаров", "state": "EXECUTED"},
        {"id": 2, "description": "Перевод средств", "state": "EXECUTED"},
        {"id": 3, "description": "Пополнение счёта", "state": "CANCELED"},
        {"id": 4, "description": "Возврат платежа", "state": "PENDING"}
    ]

def test_process_bank_search(sample_transactions):
    results = process_bank_search(sample_transactions, "товаров")
    assert len(results) == 1
    assert results[0]["id"] == 1

    empty_results = process_bank_search(sample_transactions, "недоступно")
    assert len(empty_results) == 0

def test_process_bank_operations(sample_transactions):
    categories = ["Оплата", "Перевод"]
    counts = process_bank_operations(sample_transactions, categories)
    expected_result = {'Оплата': 1, 'Перевод': 1}
    assert counts == expected_result




