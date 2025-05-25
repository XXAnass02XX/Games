class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, dy):
        self.y += dy