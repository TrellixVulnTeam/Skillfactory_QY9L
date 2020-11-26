class Pet():
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    def getData(self):
        print("Имя:", self.name)
        print("Пол:", self.sex)
        print("Возраст:", self.age)
class Cat(Pet):
    def fullData(self):
        print("Кот", self.name,",", self.sex, ", с возрастом", self.age)