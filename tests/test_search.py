from src.search import categories
from src.search import process_bank_operations
from src.search import process_bank_search


def test_process_bank_search(list_transactions_for_assert):
    assert process_bank_search(list_transactions_for_assert, 'fff') == []
    assert process_bank_search(list_transactions_for_assert, "PENDING") == [{
            "id": "650703",
            "state": "PENDING",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }]


def test_categories(list_transactions_for_assert):
    assert categories(list_transactions_for_assert) == ['Перевод организации', 'Перевод с карты на карту']


def test_process_bank_operations(list_transactions_for_assert, list_categories_for_assert):
    result = process_bank_operations(list_transactions_for_assert, list_categories_for_assert)
    assert result == {'Перевод организации': 2, 'Перевод с карты на карту': 1}
