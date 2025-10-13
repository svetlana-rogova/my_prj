import json
from unittest.mock import mock_open, patch

from src.utils import data_transactions


def test_data_transactions():
    with patch("os.path.exists", return_value=False):
        result = data_transactions("mock_file")
        assert result == []
    with patch("os.path.getsize", return_value=0):
        result = data_transactions("mock_file")
        assert result == []
    fake_data = [{"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}}]
    m = mock_open(read_data=json.dumps(fake_data))
    with patch("builtins.open", m):
        with open("fake_file.json", "r") as f:
            result = json.load(f)
    assert result == fake_data
