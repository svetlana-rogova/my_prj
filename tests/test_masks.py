import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected_result", [
    ("7000792289606361", "7000 79** **** 6361"),
    ((), "Номер карты должен состоять из 16 цифр"),
    ("python", "Номер карты должен состоять из 16 цифр"),
    ("70007922896063617000792289606361", "Номер карты должен состоять из 16 цифр")
])
def test_get_mask_card_number(card_number: str, expected_result: str) -> None:
    assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize("card_number, expected_result", [
    ("7000792289606361", "**6361"),
    ((), "В номере счета должно быть больше 4 цифр"),
    ("python", "В номере счета должно быть больше 4 цифр"),
    ("70007922896063617000792289606361", "**6361")
])
def test_get_mask_account(card_number: str, expected_result: str) -> None:
    assert get_mask_account(card_number) == expected_result
