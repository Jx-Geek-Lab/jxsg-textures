import os
import math
import random
from PIL import Image, ImageDraw

cell = 16                               # Cell size in pixels

grid_x = 64                             # Grid size by X in cells
grid_y = 64                             # Grid size by Y in cells

img_wdth = grid_x * cell                # Image width
img_hght = grid_y * cell                # Image height

quantity = 10                           # Number of generations

name = "grass"

tone = 1

def l(v):
    v = math.floor(v * (1 + tone))
    if v > 255:
        return 255
    return v

def d(v):
    v = math.floor(v * tone)
    if v < 0:
        return 0
    return v

fn = d

def conv(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def save(image, index):
    filename = name + "_" + "0" * (4 - len(str(index))) + str(index) + ".png"
    if os.path.exists(filename):
        os.remove(filename)
    image.save(filename, "PNG")

grane = [
    [conv("0b0c07"), 1],
    [conv("2a323d"), 3],
    [conv("7e8484"), 3],
    [conv("b8c2c1"), 3],
    [conv("754433"), 4],
    [conv("ac644c"), 4],
    [conv("d09c84"), 4],
    [conv("c75f3c"), 7],
    [conv("ecae89"), 7],
]

grass = [
    [conv("4b5d55"), 5],
    [conv("536b58"), 5],
    [conv("5e7a57"), 5],
    [conv("6b7d53"), 3],
    [conv("7b8c5c"), 3],
    [conv("535f57"), 1],
    [conv("b6af64"), 1],
]

palette = []

samples = grass

for sample in samples:
    for weight in range(sample[1]):
        palette.append(sample[0])

for z in range(quantity):

    img = Image.new("RGB", (img_wdth, img_hght))
    draw = ImageDraw.Draw(img)
    
    for x in range(grid_x):
        for y in range(grid_y):
            r, g, b = palette[random.randint(0, len(palette) - 1)]
            draw.rectangle((x * cell, y * cell, x * cell + (cell - 1), y * cell + (cell - 1)), fill=(r, g, b))
            
    save(img, z)
