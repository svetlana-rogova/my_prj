import os
import re
from datetime import datetime

from src.reading_transactions import read_transactions_csv
from src.reading_transactions import read_transactions_excel
from src.utils import data_transactions
from src.search import process_bank_search


file_json = data_transactions(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json"))
file_csv = read_transactions_csv(os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv"))
file_excel = read_transactions_excel(os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx"))


def main():
    """Функция обрабатывает файлы, полученные из других модулей, и выводит данные о транзакциях,
    которые выбрал пользователь"""
    while True:
        answer = input("Привет! Добро пожаловать в программу работы с банковскими транзакциями. "
                       "Выберите необходимый пункт меню:\n"
                       " 1. Получить информацию о транзакциях из JSON - файла\n"
                       " 2. Получить информацию о транзакциях из CSV - файла\n"
                       " 3. Получить информацию о транзакциях из XLSX - файла")
        if answer == "1":
            print("Для обработки выбран JSON - файл.")
            file = file_json
            break
        elif answer == "2":
            print("Для обработки выбран CSV - файл.")
            file = file_csv
            break
        elif answer == "3":
            print("Для обработки выбран XLSX - файл.")
            file = file_excel
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")

    while True:
        word = input(("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                      "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"))
        if word.upper() == "EXECUTED":
            print("Операции отфильтрованы по статусу 'EXECUTED'")
            filter_dict = process_bank_search(file, "EXECUTED")
            break
        elif word.upper() == "CANCELED":
            print("Операции отфильтрованы по статусу 'CANCELED'")
            filter_dict = process_bank_search(file, "CANCELED")
            break
        elif word.upper() == "PENDING":
            print("Операции отфильтрованы по статусу 'PENDING'")
            filter_dict = process_bank_search(file, "PENDING")
            break
        else:
            print(f"Статус операции '{word}' недоступен")

    while True:
        answer = input("Отсортировать операции по дате? Да / Нет")
        if answer.lower() == "да":
            while True:
                answer_two = input("Отсортировать по возрастанию или по убыванию?")
                if answer_two.lower() == "по возрастанию":
                    filter_dict_data = sorted(filter_dict, key=lambda p: p["date"])
                    break
                elif answer_two.lower() == "по убыванию":
                    filter_dict_data = sorted(filter_dict, key=lambda p: p["date"], reverse=True)
                    break
                else:
                    print("Выберите по возрастанию или по убыванию")

            break
        elif answer.lower() == "нет":
            filter_dict_data = filter_dict
            break
        else:
            print("Введите Да или Нет")

    while True:
        answer_code = input("Выводить только рублевые транзакции? Да/Нет")
        filter_dict_code = []
        if answer_code.lower() == "да":
            for transaction in filter_dict_data:
                currency_code = transaction.get('operationAmount', {}).get('currency', {}).get('code')
                if currency_code == 'RUB' or transaction.get('currency_code') == 'RUB':
                    filter_dict_code.append(transaction)
            break
        elif answer_code.lower() == "нет":
            filter_dict_code = filter_dict_data
            break
        else:
            print("Введите Да или Нет")

    while True:
        answer_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        if answer_description.lower() == "да":
            word_search = input("Какое слово найти?")
            filter_dict_description = []
            for transactions in filter_dict_code:
                search_object = str(transactions.get("description", ""))
                pattern = re.compile(rf"\b{word_search}\b")
                matches = pattern.search(search_object)
                if matches:
                    filter_dict_description.append(transactions)
            if filter_dict_description == []:
                print("Введенного Вами слова нет в описании")
            break
        elif answer_description.lower() == "нет":
            filter_dict_description = filter_dict_code
            break
        else:
            print("Введите Да или Нет")
    amount_transactions = len(filter_dict_description)
    if amount_transactions == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {amount_transactions}")
        for operation in filter_dict_description:
            date_obj = datetime.fromisoformat(operation["date"])
            formater_data = date_obj.strftime("%d.%m.%Y")
            currency_name = (operation.get("operationAmount", {})
                             .get("currency", {})
                             .get("name")
                             or operation.get("currency_code", ""))

            amount = (operation.get("operationAmount", {})
                      .get("amount")
                      or operation.get("amount", ""))
            if operation.get("from"):
                print(f"\n {formater_data} {operation["description"]}\n "
                      f"{operation["from"]} -> {operation["to"]}\n Сумма: {amount} {currency_name}")
            else:
                print(f"\n {formater_data} {operation["description"]}\n "
                      f"{operation["to"]}\n Сумма: {amount} {currency_name}")


main()
