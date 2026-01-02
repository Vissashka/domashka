from unittest.mock import patch
import pandas as pd
from src.file_handlers import read_csv_transactions, read_excel_transactions


@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv):
    expected_data = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]
    mock_df = pd.DataFrame(expected_data)
    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("mocked/path/to/file.csv")
    assert result == expected_data


@patch("pandas.read_excel")
def test_read_excel_transactions(mock_read_excel):
    expected_data = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]
    mock_df = pd.DataFrame(expected_data)
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("mocked/path/to/file.xlsx")
    assert result == expected_data
