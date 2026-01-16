import os
from typing import Dict, Optional

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('EXCHANGE_RATES_API_KEY')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'
HEADERS = {'apikey': API_KEY}


def convert_currency(transaction: Dict[str, Any]):
    # ...
    response = requests.get(BASE_URL, headers=HEADERS, params={"base": currency, "symbols": "RUB"})

    if response.status_code == 200:
        data = response.json()

        # Логика для проверки наличия необходимой информации
        if "rates" in data and "RUB" in data["rates"]:
            rate = data["rates"]["RUB"]
            return round(amount * rate, 2)
        else:
            print("Ошибка: Не найдены данные по курсу.", data)
            return None
    else:
        print(f"Ошибка запроса к API ({response.status_code}). Ответ:", response.text)
        return None

