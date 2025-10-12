import json
import os

def data_transactions(input_file):
    """Функция для чтения файла и вывода списка с данными о транзакциях"""
    if not os.path.exists(input_file) or os.path.getsize(input_file) == 0:
        return []
    with open(input_file, "r", encoding="utf-8") as f:
        try:
            transactions = json.load(f)
            return transactions
        except FileNotFoundError:
            return []




input_file = os.path.join(os.path.dirname(__file__),"..", "data", "operations.json")
print(data_transactions(input_file))


