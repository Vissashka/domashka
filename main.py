import pandas as pd

# Путь к файлу Excel
excel_file_path = './data/transactions_excel.xlsx'

# Загрузка данных из Excel файла с указанием движка
df = pd.read_excel(excel_file_path, engine='openpyxl')  # или 'xlrd' для .xls файлов

# Вывод первых 5 строк для проверки
print(df.head())

