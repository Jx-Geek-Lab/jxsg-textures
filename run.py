import os
import random
from PIL import Image, ImageDraw

cell = 16                               # Cell size in pixels

grid_x = 64                             # Grid size by X in cells
grid_y = 64                             # Grid size by Y in cells

img_wdth = grid_x * cell                # Image width
img_hght = grid_y * cell                # Image height

quantity = 1                            # Number of generations

name = "ground"

image = Image.open("samples/" + name + "/0001.png")
sw = 550
sh = 275
seek = (sw * 25) + 25

pixels = list(image.getdata())

palette = []

matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for row in range(10):
    for col in range(10):
        offset = ((row * (sw * 25)) + col * 25) + seek
        r = pixels[offset][0]
        g = pixels[offset][1]
        b = pixels[offset][2]
        n = str(r) + 'x' + str(g) + 'x' + str(b)
        if '0x0x0' != n and '255x255x255' != n:
            matrix[col] = matrix[col] + 1
            palette.append(pixels[offset])

for index, value in enumerate(matrix):
    print (chr(65 + index) + ' = ' + str(value))

def conv(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def save(image, index):
    filename = name + "_" + "0" * (4 - len(str(index))) + str(index) + ".png"
    if os.path.exists(filename):
        os.remove(filename)
    image.save(filename, "PNG")

for z in range(quantity):

    img = Image.new("RGB", (img_wdth, img_hght))
    draw = ImageDraw.Draw(img)
    
    for x in range(grid_x):
        for y in range(grid_y):
            r, g, b = palette[random.randint(0, len(palette) - 1)]
            draw.rectangle((x * cell, y * cell, x * cell + (cell - 1), y * cell + (cell - 1)), fill=(r, g, b))
            
    save(img, z)
