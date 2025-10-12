import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

headers = {"apikey": API_KEY}


def amount_transactions(transaction):
    """Выводим сумму транзакции. Если сумма не в рублях, то конвертируем ее"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    elif currency in ("USD", "EUR"):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("result")
        else:
            print("Возникла ошибка, перепроверьте введенные данные")
    else:
        print("Возникла ошибка, перепроверьте введенные данные")
