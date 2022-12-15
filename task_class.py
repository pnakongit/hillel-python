import math


class Frange:
    def __init__(self, first_arg=None, second_arg=None, step=1):
        if second_arg is None:
            self.start = 0
            self.stop = first_arg
        else:
            self.start = first_arg
            self.stop = second_arg
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step >= 0 and self.start >= self.stop:
            raise StopIteration
        elif self.step <= 0 and self.start <= self.stop:
            raise StopIteration
        value = self.start
        self.start += self.step
        return value


class Colorizer:
    colors = {"GREY": 90, "RED": 91, "GREEN": 92, "YELLOW": 93, "BLUE": 94, "PINK": 95, "TURQUOISE": 96}

    def __init__(self, color):
        self.color = Colorizer.colors.get(color, 0)

    def __enter__(self):
        print(f'\033[{self.color}m', end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'\033[0m', end='')


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def __contains__(self, point: Point):
        return True if (self.x - point.x) ** 2 + (self.y - point.y) ** 2 <= self.radius ** 2 else False


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):
        return self.width * self.height * math.sin(self.angle)


class Triangle(Parallelogram):
    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width, angle)

    def square(self):
        return super().square() / 2

    pass


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass
