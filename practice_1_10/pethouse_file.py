from pethouse_class import Cat, Clients, Guests

cats = [("Сэм", "Мальчик", 2), ("Барон", "Мальчик", 2)]


def menu():
    print("Выберите пункт меню")
    print("1. Животные")
    print("2. Клиенты и баланс")
    print("3. Корпоратив")
    print("0. Выход из программы")
    choice_0 = int(input("[1,2,3,0]-->"))

    if choice_0 == 1:
        for cat_name, cat_sex, cat_age in cats:
            cat_ex = Cat(cat_name, cat_sex, cat_age)
            print("Кот {0}, {1}, возраст {2}".format(cat_ex.name, cat_ex.sex, cat_ex.age))
        print("Enter для возврата в меню")
        input("-->")
        menu()

    elif choice_0 == 2:
        cl_menu()

    elif choice_0 == 3:
        g_menu()

    elif choice_0 == 0:
        print("Выход из программы")
        exit()

    else:
        print("Выберите один из пунктов меню [1,2,3,0]")
        menu()


def cl_menu():

    print("===Клиенты и баланс===/Выберите пункт меню")
    print("1. Список клиентов")
    print("2. Поиск клиента по имени и фамилии")
    print("3. Добавить клиента")
    print("0. Возврат в главное меню")
    choice_1 = int(input("[1,2,3,0]-->"))

    if choice_1 == 1:
        print("---Полный список клиентов---")
        clients.list()
        input("Enter для продолжения -->")
        cl_menu()

    elif choice_1 == 2:
        search = input("Введите имя или фамилию --> ")
        result = clients.find(search)

        if len(result) > 0:
            for (i, j, k) in result:
                print("Клиент: {} {}, Баланс: {}".format(i, j, k))
                input("Enter для продолжения -->")
        else:
            print("Клиент не найден")
        cl_menu()

    elif choice_1 == 3:
        f_name = input("Введите имя клиента --> ")
        l_name = input("Введите фамилию клиента --> ")
        clients.add(f_name, l_name)
        print("Клиент {} {} добавлен. Баланс = 0".format(f_name, l_name))
        cl_menu()

    elif choice_1 == 0:
        menu()
    else:
        print("Выберите один из пунктов меню [1,2,3,0]")
        menu()


def g_menu():

    print("===Корпоратив===/Выберите пункт меню")
    print("1. Список гостей")
    print("2. Поиск гостей по имени и фамилии")
    print("3. Добавить гостя")
    print("0. Возврат в главное меню")
    choice_1 = int(input("[1,2,3,0]-->"))

    if choice_1 == 1:
        print("---Полный список гостей корпоратива---")
        guests.list()
        input("Enter для продолжения -->")
        g_menu()

    elif choice_1 == 2:
        search = input("Введите имя или фамилию --> ")
        result = guests.find(search)

        if len(result) > 0:
            for (i, j, k, l) in result:
                print("{} {}, г.{}, статус:{}".format(i, j, k, l))
                input("Enter для продолжения -->")
        else:
            print("Указанный гость в списке не найден")
        g_menu()

    elif choice_1 == 3:
        f_name = input("Введите имя гостя --> ")
        l_name = input("Введите фамилию гостя --> ")
        city = input("Введите город проживания гостя --> ")
        status = input("Введите статус гостя --> ")
        guests.add(f_name, l_name, city, status)
        print("Гость {} {} из г.{} добавлен. Статус: {}".format(f_name, l_name, city, status))
        g_menu()

    elif choice_1 == 0:
        menu()

    else:
        print("Выберите один из пунктов меню [1,2,3,0]")
        menu()


clients = Clients()
guests = Guests()
menu()
