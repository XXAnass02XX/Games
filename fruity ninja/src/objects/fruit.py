from abc import ABC, abstractmethod

class Fruit(ABC):
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def move(self):
        pass
        #self.position.move()