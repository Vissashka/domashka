import os
import requests
from dotenv import load_dotenv
from typing import Dict, Optional

load_dotenv()
API_KEY = os.getenv('EXCHANGE_RATES_API_KEY')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'
HEADERS = {'apikey': API_KEY}


def convert_currency(transaction: Dict[str, any]) -> Optional[float]:
    """
    Преобразует сумму транзакции в рубли, обращаясь к API
    обменных курсов при необходимости.

    :param transaction: Словарь с информацией о транзакции
    :return: Сумма транзакции в рублях (если доступна валюта),
             None в противном случае
    """
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    # Валюта уже в рублях, ничего не делаем
    if currency == 'RUB':
        return amount

    response = requests.get(BASE_URL, headers=HEADERS, params={'symbols': 'RUB'})
    rates = response.json().get('rates', {})

    if 'RUB' in rates:
        rub_rate = rates['RUB']
        converted_amount = round(amount * rub_rate, 2)
        return converted_amount
    else:
        return None
