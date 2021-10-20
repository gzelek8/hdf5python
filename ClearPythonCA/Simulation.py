from collections import Counter

import Grain


class Simulation:

    def __init__(self, grain_growth, neighbourhood, neigh):
        self.GrainGrowth = grain_growth
        self.Neighbourhood = neighbourhood
        self.Neigh = neigh

    def calculate_simulation(self):
        end = self.GrainGrowth.xSize * self.GrainGrowth.ySize
        while end > 0:
            end = self.GrainGrowth.xSize * self.GrainGrowth.ySize
            for counter_x, grains in enumerate(self.GrainGrowth.Grains):
                for counter_y, grain in enumerate(grains):
                    if grain is None:
                        grain_neighbourhood = []
                        if self.Neigh == 'moore':
                            grain_neighbourhood = self.Neighbourhood.add_moore_neighbourhood(counter_x, counter_y)
                        elif self.Neigh == 'neuman':
                            grain_neighbourhood = self.Neighbourhood.add_von_neuman_neighbourhood(counter_x, counter_y)
                        new_state = Simulation.get_most_frequent_element(grain_neighbourhood)
                        if new_state:
                            self.GrainGrowth.GrainsNextStep[counter_x][counter_y] = Grain.Grain(counter_x, counter_y,
                                                                                                new_state)
                    else:
                        self.GrainGrowth.GrainsNextStep[grain.X][grain.Y] = grain
            amount_of_grains = self.add_next_step_state()
            end -= amount_of_grains
            print(end)

    def add_next_step_state(self):
        amount_of_grains = 0
        for grains in self.GrainGrowth.GrainsNextStep:
            for grain in grains:
                if grain:
                    amount_of_grains += 1
                    self.GrainGrowth.Grains[grain.X][grain.Y] = grain
        return amount_of_grains

    @staticmethod
    def get_most_frequent_element(neighbourhood):
        colors = []
        for grain in neighbourhood:
            if grain:
                if grain.Color:
                    colors.append(grain.Color)
        if colors:
            most_frequent_element = Counter(colors)
            return most_frequent_element.most_common(1)[0][0]
        else:
            return None
