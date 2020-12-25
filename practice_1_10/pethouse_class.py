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
        self.clDB.append(("Иван", "Иванов", 500))
        self.clDB.append(("Петр", "Петров", 200))
        self.clDB.append(("Василий", "Сидоров", -50))


class Clients(DB):

    def cl_list(self):
        for (i, j, k) in self.clDB:
            print("{} {}".format(i, j))

    def cl_find(self, fl_name):
        self.flname = fl_name
        cl_filter = []
        for (i, j, k) in self.clDB:
            if i == self.flname or j == self.flname:
                cl_filter.append((i, j, k))
        return cl_filter


class Guests(DB):
    pass
