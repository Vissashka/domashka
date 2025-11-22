def mask_account_card(account_string):


    if account_string.startswith("Счет"):  # обработка случая банковского счёта
        _, account_number = account_string.split(maxsplit=1)
        return f"Счет {'*'*(len(account_number)-4)}{account_number[-4:]}"
    else:  # обработка всех остальных случаев (карты)
        card_type, card_number = account_string.rsplit(maxsplit=1)
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return f"{card_type} {masked_number}"














