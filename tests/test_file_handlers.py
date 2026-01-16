import unittest
from unittest.mock import patch, mock_open
from src.file_handlers import read_csv_transactions

class TestFileHandlers(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='id,name,age\n1,Alice,30\n2,Bob,25')
    def test_read_csv_transactions(self, mock_file):
        result = read_csv_transactions('file.csv')
        expected = [{'id': '1', 'name': 'Alice', 'age': '30'}, {'id': '2', 'name': 'Bob', 'age': '25'}]
        self.assertEqual(result, expected)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_read_csv_transactions_file_not_found(self, mock_file):
        result = read_csv_transactions('file.csv')
        self.assertIsNone(result)

    @patch('builtins.open', side_effect=Exception)
    def test_read_csv_transactions_exception(self, mock_file):
        result = read_csv_transactions('file.csv')
        self.assertIsNone(result)

import unittest
from unittest.mock import patch
from src.file_handlers import read_excel_transactions
import pandas as pd

class TestFileHandlers(unittest.TestCase):
    @patch('pandas.read_excel')
    def test_read_excel_transactions(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob'], 'age': [30, 25]})
        result = read_excel_transactions('file.xlsx')
        expected = [{'id': 1, 'name': 'Alice', 'age': 30}, {'id': 2, 'name': 'Bob', 'age': 25}]
        self.assertEqual(result, expected)

    @patch('pandas.read_excel', side_effect=FileNotFoundError)
    def test_read_excel_transactions_file_not_found(self, mock_read_excel):
        result = read_excel_transactions('file.xlsx')
        self.assertIsNone(result)

    @patch('pandas.read_excel', side_effect=Exception)
    def test_read_excel_transactions_exception(self, mock_read_excel):
        result = read_excel_transactions('file.xlsx')
        self.assertIsNone(result)




