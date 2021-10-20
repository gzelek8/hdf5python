class Neighborhood:

    def __init__(self, xSize, ySize, grains, grains_next_step):
        self.xSize = xSize
        self.ySize = ySize
        self.Grains = grains
        self.GrainsNextStep = grains_next_step

    def get_top_neighbourhood(self, x_grain, y_grain):
        if y_grain == 0:
            y = 0
        else:
            y = y_grain - 1
        return self.Grains[x_grain][y]

    def get_bottom_neighbourhood(self, x_grain, y_grain):
        if y_grain == self.ySize - 1:
            y = self.ySize - 1
        else:
            y = y_grain + 1
        return self.Grains[x_grain][y]

    def get_left_neighbourhood(self, x_grain, y_grain):
        if x_grain == 0:
            x = 0
        else:
            x = x_grain - 1
        return self.Grains[x][y_grain]

    def get_left_bottom_neighbourhood(self, x_grain, y_grain):
        if x_grain == 0 or y_grain == self.ySize - 1:
            x = x_grain
            y = y_grain
        else:
            x = x_grain - 1
            y = y_grain + 1
        return self.Grains[x][y]

    def get_right_bottom_neighbourhood(self, x_grain, y_grain):
        if x_grain == self.xSize - 1 or y_grain == self.ySize - 1:
            x = x_grain
            y = y_grain
        else:
            x = x_grain + 1
            y = y_grain + 1
        return self.Grains[x][y]

    def get_left_top_neighbourhood(self, x_grain, y_grain):
        if x_grain == 0 or y_grain == 0:
            x = x_grain
            y = y_grain
        else:
            x = x_grain - 1
            y = y_grain - 1
        return self.Grains[x][y]

    def get_right_top_neighbourhood(self, x_grain, y_grain):
        if x_grain == self.xSize - 1 or y_grain == 0:
            x = x_grain
            y = y_grain
        else:
            x = x_grain + 1
            y = y_grain - 1
        return self.Grains[x][y]

    def get_right_neighbourhood(self, x_grain, y_grain):
        if x_grain == self.xSize - 1:
            x = self.xSize - 1
        else:
            x = x_grain + 1
        return self.Grains[x][y_grain]

    def add_moore_neighbourhood(self, x, y):
        neighbourhood = [self.get_top_neighbourhood(x, y), self.get_bottom_neighbourhood(x, y),
                         self.get_right_top_neighbourhood(x, y), self.get_right_neighbourhood(x, y),
                         self.get_right_bottom_neighbourhood(x, y), self.get_left_top_neighbourhood(x, y),
                         self.get_left_neighbourhood(x, y), self.get_left_bottom_neighbourhood(x, y)]
        return neighbourhood

    def add_von_neuman_neighbourhood(self, x, y):
        neighbourhood = [self.get_top_neighbourhood(x, y), self.get_bottom_neighbourhood(x, y),
                         self.get_right_neighbourhood(x, y), self.get_left_neighbourhood(x, y)]
        return neighbourhood
