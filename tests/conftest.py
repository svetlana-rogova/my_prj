from typing import Any

import pytest

import pandas as pd


@pytest.fixture
def enumeration_dictionaries() -> list[dict[str, str]]:
    return [
        {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_transactions() -> list[dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 582913477,
            "state": "EXECUTED",
            "date": "2022-11-15T14:47:10.125673",
            "operationAmount": {"amount": "12500.50", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Оплата услуг",
            "from": "Счет 40817810099910004312",
            "to": "Счет 40817810432100056789",
        },
    ]


@pytest.fixture
def mock_df():
    mock_df = pd.DataFrame({"id": [650703], "state": ["EXECUTED"], "amount": [16210]})
    return mock_df
