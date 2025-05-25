from fruit import Fruit

class Apple(Fruit):
    dy = 1
    radius = 5
    color = 'RED'
    def __init__(self, position):
        super().__init__(position)
        self.life = 1

    def move(self):
        self.position.move(self.dy)

    def kick(self):
        self.life -= 1

