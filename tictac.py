import random
import sys


def field_print():  # отрисовка поля
    f = 0
    while f < 3:  # шлепаем строки в цикле
        print(xo_field.get(f*3+1), "|", xo_field.get(f*3+2), "|", xo_field.get(f*3+3))  # за раз - одну строку
        if f < 2:  # разделители строк (на 1 меньше чем строк)
            print("- + - + -")
        f += 1


def xo_input():  # Ход пользователя
    print("Выберите ячейку, куда хотите поставить", user_mark)
    step_cell = int(input())  # вводим данные (1-9)
    if (xo_field.get(step_cell)) == "." or 0 > step_cell > 9:  # проверяем что ввели и пуста ли ячейка с этим номером
        print("Выбрана ячейка", str(step_cell))
        (xo_field[step_cell]) = str(user_mark)  # ставим в выбранную ячейку словаря Х или О
        field_print()  # заново печатаем поле из словаря
        step_select()  # уходим на переключение хода
    else:
        print("Неверно введен номер ячейки")
        xo_input()  # Заново вводим ячейку


def comp_step():  # Ход компьютера
    step_cell = random.randint(1, 9)  # случайно выбираем ячейку
    if (xo_field.get(step_cell)) == ".":  # проверяем ячейку на пустоту
        print("Ход компьютера. Выбрана ячейка", str(step_cell))
        (xo_field[step_cell]) = str(comp_mark)  # и пишем символ Х или О
        field_print()  # рисуем заново поле
        step_select()  # и идем на выбор шага
    else:
        comp_step()  # если ячейка с выбранным числом - занята, то заново


def step_select():  # выбор кто ходит
    global flag  # глобальный триггер хода
    global step  # номер шага
    if step > 4:  # на пятом шаге
        check()  # вызываем функцию проверки
    if step == 9:  # на десятом ничья
        print("Ничья")
        sys.exit()
    step += 1  # увеличиваем счетчик шагов
    print("Ход", step)

    if flag == 1:  # Если флаг поднят
        flag = 0  # Опустить флаг
        if user_mark == "X":  # Если юзер ходит Х
            xo_input()
        else:
            comp_step()  # иначе отдаем компу

    else:  # если флаг опущен
        flag = 1  # поднимаем
        if user_mark == "O":  # если юзер ходит О
            xo_input()  # то вызываем функцию ввода
        else:
            comp_step()  # иначе отдаем компу


def check():
    win_state = ['123', '456', '789', '147', '258', '369', '159', '357']  # блок выигрышных комбинаций ячеек
    for i in win_state:  # берем каждую комбинацию
        j = (xo_field[int(i[0])]+xo_field[int(i[1])]+xo_field[int(i[2])])  # и читаем с поля данные
        if j == "XXX":  # Если во всех трех ячейках Х
            print("'X' Выиграл")  # то поздравляем
            sys.exit()
        if j == "OOO":  # Аналогично доя О
            print("'O' Выиграл")
            sys.exit()
        # print(xo_field[int(i[0])],xo_field[int(i[1])],xo_field[int(i[2])])
        # if xo_field[int(i[0])] and xo_field[int(i[1])] and


print("+++Крестики-нолики+++")
print("Нумерация ячеек на поле")
a = 0
while a < 3:  # рисуем поле с картой ячеек (1-9)
    print((a*3+1), "|", (a*3+2), "|", (a*3+3))
    if a < 2:
        print("- + - + -")
    a += 1
x = 1
xo_field = {}  # Заполняем словарь точками
while x < 10:
    xo_field[x] = "."
    x += 1
xo = random.randint(0, 1)  # рандомайзер выбирает, за кого Х или О будет играть юзер

if xo == 1:
    user_mark = "X"
    comp_mark = "O"
else:
    user_mark = "O"
    comp_mark = "X"

step = 0  # Обнуляем переменные шага
flag = 1  # И шага
print("Вы играете:", user_mark)
print("Комп играет:", comp_mark)
input("Нажмите Enter для продолжения")  # задержка начального экрана с картой и вводными данными игры

field_print()  # вывод пустого поля первоначально
step_select()  # и бежим на выбор шага
