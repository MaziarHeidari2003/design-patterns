from abc import ABC

class Shape(ABC):
    def __str__(self):
        return ''
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def resize(self, radius):
        self.radius = radius


    def __str__(self):
        return f'A circle of radius {self.radius}'

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def __str__(self):
        return f'a square with side {self.side}'


class ColoredShaped(Shape):
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape


    def __str__(self):
        return f'{self.shape} has the color {self.color}'    



if __name__ == "__main__":
    c1 = Circle(2)
    c2 = ColoredShaped(c1,'red')
    print(c2)
