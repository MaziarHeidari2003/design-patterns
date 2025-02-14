from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass


class VectorRendere(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRendere(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self,renderer,radius):
        super().__init__(renderer)  
        self.radius = radius

    def draw(self):
        return self.renderer.render_circle(self.radius) 

    def resize(self, factor):
        return self.radius * factor   
    

raster = RasterRendere()
vector = VectorRendere()
circle = Circle(vector, 5)
circle.draw()
circle.resize(2)
circle.draw()
