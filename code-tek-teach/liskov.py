class Reqtangel:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self,value):
        self._width = value

    @height.setter
    def height(self,value):
        self._height = value


    def __str__(self):
        return f"{self.height} and {self.width}"
    

class Square(Reqtangel):
    def __init__(self,size):
        Reqtangel.__init__(self,size,size) 

    @Reqtangel.width.setter
    def width(self,value):
        self._width = self._height = value

    @Reqtangel.width.setter
    def height(self,value):
        self._height = self._width = value
                     