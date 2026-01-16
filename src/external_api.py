import logging
import requests
from typing import Dict, Any
import os

logger = logging.getLogger(__name__)

def convert_currency(transaction: Dict[str, Any]):
    currency = transaction.get("currency")
    amount = transaction.get("amount")
    BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'
    HEADERS = {'apikey': os.getenv('EXCHANGE_RATES_API_KEY')}

    if currency is None or amount is None:
        logger.error("Необходимые данные (валюта или сумма) отсутствуют.")
        return None

    try:
        response = requests.get(BASE_URL, headers=HEADERS, params={"base": currency, "symbols": "RUB"})
        if response.status_code != 200:
            logger.error(f"Ошибка запроса к API ({response.status_code}). Ответ: {response.text}")
            return None

        data = response.json()
        if "rates" in data and "RUB" in data["rates"]:
            rate = data["rates"]["RUB"]
            return round(float(amount) * rate, 2)
        else:
            logger.error("Ошибка: Нет данных по курсу.")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка подключения: {e}")
        return None



