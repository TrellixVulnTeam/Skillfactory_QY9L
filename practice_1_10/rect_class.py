class Rectangle:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def getwidth(self):
        return self.width

    def get_height(self):
        return self.height

    def get_coords(self):
        res = ("{}({}, {}, {}, {})".format(__class__.__name__, self.x, self.y, self.width, self.height))
        return res

    def get_area(self):
        return self.width * self.height
