import unittest
from unittest.mock import patch, Mock
from main import convert_currency
import sys
import os

# Добавляем корень проекта в PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestConvertCurrency(unittest.TestCase):

    def setUp(self):
        self.transaction_usd = {
            'amount': 100,
            'currency': 'USD'
        }

        self.transaction_eur = {
            'amount': 100,
            'currency': 'EUR'
        }

        self.transaction_rub = {
            'amount': 100,
            'currency': 'RUB'
        }

        self.invalid_transaction = {
            'amount': 100,
            'currency': 'XXX'
        }

        self.missing_amount_transaction = {
            'currency': 'USD'
        }

    @patch('requests.get')
    def test_convert_usd_to_rub(self, mock_get):
        """Тестирование успешного преобразования USD в рубли"""
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'RUB': 80}}
        mock_get.return_value = mock_response

        result = convert_currency(self.transaction_usd)
        expected_result = 8000.00
        self.assertEqual(result, expected_result)

    @patch('requests.get')
    def test_convert_eur_to_rub(self, mock_get):
        """Тестирование успешного преобразования EUR в рубли"""
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {'RUB': 90}}
        mock_get.return_value = mock_response

        result = convert_currency(self.transaction_eur)
        expected_result = 9000.00
        self.assertEqual(result, expected_result)

    def test_already_in_rubles(self):
        """Проверяем случай, когда валюта уже указана в рублях"""
        result = convert_currency(self.transaction_rub)
        expected_result = 100
        self.assertEqual(result, expected_result)

    @patch('requests.get')
    def test_invalid_currency(self, mock_get):
        """Проверяем обработку неверной валюты"""
        mock_response = Mock()
        mock_response.json.return_value = {'rates': {}}
        mock_get.return_value = mock_response

        result = convert_currency(self.invalid_transaction)
        self.assertIsNone(result)

    def test_missing_amount_field(self):
        """Проверяем отсутствие поля 'amount' в транзакции"""
        result = convert_currency(self.missing_amount_transaction)
        self.assertIsNone(result)

    @patch('requests.get')
    def test_server_error(self, mock_get):
        """Обработка ситуации, когда сервер API возвращает ошибку"""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            convert_currency(self.transaction_usd)


if __name__ == '__main__':
    unittest.main()


