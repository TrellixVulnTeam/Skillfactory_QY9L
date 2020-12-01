import random


class Field:
    def __init__(self):
        self.u_field = {}
        self.ai_field = {}

    def draw_fields(self):
        print(" |1|2|3|4|5|6|           |1|2|3|4|5|6|")

        for i in range(6):
            field = (str(i + 1) + "|")
            for j in range(6):
                field = field + self.u_field.get(i*6+j+1) + "|"

            field = field + (10*" ")
            field = field + (str(i + 1) + "|")

            for j in range(6):
                field = field + self.ai_field.get(i*6+j+1) + "|"

            print(field)

    def u_init(self):
        for i in range(37):
            a = random.randint(0, 1)
            if a == 0:
                self.u_field[i] = "0"
            else:
                self.u_field[i] = "X"
        return self.u_field

    def ai_init(self):
        for i in range(37):
            a = random.randint(0, 1)
            if a == 0:
                self.ai_field[i] = "0"
            else:
                self.ai_field[i] = "X"
        return self.ai_field
