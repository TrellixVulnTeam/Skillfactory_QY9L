from random import randint


class Player:
    def __init__(self, field, enemy):
        self.field = field
        self.enemy = enemy
    def ask(self):
        raise NotImplementedError()
    def move (self):
        while True:
            try:
                shot_coords = self.ask()
                repeat = self.enemy.shot(shot_coords)
                return(repeat)
            except FieldException as e:
                print(e)

class AI(Player):
    def ask(self):
        ai_move =  Point(randint(0,5),randint(0,5))
        print(f"Ход AI: {ai_move.x+1}-{ai_move.y+1}")
        return ai_move
class User(Player):
    def ask(self):
        while True:
            coords = input("Введите координаты выстрела:").split()


            if len(coords) != 2:
                print("Ошибка! Введите 2 координаты через пробел")


            try:
                x,y = coords
            except ValueError:
                print("не введены координаты!!!")
                continue
            if not (x.isdigit()) or not (y.isdigit()):
                print("Введите числа")
                continue
            x,y = int(x), int(y)

            return Point(x-1,y-1)
class Game:
    def greeting(self):
        print("Добро пожаловать в 'Морской бой'")
        print("Формат ввода координат: х у")
        print("х - номер строки, y - номер столбца")
        input("Нажмите Enter для продолжения")

    def __init__(self, size = 6):
        self.size = size
        user = self.init_field()
        comp = self.init_field()
        comp.mask = True
        self.ai = AI(comp, user)
        self.user = User(user,comp)
    def loop(self):
        flag =0

        while True:
            print(20 * "-")
            print("Поле игорька:")
            print(self.user.field)
            print("Поле AI:")
            print(self.ai.field)
            if flag %2 == 0:
                print(20 * "-")
                print("Ход игорька:")
                repeat = self.user.move()
            else:
                print(20 * "-")
                print("Ход AI:")
                repeat = self.ai.move()

            if repeat:
                flag -= 1
            if self.ai.field.count == 7:
                print(20*"-")
                print("Игорек выиграл")
                break
            if self.user.field.count == 7:
                print(20*"-")
                print("AI выиграл")
                break
            flag += 1

    def init_field(self):
        field = None
        while field is None:
            field = self.ships_init(self.size)
        return field

    def ships_init(self, size):
        ships = [3, 2, 2, 1, 1, 1, 1]
        field = Field(self.size,0)
        attempts = 0
        for i in ships:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Point(randint(0, self.size), randint(0, self.size)), i, randint(0, 1))
                try:
                    field.set(ship)
                    break
                except FieldWrongShipCoordsException:
                    pass
        field.begin()
        return field
class Field:
    def __init__(self, size, mask):
        self.size = size
        self.mask = mask
        self.count = 0
        self.field = [["O"]*size for _ in range(size)]
        self.busy = []
        self.ships = []

    def set(self, ship):
        for i in ship.coords:
            if self.outboard(i) or i in self.busy:
                raise FieldWrongShipCoordsException()
        for j in ship.coords:
            self.field[j.x][j.y] = "■"
            self.busy.append(j)
        self.ships.append(ship)
        self.around(ship)

    def around(self, ship, verb=False):
        near = [(-1,0),(1,0),(0,0),(0,1),(0,-1)]
        for d in ship.coords:
            for dx, dy in near:
                cur = Point(d.x + dx, d.y + dy)
                if not(self.outboard(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)


    def __str__(self):
        string = ''
        string += ' |1|2|3|4|5|6|'
        for i, j in enumerate(self.field):
            string += f"\n{i+1}|"+"|".join(j)+"|"
        if self.mask:
            string = string.replace("■","O")
        return string

    def outboard(self, cur):
        return not((0 <= cur.x < self.size) and (0 <= cur.y < self.size))

    def shot(self, point):
        if self.outboard(point):
            raise FieldOutException()
        if point in self.busy:
            raise FieldBusyException()
        self.busy.append(point)
        for ship in self.ships:
            if point in ship.coords:
                ship.points -=1
                self.field[point.x][point.y] = "X"
                if ship.points == 0:
                    self.count +=1
                    self.around(ship, True)
                    print("Убит!!!")
                    return False  # определяет будет ли повтор хода после уничтожения
                else:
                    print("Ранен!!!")
                    return True  # повтор хода после попадания
        self.field[point.x][point.y] = "T"
        print("Мимо!!!")
        return False  # передаем ход другому игорьку
    def begin(self):
        self.busy = []

class Ship:
    def __init__(self, startpoint, length, orient):
        self.startpoint = startpoint
        self.length = length
        self.points = length
        self.orient = orient

    def ship_hit(self, hit):
        return hit in self.coords

    @property
    def coords(self):
        ship_coords = []
        for i in range (self.length):
            cur_x = self.startpoint.x
            cur_y = self.startpoint.y
            if self.orient:
                cur_y +=i
            else:
                cur_x +=i
            ship_coords.append(Point(cur_x,cur_y))
        return ship_coords


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, coord):
        return self.x == coord.x and self.y == coord.y

class FieldException(Exception):
    pass

class FieldWrongShipCoordsException(FieldException):
    pass

class FieldOutException(FieldException):
    def __str__(self):
        return "Стреляем за пределы поля"
class FieldBusyException(FieldException):
    def __str__(self):
        return "Туда уже стреляли"
