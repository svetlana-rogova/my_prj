from masks import get_mask_card_number
from masks import get_mask_account
from datetime import datetime

def mask_account_card(info: str) -> str:
    """Функция для обработки информации как о картах, так и о счетах"""
    new_info = info.split()
    name_info = [el for el in new_info if el.isalpha()]
    if new_info [0] == 'Счет':
        return ' '.join(name_info) + ' ' + get_mask_account(new_info[-1])
    else:
        return ' '.join(name_info) + ' ' + get_mask_card_number(new_info[-1])


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 8990922113665229"))



def get_date(time_data: str) -> str:
    """Вывод даты в нужном формате"""
    split_time_data = time_data.split('T')[0]
    split_time_data_new = split_time_data.split('-')
    return f'"{split_time_data_new[2]}.{split_time_data_new[1]}.{split_time_data_new[0]}"'


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))

