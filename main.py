import pandas as pd

# Путь к файлу Excel
excel_file_path = './data/transactions_excel.xlsx'

# Загрузка данных из Excel файла с указанием движка
df = pd.read_excel(excel_file_path, engine='openpyxl')  # или 'xlrd' для .xls файлов

# Вывод первых 5 строк для проверки
print(df.head())

import json
from typing import List, Dict

# Импортируем ранее созданные функции
from src.process_data import process_bank_search, process_bank_operations


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    # Обработка выбора формата файлов
    file_type = input(
        "Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла\n")

    if file_type == '1':
        with open('data.json') as f:
            data = json.load(f)
    else:
        raise NotImplementedError("Поддерживаются только JSON-файлы")

    # Фильтрация по статусу
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status_filter = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: {}\n".format(
                ", ".join(valid_statuses)))
        if status_filter.upper() not in valid_statuses:
            print("Статус операции {} недоступен.".format(status_filter))
        else:
            break

    filtered_data = [item for item in data if item["state"] == status_filter.upper()]

    # Дополнительные фильтры и сортировка
    sort_by_date = input("Отсортировать операции по дате? Да/Нет ")
    if sort_by_date.lower() == 'да':
        sorted_order = input("Отсортировать по возрастанию или по убыванию?")
        if sorted_order.lower() == 'по возрастанию':
            filtered_data.sort(key=lambda x: x['date'])
        elif sorted_order.lower() == 'по убыванию':
            filtered_data.sort(key=lambda x: x['date'], reverse=True)

    filter_currency = input("Выводить только рублевые транзакции? Да/Нет ")
    if filter_currency.lower() == 'да':
        filtered_data = [item for item in filtered_data if item['amount']['currency'] == 'RUB']

    search_in_description = input("Отфильтровать список транзакций по определённому слову в описании? Да/Нет ")
    if search_in_description.lower() == 'да':
        search_term = input("Введите слово для поиска в описании:")
        filtered_data = process_bank_search(filtered_data, search_term)

    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...")
    for idx, transaction in enumerate(filtered_data):
        print(f"{transaction['date']} {transaction['description']}")
        print(
            f"Счет {transaction['account_number'][:4]}****{transaction['account_number'][-4:]}\nСумма: {transaction['amount']['value']} {transaction['amount']['currency']}\n")


if __name__ == "__main__":
    main()

def convert_currency(transaction):
    # Реализация функции...
    pass