def get_mask_card_number(num_card: str) -> str:
    """Маскируем номер банковской карты"""
    if len(num_card) == 16 and num_card.isdigit():
        groups = [num_card[i: i + 4] for i in range(0, len(num_card), 4)]
        return f"{groups[0]} {groups[1][:2]}** **** {groups[3]}"
    else:
        return "Номер карты должен состоять из 16 цифр"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(num_account: str) -> str:
    """Маскируем номер счета"""
    if len(num_account) > 4 and num_account.isdigit():
        return f"**{num_account[-4:]}"
    else:
        return "В номере счета должно быть больше 4 цифр"


print(get_mask_account("73654108430135874305"))
