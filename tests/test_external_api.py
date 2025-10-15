from unittest.mock import patch

from src.external_api import amount_transactions, headers


@patch('src.external_api.requests.get')
def test_amount_transactions(mock_get):
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "RUB"}
        }
    }
    assert amount_transactions(transaction) == 100.0

    transaction_usd = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 8115.4592}
    result = amount_transactions(transaction_usd)
    assert result == 8115.4592
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.0", headers=headers
    )
    transaction_usd = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    mock_get.return_value.status_code = 400
    assert amount_transactions(transaction_usd) == 0.0
