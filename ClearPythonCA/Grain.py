class Grain:
    count = 0

    def __init__(self, x, y, color):
        self.X = x
        self.Y = y
        self.Color = color
        self.Neighbors = []
