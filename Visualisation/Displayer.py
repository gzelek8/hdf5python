import random

from PIL import Image

#
# image = Image.new('RGB', (1000, 200))
# image.save("image.png", "PNG")
# for width in range(image.width):
#     for height in range(image.height):
#         image.putpixel((width, height), (random.randrange(255), random.randrange(255), random.randrange(255)))
# image.save("image.png", "PNG")

with open('text.txt', 'r') as file:
    colorId_and_colors_list = {}
    colors_list = []
    colorId_list = []
    counter = 0
    image = Image.new('RGB', (100, 100))
    for height, line in enumerate(file):
        for width, colorId in enumerate(line.split("\t")):
            if colorId != '\n':
                if int(colorId) not in colorId_list:
                    colorId = int(colorId)
                    random_color = (
                        random.randrange(255), random.randrange(255), random.randrange(255))
                    while random_color in colors_list:
                        random_color = (random.randrange(255), random.randrange(255), random.randrange(255))
                    colors_list.append(random_color)
                    colorId_list.append(colorId)
                    colorId_and_colors_list[colorId] = random_color
                for colorId_and_color in colorId_and_colors_list:
                    if colorId_and_color == int(colorId):
                        counter += 1
                        print(counter)
                        image.putpixel((height, width), colorId_and_colors_list[int(colorId)])
image.save("image3.png", "PNG")
