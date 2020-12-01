class Pet:

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_data(self):
        print("Имя:", self.name)
        print("Пол:", self.sex)
        print("Возраст:", self.age)


class Cat(Pet):
    def full_data(self):
        print("Кот", self.name, ",", self.sex, ", с возрастом", self.age)


class DB:

    def __init__(self):
        self.clDB = []
        self.gDB = []
        # Отладочные данные
        self.clDB.append(("Иван", "Иванов", 500))
        self.clDB.append(("Петр", "Петров", 200))
        self.clDB.append(("Василий", "Сидоров", -50))

        self.gDB.append(("Иван", "Петров", "Москва", "Наставник"))
        self.gDB.append(("Петр", "Иванов", "Санкт-Петербург", "Волонтер"))
        self.gDB.append(("Алексей", "Васильев", "Н.Новгород", "Бригадир"))


class Clients(DB):

    def list(self):
        for (i, j, k) in self.clDB:
            print("{} {}".format(i, j))

    def find(self, fl_name):
        cl_filter = []

        for (i, j, k) in self.clDB:
            if i == fl_name or j == fl_name:
                cl_filter.append((i, j, k))
        return cl_filter

    def add(self, f_name, l_name):
        self.clDB.append((f_name, l_name, 0))


class Guests(DB):
    def list(self):
        for (i, j, k, l) in self.gDB:
            print("{} {}, г.{}, статус:{}".format(i, j, k, l))

    def find(self, fl_name):
        g_filter = []

        for (i, j, k, l) in self.gDB:
            if i == fl_name or j == fl_name:
                g_filter.append((i, j, k, l))
        return g_filter

    def add(self, f_name, l_name, g_city, g_status):
        self.gDB.append((f_name, l_name, g_city, g_status))
