message = 'rub'
try:
    tg_string = message.split(' ')
    base = tg_string[0]
    quote = tg_string[1]
    amount = tg_string[2]

except TypeError:
    print("TypeError")


except IndexError:
    print("IndexError")
except ValueError:
    print("ValueError")
except BaseException:
    print("Не отловлена ошибка")

else:
    print(base,quote,amount)