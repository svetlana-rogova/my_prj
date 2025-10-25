import json
import logging
import os


def data_transactions(input_file):
    """Функция для чтения файла и вывода списка с данными о транзакциях"""
    log_path = os.path.join(os.path.dirname(__file__), "../logs/utils.log")
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(log_path, "w", encoding="utf-8")
    file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    try:
        if os.path.getsize(input_file) == 0:
            logger.debug("Файл пуст")
            return []
        with open(input_file, "r", encoding="utf-8") as f:
            transactions = json.load(f)
            logger.info("Файл прочитан и данные выведены в консоль")
            return transactions
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Фaйл не существует или данные в файле не являются корректным документом JSON")
        return []


input_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
if __name__ == "__main__":
    print(data_transactions(input_file))
