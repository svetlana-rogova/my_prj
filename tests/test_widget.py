import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("requisites, expected_response", [
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Счет 374650916", "Счет **0916"),
    ("352", "Номер карты должен состоять из 16 цифр"),
    ("Счет 872", "В номере счета должно быть больше 4 цифр")
])
def test_mask_account_card(requisites, expected_response):
    assert mask_account_card(requisites) == expected_response


@pytest.mark.parametrize("time_and_date, expected_response", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2025-09-17T02:27:12.654407", "17.09.2025")
])
def test_get_date(time_and_date, expected_response):
    assert get_date(time_and_date) == expected_response


def test_get_date_invalid():
    with pytest.raises(IndexError):
        get_date("20250917")
