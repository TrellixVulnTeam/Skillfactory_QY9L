import requests
import json
import math
class BankAPI:
    @staticmethod
    def get_price(base, quote, amount):
        print(f"https://api.exchangeratesapi.io/latest?base={base.upper()}&symbols={quote.upper()}")
        request = requests.get(f"https://api.exchangeratesapi.io/latest?base={base.upper()}&symbols={quote.upper()}")
        print("sys--> ", request.content)
        rate = float(json.loads(request.content)["rates"][quote.upper()])
        print("sys--> ", rate)
        return f"{math.floor(float(amount)*100)/100} {base.upper()} = {math.floor(rate * float(amount)*100)/100} {quote.upper()}"

class APIException(BaseException):
    def __init__(self,error,text):
        self.error = error
        self.text = text

