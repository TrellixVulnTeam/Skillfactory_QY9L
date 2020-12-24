import telebot
import requests
import json

TOKEN = "1453157377:AAE2uFDEg5cwm1fkOI_aDSrHj8v4dr-ydpw"


def bank_api_poll(base, quote):
    request = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}&symbols={quote}")
    print(request.content)
    rate = float(json.loads(request.content)['rates'][quote])
    print(rate)

    return rate


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
        cur_values = cur_values + f"{cur}: {cur_data[cur]} "
    return cur_values


def g_bank_api_poll(base, quote):
    request = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}&symbols={quote}")
    print(request.content)
    rate = float(json.loads(request.content)['rates'][quote])
    print(rate)

    return rate
# Обрабатываются все сообщения содержащие команды '/start' or '/help'.


bot = telebot.TeleBot(TOKEN)
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


#  bank_api_poll("EUR", "USD")


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    print(f"{message.from_user.username}: {message.text}")
    rep = instruction()
    bot.send_message(chat_id=message.chat.id, text=rep)


@bot.message_handler(commands=['values'])  # Обработчик для команды /values
def handle_start_help(message):
    print(f"{message.from_user.username}: {message.text}")
    rep = values()
    bot.send_message(chat_id=message.chat.id, text=rep)


@bot.message_handler(commands=['convert'])  # Обработчик для группы
def handle_start_help(message):
    print(f"{message.from_user.username}: {message.text}")
    try:
        command, base, quote, amount = message.text.split(' ', 3)
    except AttributeError:
        answer = "err:Broken Attributes"
        print(answer)
    except ValueError:
        answer = "err:Value Error"
        print(answer)
    else:
        base, quote = base.upper(), quote.upper()
        print(command[1::], base.upper(), quote.upper(), amount)
        rate = bank_api_poll(base.upper(), quote.upper())
        answer = f"{amount} {base} = {rate*float(amount)} {quote}"
    bot.reply_to(message, text=answer)


@bot.message_handler()
def repeat(message: telebot.types.Message):
    print(f"{message.from_user.username}: {message.text}")

    base, quote, amount = message.text.split(' ', 3)
    print(base, quote, amount)
    rate = bank_api_poll(base, quote)
    answer = f"{amount} {base} = {rate*float(amount)} {quote}"
    bot.reply_to(message, text=answer)


print("Bot started")
bot.polling(none_stop=True)
