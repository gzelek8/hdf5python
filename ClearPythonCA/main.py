import GrainGrowth
import Neighborhood
import Simulation
import timeit


if __name__ == '__main__':
    xSize = 100
    ySize = 100
    neigh = 'neuman'
    print("START")
    start = timeit.default_timer()
    grain_growth = GrainGrowth.GrainGrowth(xSize, ySize)
    neighbourhood = Neighborhood.Neighborhood(xSize, ySize, grain_growth.Grains, grain_growth.GrainsNextStep)
    simulation = Simulation.Simulation(grain_growth, neighbourhood, neigh)
    if neigh == 'moore':
        grain_growth.random_spawn(5)
    elif neigh == 'neuman':
        grain_growth.random_spawn(5)
    simulation.calculate_simulation()
    stop = timeit.default_timer()
    print('Time: ', stop - start)
    print("STOP")
    with open('test.txt', 'w') as file:
        for line in grain_growth.Grains:
            for el in line:
                file.write(str(el.Color) + '\t')
            file.write('\n')
    # grain_xd = []
    # for grains in grain_growth.Grains:
    #     xd = []
    #     for grain in grains:
    #         xd.append(grain.Color)
    #     grain_xd.append(xd)
    # for el in grain_xd:
    #     print(el)