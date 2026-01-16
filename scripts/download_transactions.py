import os

import requests

DOWNLOAD_DIR = './data'  # Директория, куда будут помещены скачанные файлы
URL = 'https://raw.githubusercontent.com/skypro-008/transactions/main/transactions_excel.xlsx'
FILENAME = 'transactions_excel.xlsx'

# Если папки ещё нет, создадим её
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

response = requests.get(URL)

# Сохраняем файл в указанную директорию
output_path = os.path.join(DOWNLOAD_DIR, FILENAME)

with open(output_path, 'wb') as f:
    f.write(response.content)

print(f"Файл {FILENAME} успешно скачан.")
