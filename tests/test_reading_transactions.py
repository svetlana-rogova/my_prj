from src.reading_transactions import read_transactions_csv, read_transactions_excel
from unittest.mock import mock_open, patch


mock_csv_data = """id;state;date;amount;currency_name;currency_code;from;to;description\n
650703; EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
"Счет 58803664561298323391;Счет 39745660563456619397; Перевод организации"""


@patch("builtins.open", new_callable=mock_open, read_data=mock_csv_data)
def test_read_transactions_csv(file_mock):
    result = read_transactions_csv("")
    assert result[0]["id"] == "650703"
    assert len(result) == 1


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_transactions_csv_file_not_found(file_mock):
    result = read_transactions_csv("")
    assert result == "Файл не найден"


@patch("pandas.read_excel")
def test_read_transactions_excel(mock_file, mock_df):
    mock_file.return_value = mock_df
    result = read_transactions_excel("")
    assert result[0]["id"] == 650703
