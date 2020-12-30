import telebot
from extensions import *


file = open('token.cfg', 'r')
token = file.read()
file.close()




def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def instruction():

    header = f"===Конвертер валют===\n" \
            f"Для получения результата введите три параметра: " \
            f"исходный код валюты, код валюты, в которую нужно перевести, " \
            f"и количество исходной валюты, через пробел.\n" \
            f"===\nНапример: EUR USD 150\n" \
            f"===\nСписок доступных валют: /values\n"
    return header


def values():
    cur_values = "Список доступных кодов валют:\n"+20*"="+"\n"
    for cur in cur_data:
        cur_values = cur_values + f"{cur}: {cur_data[cur]}. "
    return cur_values


def convert(message):  # Обрабатываем введенное сообщение
    try:
        tg_string = message.text.split(' ')
        base = tg_string[0].upper()
        quote = tg_string[1].upper()
        amount = tg_string[2]
        if "," in amount:
            amount = amount.replace(",",".")
    except IndexError:
        error = 1
        text = "Недостаточно параметров.\nПример команды: EUR RUB 100\nСписок валют - /values"
        raise APIException(error, text)
    else:
        if len(tg_string)>3:
            error = 2
            text = "Слишком много параметров.\nПример команды: EUR RUB 100\nСписок валют - /values"
            raise APIException(error, text)
        elif base.upper() not in cur_data.keys():
            error = 3
            text = "Неверен код исходной валюты.\nСписок валют - /values"
            raise APIException(error, text)
        elif quote.upper() not in cur_data.keys():
            error = 4
            text = "Неверен код результирующей валюты.\nСписок валют - /values"
            raise APIException(error, text)
        elif not isfloat(amount):
            error = 5
            text = "Неверно количество исходной валюты.\nПример команды: EUR RUB 100"
            raise APIException(error, text)
        elif base == quote:
            error = 6
            text = "Исходная и результирующая валюты идентичны.\nПример команды: EUR RUB 100"
            raise APIException(error, text)
        else:
            text = BankAPI.get_price(base, quote, amount)
            error = 0
    finally:
        return error, text


cur_data = {"EUR": "Евро", "USD": "Доллар США", "JPY": "Японская йена", "BGN": "Болгарский лев",
            "CZK": "Чешская крона", "DKK": "Датская крона", "GBP": "Британский фунт", "HUF": "Венгерский форинт",
            "PLN": "Польский злотый", "RON": "Румынский лей", "SEK": "Шведская крона", "CHF": "Швейцарский франк",
            "ISK": "Исландская крона", "NOK": "Норвежская крона", "HRK": "Хорватская куна", "RUB": "Российский рубль",
            "TRY": "Турецкая лира", "AUD": "Австралийский доллар", "BRL": "Бразильский реал",
            "CAD": "Канадский доллар", "CNY": "Китайский юань", "HKD": "Гонконгский доллар",
            "IDR": "Индонезийская рупия", "ILS": "Израильский шекель", "INR": "Индийская рупия",
            "KRW": "Южнокорейская вона", "MXN": "Пексиканское песо", "MYR": "Малайзиский ринггит",
            "NZD": "Новозеландский доллар", "PHP": "Филиппинское песо", "SGD": "Сингапурский доллар",
            "THB": "Тайский бат", "ZAR": "Южноафриканский рэнд"}

bot = telebot.TeleBot(token)
print("Bot started")



@bot.message_handler(commands=['start', 'help'])  # Обработчик /start /help
def handle_start_help(message):
    print(f"{message.from_user.username}: {message.text}")
    rep = instruction()
    bot.send_message(chat_id=message.chat.id, text=rep)

@bot.message_handler(commands=['start', 'help'])  # Обработчик /start /help
def handle_start_help(message):
    print(f"{message.from_user.username}: {message.text}")
    rep = instruction()
    bot.send_message(chat_id=message.chat.id, text=rep)

@bot.message_handler(commands=['values'])  # Обработчик /values
def handle_start_help(message):
    print(f"{message.from_user.username}: {message.text}")
    rep = values()
    bot.send_message(chat_id=message.chat.id, text=rep)

@bot.message_handler()  # Общий обработчик
def repeat(message: telebot.types.Message):

    print(f"{message.from_user.username}: {message.text}")
    error, result = convert(message)
    print(f"err={error}, {result}")
    if error == 0:
        bot.reply_to(message, text=result)
    else:
        bot.reply_to(message, text=f"{result}")

bot.polling(none_stop=True)
