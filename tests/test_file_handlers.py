import pytest
import pandas as pd
from src.file_handlers import read_csv_transactions, read_excel_transactions

# Тестируемые функции находятся в модуле src.file_handlers

# Вспомогательная функция для создания временного csv-файла
@pytest.fixture(scope="session")
def create_temporary_csv(tmp_path_factory):
    content = """id;description;amount\n1;Transaction 1;100.00\n2;Transaction 2;-50.00"""
    filename = tmp_path_factory.mktemp("data") / "transactions.csv"
    filename.write_text(content)
    return str(filename)

# Вспомогательная функция для создания временного excel-файла
@pytest.fixture(scope="session")
def create_temporary_excel(tmp_path_factory):
    df = pd.DataFrame({
        "id": [1, 2],
        "description": ["Transaction 1", "Transaction 2"],
        "amount": [100.00, -50.00]
    })
    filename = tmp_path_factory.mktemp("data") / "transactions.xlsx"
    df.to_excel(filename, index=False)
    return str(filename)

# Тесты для функции read_csv_transactions

def test_read_csv_transactions_success(create_temporary_csv):
    transactions = read_csv_transactions(create_temporary_csv)
    assert len(transactions) == 2
    assert transactions[0]["id"] == 1
    assert transactions[0]["description"] == "Transaction 1"
    assert transactions[0]["amount"] == 100.00

def test_read_csv_transactions_file_not_found():
    non_existing_file = "/path/to/non-existing-file.csv"
    transactions = read_csv_transactions(non_existing_file)
    assert transactions is None

def test_read_csv_transactions_wrong_format(tmp_path):
    wrong_format_file = tmp_path / "wrong-format.csv"
    wrong_format_file.write_text("This,is,a,wrong,format")
    transactions = read_csv_transactions(str(wrong_format_file))
    assert transactions is None

# Тесты для функции read_excel_transactions

def test_read_excel_transactions_success(create_temporary_excel):
    transactions = read_excel_transactions(create_temporary_excel)
    assert len(transactions) == 2
    assert transactions[0]["id"] == 1
    assert transactions[0]["description"] == "Transaction 1"
    assert transactions[0]["amount"] == 100.00

def test_read_excel_transactions_file_not_found():
    non_existing_file = "/path/to/non-existing-file.xlsx"
    transactions = read_excel_transactions(non_existing_file)
    assert transactions is None

def test_read_excel_transactions_wrong_format(tmp_path):
    wrong_format_file = tmp_path / "wrong-format.xlsx"
    wrong_format_file.write_text("This is not an Excel file!")
    transactions = read_excel_transactions(str(wrong_format_file))
    assert transactions is None










