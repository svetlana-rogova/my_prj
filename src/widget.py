from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Функция для обработки информации как о картах, так и о счетах"""
    new_info = info.split()
    name_info = [el for el in new_info if el.isalpha()]
    number = new_info[-1]
    if new_info[0] == "Счет":
        if len(number) <= 4 or not number.isdigit():
            return "В номере счета должно быть больше 4 цифр"
        masked = get_mask_account(number)
    else:
        if len(number) != 16 or not number.isdigit():
            return "Номер карты должен состоять из 16 цифр"
        masked = get_mask_card_number(number)
    return " ".join(name_info) + " " + masked


if __name__ == "__main__":
    print(mask_account_card("Visa Gold 5999414228426353"))


def get_date(time_data: str) -> str:
    """Вывод даты в нужном формате"""
    split_time_data = time_data.split("T")[0]
    split_time_data_new = split_time_data.split("-")
    return f'{split_time_data_new[2]}.{split_time_data_new[1]}.{split_time_data_new[0]}'


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
