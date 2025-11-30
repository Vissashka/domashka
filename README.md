# Виджет банковских операций

Проект представляет собой интерфейс для отображения банковской активности клиентов. Поддерживаются фильтрация и сортировка транзакций по статусу и дате соответственно.

## Установка и запуск

Перед использованием убедитесь, что установлен Python версии >= 3.8.

Склонируйте репозиторий:

git clone https://github.com/Vissashka/domashka.git

## Установите зависимости (при наличии):

cd domashka
poetry install

pip install -r requirements.txt

## Запустите приложение (пример скрипта запуска):

python app.py

## Функционал сервисаСервис включает следующие возможности:
* Маскировку номеров карт и счетов: 
 используется для защиты персональных данных пользователей.
* Фильтрацию транзакций: 
 позволяет выбирать только успешные операции.
* Сортировку транзакций: 
 сортирует операции по дате (самые свежие вверху).
## Использование 
* APIМодуль src/masks.py обрабатывает персональные данные (карты и счета), 
* модуль src/widget.py формирует основную структуру виджета
* модуль src/processing.py осуществляет обработку транзакций.
## Примеры использования
### Маскировка карты и счета

pythonfrom src.masks import get_mask_card_number, get_mask_account

Маскируем карту
print(get_mask_card_number(7000792289606361))  # 7000 79** **** 6361

Маскируем счёт
print(get_mask_account(73654108430135874305))  # **4305### Работа с виджетом

pythonfrom src.widget import mask_account_card, get_date

Обрабатываем аккаунт или карту
print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361

Конвертируем дату
print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024### Обработка транзакций

pythonfrom src.processing import filter_by_state, sort_by_date

transactions = [    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]

Фильтруем транзакции по состоянию
executed_transactions = filter_by_state(transactions)print(executed_transactions)

Сортируем транзакции по дате
sorted_transactions = sort_by_date(transactions)print(sorted_transactions)