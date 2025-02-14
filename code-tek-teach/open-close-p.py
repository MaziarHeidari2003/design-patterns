from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2 
    LARGE = 3


class Product:
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size


class Specification:
    def is_satisfied(self,item):
        pass

    def __and__(self,other):
        return AndSpecification(self,other)    

class Filter:
    def filter(self,items,spec):
        pass

class ColorSpecification(Specification):
    def __init__(self,color):
        self.color = color

    def is_satisfied(self,item):
        return item.color  == self.color


class SizeSpecification(Specification):
    def __init__(self,size):
        self.size = size

    def is_satitisfied(self,item):
        return item.size == self.size            


class AndSpecification(Specification):
    def __init__(self,spec1,spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)    

class BetterFilter(Filter):
    def filter(self,items,spec:Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item
                
    def filter_by_size(self,products,size):
        for p in products:
            if p.size == size:
                yield p    

tree = Product('tree',Color.GREEN,Size.LARGE)
car = Product('car',Color.GREEN,Size.MEDIUM)
sea = Product('sea',Color.BLUE,Size.LARGE)

products = [tree, car, sea]

bf = BetterFilter()

print('the green one')
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f'{p.name} is green')

print('based on the size')
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products,large):
    print(f'{p.name} is large')



large_blue = large and ColorSpecification(Color.BLUE)
for p in bf.filter(products,large_blue):
    print(f'{p.name} is large and blue')
