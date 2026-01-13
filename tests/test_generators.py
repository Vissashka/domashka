from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency():
    transactions = [
        {"id": 939719570, "state": "EXECUTED", "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 142264268, "state": "EXECUTED", "operationAmount": {"currency": {"code": "EUR"}}}
    ]
    usd_gen = filter_by_currency(transactions, 'USD')
    assert next(usd_gen)["id"] == 939719570

def test_transaction_descriptions():
    transactions = [
        {"id": 939719570, "description": "Перевод организации"},
        {"id": 142264268, "description": "Оплата услуг"}
    ]
    desc_gen = transaction_descriptions(transactions)
    assert next(desc_gen) == 'Перевод организации'

def test_card_number_generator():
    gen = card_number_generator(1, 5)
    numbers = list(gen)
    expected_numbers = [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004',
        '0000 0000 0000 0005'
    ]
    assert numbers == expected_numbers
