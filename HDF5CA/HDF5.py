import timeit
from collections import Counter
from random import randrange

import h5py

xSize = 1000
ySize = 1000
random_spawn_amount = 1000
x_amount_grains = 20
y_amount_grains = 20
neighbourhood_string = 'moore'
colors = []

file = h5py.File("grainGrowth.hdf5", 'w')
grains_dataset = file.create_dataset("grainGrowth", (xSize, ySize), dtype=int)
grains_next_step_dataset = file.create_dataset("grains_next_step", (xSize, ySize), dtype=int)


def draw_color():
    random_color = randrange(1, ySize * ySize)
    while random_color in colors:
        random_color = randrange(1, ySize * ySize)
    colors.append(random_color)
    return random_color


def get_most_frequent_element(neighbourhood):
    neighbourhood_colors = []
    for grains in neighbourhood:
        for grain in grains:
            if grain != 0:
                neighbourhood_colors.append(grain)
    if neighbourhood_colors:
        most_frequent_element = Counter(neighbourhood_colors)
        return most_frequent_element.most_common(1)[0][0]
    else:
        return 0


def homogeneous_spawn():
    y = ySize / y_amount_grains
    x = xSize / x_amount_grains
    x_offset = int((ySize - (x_amount_grains - 1) * x) / 2)
    y_offset = int((ySize - (y_amount_grains - 1) * y) / 2)
    for counter_x in range(x_amount_grains):
        for counter_y in range(y_amount_grains):
            random_color = draw_color()
            y_grain = int(counter_y * y + y_offset)
            x_grain = int(counter_x * x + x_offset)
            grains_dataset[x_grain, y_grain] = random_color
            grains_next_step_dataset[x_grain, y_grain] = random_color


def random_spawn():
    points = []
    for counter in range(random_spawn_amount):
        random_color = draw_color()
        x_grain = randrange(xSize)
        y_grain = randrange(ySize)
        while (x_grain, y_grain) in points:
            x_grain = randrange(xSize)
            y_grain = randrange(ySize)
        points.append((x_grain, y_grain))
        grains_dataset[x_grain, y_grain] = random_color
        grains_next_step_dataset[x_grain, y_grain] = random_color


def handle_corner(x_counter, y_counter):
    if x_counter == 0 and y_counter == 0:
        neighbourhood = grains_dataset[0:2, 0:2]
        if neighbourhood_string == 'neuman':
            neighbourhood = [[neighbourhood[0, 1], neighbourhood[1, 0]]]
        change_grain_state(neighbourhood, x_counter, y_counter)

    elif x_counter == 0 and y_counter == ySize - 1:
        neighbourhood = grains_dataset[0:2, ySize - 2:ySize]
        if neighbourhood_string == 'neuman':
            neighbourhood = [[neighbourhood[0, 0], neighbourhood[1, 1]]]
        change_grain_state(neighbourhood, x_counter, y_counter)

    elif x_counter == xSize - 1 and y_counter == 0:
        neighbourhood = grains_dataset[xSize - 2:xSize, 0:2]
        if neighbourhood_string == 'neuman':
            neighbourhood = [[neighbourhood[0, 0], neighbourhood[1, 1]]]
        change_grain_state(neighbourhood, x_counter, y_counter)

    elif x_counter == xSize - 1 and y_counter == ySize - 1:
        neighbourhood = grains_dataset[xSize - 2:xSize, ySize - 2:ySize]
        if neighbourhood_string == 'neuman':
            neighbourhood = [[neighbourhood[0, 1], neighbourhood[1, 0]]]
        change_grain_state(neighbourhood, x_counter, y_counter)


def handle_top_and_bottom_edge(x_counter, y_counter):
    if x_counter == 0 and y_counter != 0 and y_counter != ySize - 1:
        neighbourhood = grains_dataset[0:2, y_counter - 1:y_counter + 2]
        if neighbourhood_string == 'neuman':
            neighbourhood = [[neighbourhood[0, 0], neighbourhood[0, 2], neighbourhood[1, 1]]]
        change_grain_state(neighbourhood, x_counter, y_counter)

    elif x_counter == xSize - 1 and y_counter != 0 and y_counter != ySize - 1:
        neighbourhood = grains_dataset[xSize - 2:xSize, y_counter - 1:y_counter + 2]
        if neighbourhood_string == 'neuman':
            neighbourhood = [[neighbourhood[0, 1], neighbourhood[1, 0], neighbourhood[1, 2]]]
        change_grain_state(neighbourhood, x_counter, y_counter)


def handle_right_and_left_edge(x_counter, y_counter):
    if x_counter != 0 and y_counter == 0 and x_counter != xSize - 1:
        neighbourhood = grains_dataset[x_counter - 1:x_counter + 2, 0:2]
        if neighbourhood_string == 'neuman':
            neighbourhood = [[neighbourhood[0, 0], neighbourhood[1, 1], neighbourhood[2, 0]]]
        change_grain_state(neighbourhood, x_counter, y_counter)

    elif x_counter != 0 and y_counter == ySize - 1 and x_counter != xSize - 1:
        neighbourhood = grains_dataset[x_counter - 1:x_counter + 2, ySize - 2:ySize]
        if neighbourhood_string == 'neuman':
            neighbourhood = [[neighbourhood[0, 1], neighbourhood[1, 0], neighbourhood[2, 1]]]
        change_grain_state(neighbourhood, x_counter, y_counter)


def handle_centre(x_counter, y_counter):
    if x_counter != 0 and y_counter != 0 and x_counter != xSize - 1 and y_counter != ySize - 1:
        neighbourhood = grains_dataset[x_counter - 1:x_counter + 2, y_counter - 1:y_counter + 2]
        if neighbourhood_string == 'neuman':
            neighbourhood = [[neighbourhood[0, 1], neighbourhood[1, 0], neighbourhood[2, 1], neighbourhood[1, 2]]]
        change_grain_state(neighbourhood, x_counter, y_counter)


def change_grain_state(neighbourhood, x_counter, y_counter):
    new_state = get_most_frequent_element(neighbourhood)
    if new_state != 0:
        grains_next_step_dataset[x_counter, y_counter] = new_state


def change_next_step():
    global grains_dataset
    global grains_next_step_dataset
    grains_name = grains_dataset.name
    next_step_name = grains_next_step_dataset.name
    grains_dataset = file[next_step_name]
    grains_next_step_dataset = file[grains_name]


def simulation():
    # homogeneous_spawn()
    random_spawn()
    step_to_end = xSize * ySize
    while step_to_end > 0:

        step_to_end = xSize * ySize
        for x_counter in range(xSize):
            for y_counter in range(ySize):
                if grains_dataset[x_counter, y_counter] == 0:
                    handle_corner(x_counter, y_counter)
                    handle_top_and_bottom_edge(x_counter, y_counter)
                    handle_right_and_left_edge(x_counter, y_counter)
                    handle_centre(x_counter, y_counter)
                else:
                    grains_next_step_dataset[x_counter, y_counter] = grains_dataset[x_counter, y_counter]
                    step_to_end -= 1
        change_next_step()
        print(step_to_end)


print("START")
start = timeit.default_timer()
simulation()
stop = timeit.default_timer()
print('Time: ', stop - start)
file.close()
print("STOP")
