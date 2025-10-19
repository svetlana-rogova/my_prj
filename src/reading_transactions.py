import csv
import os
import pandas as pd


def read_transactions_csv(file_csv):
    """Функция для считывания данных по транзкциям из csv файла"""
    try:
        with open(file_csv, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            return [row for row in reader]
    except FileNotFoundError:
        return "Файл не найден"


file_transactions = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
# if __name__ == "__main__":
#     print(read_transactions_csv(file_transactions))


def read_transactions_excel(file_excel):
    """Функция для считывания данных по транзкциям из excel файла"""
    try:
        reader = pd.read_excel(file_excel)
        dict_list = reader.to_dict(orient="records")
        return dict_list
    except FileNotFoundError:
        return "Файл не найден"


file_excel = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")
if __name__ == "__main__":
    print(read_transactions_excel(file_excel))
