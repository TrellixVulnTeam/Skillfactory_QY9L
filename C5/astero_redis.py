import redis
import json

asterodb = redis.Redis(
    host="redis-18571.c44.us-east-1-2.ec2.cloud.redislabs.com",
    port=18571,
    password="Ny6EBAiiCaoGxUZa0rcpyvKODlH8V7Q1"
)


def add_record(name,phone):
    asterodb.set(name,phone)


def show_records():
    #records = json.loads(asterodb.get('name_phone'))
    name = input("Введите имя: ")
    print(asterodb.get(name))

def delete_record():

    delt = input("Введите имя: ")
    asterodb.delete(delt)


print("---Телефонная книгга---")
print("1. Добавить запись")
print("2. Удалить запись")
print("3. Обновить данные в БД")
print("4. Вывести данные из БД")
print("0. Выход")
print("-----------------------")
while True:
    sel = input("Выберите(1,2,3,4,0): ")
    if sel == "1":
        print("Добавление записи")
        name = input("Введите имя: ")
        phone = input("Введите тел №: ")
        add_record(name, phone)

    elif sel =="2":
        print("Удаление записи")
        delete_record()
    elif sel =="3":
        print("Обновление данных в БД")
    elif sel == "4":
        print("Вывод данных из БД")
        show_records()
    elif sel == "0":
        print("Выход из программы")
        break
    else:
        print("Выберите 1,2,3,4,0")




# dict1 = {'key1': 'value1', 'key2': 'value2'} # создаём словарь для записи
# asterodb.set('dict1', json.dumps(dict1)) # с помощью функции dumps() из модуля json превратим наш словарь в строчку
# converted_dict = json.loads(asterodb.get('dict1')) # с помощью знакомой нам функции прерващаем данные полученные из кеша обратно в словарь
# print(type(converted_dict)) # убеждаемся что мы получили действительно словарь
# print(converted_dict) # ну и выводим его содержание
# asterodb.delete('dict1')
# print(asterodb.get('dict1'))

