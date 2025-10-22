import os
import re
from collections import Counter

from src.reading_transactions import read_transactions_csv
from src.reading_transactions import read_transactions_excel
from src.utils import data_transactions


file_json = data_transactions(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json"))
file_csv = read_transactions_csv(os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv"))
file_excel = read_transactions_excel(os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx"))


def process_bank_search(file: list[dict], search: str) -> list[dict]:
    """Функция для поиска банковской операции по заданной строке"""
    my_list = []
    for transactions in file:
        search_object = str(transactions.get("state", ""))
        pattern = re.compile(rf"\b{search}\b")
        matches = pattern.search(search_object)
        if matches:
            my_list.append(transactions)
    return my_list


def categories(data: list[dict]) -> list:
    """Функция для создания списка возможных категорий"""
    categories = []
    for transactions in data:
        if transactions.get("description") not in categories and transactions.get("description"):
            categories.append(transactions.get("description"))
    return categories


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция для подсчета количества повторений категорий транзакций"""
    list_categories = [transactions.get("description") for transactions in data]
    counted = dict(Counter(list_categories))
    result = {}
    for cat in categories:
        result[cat] = counted.get(cat, 0)
    return result


if __name__ == "__main__":
    cat = categories(file_csv)
    print(process_bank_search(file_excel, "CANCELED"))
    print(categories(file_excel))
    print(process_bank_operations(file_excel, cat))
