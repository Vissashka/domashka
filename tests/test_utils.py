from unittest.mock import MagicMock, patch

from src.external_api import convert_currency
from src.utils import load_json


@patch('builtins.open', new_callable=MagicMock)
def test_load_json(mock_open):
    # Подготавливаем мокированные данные
    mock_file = MagicMock()
    mock_file.read.return_value = '[{"id": 1}]'
    mock_open.return_value.__enter__.return_value = mock_file

    result = load_json('fake/path/to/file.json')
    assert len(result) == 1
    assert result[0]['id'] == 1


@patch('src.external_api.requests.get')
def test_convert_currency(mock_get):
    # Подготовим моковские данные для успешного HTTP-запроса
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'rates': {'RUB': 75.0},
    }
    mock_get.return_value = mock_response

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_currency(transaction)
    assert result == 7500.0
