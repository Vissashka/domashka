from unittest.mock import patch

import pandas as pd

from src.file_handlers import read_csv_transactions, read_excel_transactions


# Тест для CSV
@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv):
    # Эмулируем данные из CSV
    expected_data = [
        {'id': 1, 'amount': 100},
        {'id': 2, 'amount': 200}
    ]
    mock_df = pd.DataFrame(expected_data)
    mock_read_csv.return_value = mock_df

    # Вызываем нашу функцию с поддельным путём к файлу
    result = read_csv_transactions("fake/path/to/file.csv")

    # Проверяем, что результат совпадает с ожидаемым
    assert len(result) == len(expected_data)
    for actual_row, expected_row in zip(result, expected_data):
        assert actual_row == expected_row


# Тест для Excel
@patch("pandas.read_excel")
def test_read_excel_transactions(mock_read_excel):
    # Эмулируем данные из Excel
    expected_data = [
        {'order_id': 101, 'price': 500},
        {'order_id': 102, 'price': 750}
    ]
    mock_df = pd.DataFrame(expected_data)
    mock_read_excel.return_value = mock_df

    # Вызываем нашу функцию с поддельным путём к файлу
    result = read_excel_transactions("fake/path/to/excel.xlsx")

    # Проверяем, что результат совпадает с ожидаемым
    assert len(result) == len(expected_data)
    for actual_row, expected_row in zip(result, expected_data):
        assert actual_row == expected_row

