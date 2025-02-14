from abc import ABC
from enum import Enum,auto

class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')



class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


class HotDrinkFact(ABC):
    def prepare(self,amount):
        pass


class HotTea(HotDrinkFact):
    def prepare(self, amount):
        print(f'tea {amount}')
        return Tea()

class HotCoffee(HotDrinkFact):
    def prepare(self,amount ):
        print(f'coffee {amount}')    


class HotDrinkMachine():
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True 
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name +'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name,factory_instance))
