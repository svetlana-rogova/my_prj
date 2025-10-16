import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(num_card: str) -> str:
    """Маскируем номер банковской карты"""
    if len(num_card) == 16 and num_card.isdigit():
        groups = [num_card[i: i + 4] for i in range(0, len(num_card), 4)]
        logger.info("Номер карты успешно замаскирован")
        return f"{groups[0]} {groups[1][:2]}** **** {groups[3]}"
    else:
        logger.warning("Ошибка при вводе номера банковской карты")
        return "Номер карты должен состоять из 16 цифр"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))


def get_mask_account(num_account: str) -> str:
    """Маскируем номер счета"""
    if len(num_account) > 4 and num_account.isdigit():
        logger.info("Номер счета успешно замаскирован")
        return f"**{num_account[-4:]}"
    else:
        logger.warning("Ошибка при вводе номера счета")
        return "В номере счета должно быть больше 4 цифр"


if __name__ == "__main__":
    print(get_mask_account("73654108430135874305"))
