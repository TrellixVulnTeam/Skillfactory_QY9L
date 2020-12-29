import requests
import json

class BankAPI:
    @staticmethod
    def get_price(base, quote, amount):
        print(f"https://api.exchangeratesapi.io/latest?base={base.upper()}&symbols={quote.upper()}")
        request = requests.get(f"https://api.exchangeratesapi.io/latest?base={base.upper()}&symbols={quote.upper()}")
        print("sys--> ", request.content)
        rate = float(json.loads(request.content)["rates"][quote.upper()])
        print("sys--> ", rate)
        return f"{amount} {base.upper()} = {rate * float(amount)} {quote.upper()}"

class APIException(BaseException):
    def __init__(self,error,text):
        self.error = error
        self.text = text

