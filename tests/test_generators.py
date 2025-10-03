import pytest

from typing import Any

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(list_transactions: list[dict[str, Any]]) -> None:
    generator = filter_by_currency(list_transactions)
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    gen = filter_by_currency(list_transactions, currency="EUR")
    assert next(gen) == {
        "id": 582913477,
        "state": "EXECUTED",
        "date": "2022-11-15T14:47:10.125673",
        "operationAmount": {"amount": "12500.50", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Оплата услуг",
        "from": "Счет 40817810099910004312",
        "to": "Счет 40817810432100056789",
    }
    gen_two = filter_by_currency(list_transactions, currency="RUB")
    assert list(gen_two) == []


def test_transaction_descriptions(list_transactions: list[dict[str, Any]]) -> None:
    generator = transaction_descriptions(list_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Оплата услуг"


def test_card_number_generator_one() -> None:
    gen = card_number_generator(2, 8)
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    assert next(gen) == "0000 0000 0000 0004"


@pytest.mark.parametrize(
    "start_number, end_number, number_card", [(2, 10, "0000 0000 0000 0002"), (10, 16, "0000 0000 0000 0010")]
)
def test_card_number_generator_two(start_number: int, end_number: int, number_card: int) -> None:
    gen = card_number_generator(start_number, end_number)
    assert next(gen) == number_card
