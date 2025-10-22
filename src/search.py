import re
from src.utils import data_transactions
import os
from src.reading_transactions import read_transactions_csv
from src.reading_transactions import read_transactions_excel


def process_bank_search(file:list[dict], search:str)->list[dict]:
    """Функция для поиска банковской операции по заданной строке"""
    my_list = []
    for transactions in file:
        search_object = str(transactions.get("state", ""))
        pattern = re.compile(fr"\b{search}\b")
        matches = pattern.search(search_object)
        if matches:
            my_list.append(transactions)
    return my_list


file_json = (data_transactions(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")))
file_csv =read_transactions_csv(os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv"))
file_excel = read_transactions_excel(os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx"))


if __name__ == "__main__":

    print(process_bank_search(file_excel, "CANCELED"))