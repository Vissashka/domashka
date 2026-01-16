import unittest
from unittest.mock import patch
from src.external_api import convert_currency  # Предполагаем, что ваша функция находится в модуле your_module
import requests_mock
import os
import requests

class TestCurrencyConversion(unittest.TestCase):

    def setUp(self):
        self.sample_transaction = {"amount": 100, "currency": "USD"}

    def test_successful_conversion(self):
        expected_response = {
            "rates": {"RUB": 75.5}
        }
        with patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": "test_api_key"}):
            with requests_mock.Mocker() as m:
                m.get('https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=RUB', json=expected_response)
                result = convert_currency(self.sample_transaction)
                self.assertEqual(result, 7550.00)

    def test_invalid_api_key(self):
        with patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": "invalid_api_key"}):
            with requests_mock.Mocker() as m:
                m.get('https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=RUB', status_code=401)
                result = convert_currency(self.sample_transaction)
                self.assertIsNone(result)

    def test_missing_rate_in_response(self):
        invalid_response = {
            "rates": {}  # отсутствие данных по валюте RUB
        }
        with patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": "test_api_key"}):
            with requests_mock.Mocker() as m:
                m.get('https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=RUB', json=invalid_response)
                result = convert_currency(self.sample_transaction)
                self.assertIsNone(result)

    def test_network_error(self):
        with patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": "test_api_key"}):
            with requests_mock.Mocker() as m:
                m.get('https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=RUB',
                      exc=requests.exceptions.ConnectionError)
                result = convert_currency(self.sample_transaction)
                self.assertIsNone(result)

    def test_zero_amount(self):
        zero_amount_transaction = {"amount": 0, "currency": "EUR"}
        with patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": "test_api_key"}):
            with requests_mock.Mocker() as m:
                m.get('https://api.apilayer.com/exchangerates_data/latest?base=EUR&symbols=RUB', json={"rates": {"RUB": 80}})
                result = convert_currency(zero_amount_transaction)
                self.assertEqual(result, 0.00)

    def test_unsupported_currency(self):
        unsupported_transaction = {"amount": 100, "currency": "XXX"}
        with patch.dict(os.environ, {"EXCHANGE_RATES_API_KEY": "test_api_key"}):
            with requests_mock.Mocker() as m:
                m.get('https://api.apilayer.com/exchangerates_data/latest?base=XXX&symbols=RUB', status_code=400)
                result = convert_currency(unsupported_transaction)
                self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

