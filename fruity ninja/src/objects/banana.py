from fruit import Fruit

class Banana(Fruit):
    dy = 2
    length = 2
    width = 4
    color = 'YELLOW'
    def __init__(self, position):
        super().__init__(position)
        self.life = 2

    def move(self):
        self.position.move(self.dy)

    def kick(self):
        self.life -= 1


