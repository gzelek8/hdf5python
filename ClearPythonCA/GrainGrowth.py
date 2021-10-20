from random import randrange

import Grain


class GrainGrowth:

    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        self.Grains = [[None for x in range(xSize)] for y in range(ySize)]
        self.GrainsNextStep = [[None for x in range(xSize)] for y in range(ySize)]
        self.Colors = []

    def draw_color(self):
        random_color = randrange(self.ySize * self.ySize)
        while random_color in self.Colors:
            random_color = randrange(self.ySize * self.ySize)
        self.Colors.append(random_color)
        return random_color

    def check_is_free(self, x, y):
        print(str(x) + ' ' + str(y))
        if self.Grains[x][y] is None:
            return False
        else:
            return True

    def random_spawn(self, grains_amount):
        for counter in range(grains_amount):
            x = randrange(self.ySize)
            y = randrange(self.ySize)
            while self.check_is_free(x, y):
                x = randrange(self.ySize)
                y = randrange(self.ySize)
            random_color = self.draw_color()
            self.Grains[x][y] = Grain.Grain(x, y, random_color)

    def homogeneous_spawn(self, x_grain_amount, y_grain_amount):
        y = self.ySize / y_grain_amount
        x = self.xSize / x_grain_amount
        x_offset = int((self.ySize - (x_grain_amount - 1) * x) / 2)
        y_offset = int((self.ySize - (y_grain_amount - 1) * y) / 2)
        for counter_x in range(x_grain_amount):
            for counter_y in range(y_grain_amount):
                random_color = self.draw_color()
                y_grain = int(counter_y * y + y_offset)
                x_grain = int(counter_x * x + x_offset)
                self.Grains[x_grain][y_grain] = Grain.Grain(x_grain, y_grain, random_color)
