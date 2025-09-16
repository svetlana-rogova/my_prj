from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(standard_number, short_number, word, long_number):
    assert get_mask_card_number(standard_number) == "7000 79** **** 6361"
    assert get_mask_card_number(short_number) == "Номер карты должен состоять из 16 цифр"
    assert get_mask_card_number(word) == "Номер карты должен состоять из 16 цифр"
    assert get_mask_card_number(long_number) == "Номер карты должен состоять из 16 цифр"


def test_get_mask_account(standard_number, short_number, word, long_number):
    assert get_mask_account(standard_number) == "**6361"
    assert get_mask_account(short_number) == "В номере счета должно быть больше 4 цифр"
    assert get_mask_account(word) == "В номере счета должно быть больше 4 цифр"
    assert get_mask_account(long_number) == "**6361"
