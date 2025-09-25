from typing import Any, Generator


def filter_by_currency(
    list_transactions: list[dict[str, Any]], currency: str = "USD"
) -> Generator[dict[str, Any], None, None]:
    """Функция для вывода транзакции по критерию"""
    return (
        transaction
        for transaction in list_transactions
        if transaction["operationAmount"]["currency"]["name"] == currency
    )


def transaction_descriptions(list_transactions: list[dict[str, Any]]) -> Generator[str, None, None]:
    """Функция, которая выводит описание транзакуии"""
    for transaction in list_transactions:
        yield transaction["description"]


def card_number_generator(start_number: int, end_number: int) -> Generator[str, None, None]:
    """Функция для генерации номера карты"""
    for num in range(start_number, end_number + 1):
        number_card = str(num).zfill(16)
        yield number_card[0:4] + " " + number_card[4:8] + " " + number_card[8:12] + " " + number_card[12:16]
