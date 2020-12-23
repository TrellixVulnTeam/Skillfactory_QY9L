import telebot
import requests
token = "1453157377:AAE2uFDEg5cwm1fkOI_aDSrHj8v4dr-ydpw"

bot = telebot.TeleBot(token)


# Обрабатываются все сообщения содержащие команды '/start' or '/help'.


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(chat_id=message.chat.id, text=f"{message.chat.username}! Ты ввел команду start или help! Нифига себе, ты умеещь тыкать по кнопкам и читать! Поздравляю!")

@bot.message_handler(commands=['value'])
def handle_start_help(message):
    bot.send_message(chat_id=message.chat.id, text=f"{message.chat.username}! Ты ввел команду start или help! Нифига себе, ты умеещь тыкать по кнопкам и читать! Поздравляю!")

@bot.message_handler()
def repeat(message: telebot.types.Message):
    bot.reply_to(message, text=f"Не знаю такой команды, {message.chat.username}. Попробуй /start или /help")

bot.polling(none_stop=True)