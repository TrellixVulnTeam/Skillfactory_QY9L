class Client:
    def __init__(self, firstname, lastname, wallet):
        self.firstname = firstname
        self.lastname = lastname
        self.__wallet = wallet

    def get_info(self):
        return "Клиент - " + self.firstname + " " + self.lastname + ", " + \
               "Баланс - " + str(self.wallet)

    def set_wallet(self, wallet):
        if wallet > 0 and isinstance(wallet, int):
            self.__wallet == wallet


class Database:
    def __init__(self):
        self.db = []

    def new_client(self, firstname, lastname, wallet):
        client = Client(firstname, lastname, wallet)
        self.db.append((firstname, lastname, wallet))

    def find_client(self, firstname):
        list_client = []
        for (c_firstname, c_lastname, c_wallet) in self.db:
            if c_firstname == firstname or c_lastname == firstname:
                list_client.append((c_firstname, c_lastname, c_wallet))
        return list_client
    def client_list(self):
        for i in self.db:
            print(i)

client_db = Database()


def start():
    print(30*"=")
    choice = int(input("1- добавить клиента\n2- найти клиента\n3- список клиентов\nВыберите[1,2,3] "))
    if choice == 1:
        cl_new_fname = input("имя ")
        cl_new_lname = input("Фамилия ")
        cl_new_wallet = input("Баланс ")
        client_db.new_client(cl_new_fname, cl_new_lname, cl_new_wallet)
        start()
    elif choice == 2:
        a = input("Введите имя или фамилию клиента: ")
        result = client_db.find_client(a)
        for (i,j,k) in result:
            print("{0} {1}, баланс: {2}руб.".format(i,j,k))
        start()
    elif choice == 3:
        client_db.client_list()
        start()
    else:
        print("Выберите 1,2,3")
        start()

#app = Database()
client_db.new_client("Иван","Иванов","500")
client_db.new_client("Василий","Иванов","100")
client_db.new_client("Петр","Петров","200")
client_db.client_list()
start()