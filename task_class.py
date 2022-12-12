class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point: Point):
        return True if (self.x - point.x) ** 2 + (self.y - point.y) ** 2 <= self.radius ** 2 else False
