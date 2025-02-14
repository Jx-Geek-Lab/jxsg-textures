import os
import random
from PIL import Image, ImageDraw

cell = 16                               # Cell size in pixels

grid_x = 640                            # Grid size by X in cells
grid_y = 640                            # Grid size by Y in cells

img_wdth = grid_x * cell                # Image width
img_hght = grid_y * cell                # Image height

quantity = 1                            # Number of generations

name = "grass"

image = Image.open("samples/grass/0000.png")
w, h = image.size

pixels = list(image.getdata())

palette = []

for row in range(int(w / 11)):
    for col in range(int(h / 11)):
        offset = (row * (77 * 11)) + col * 11
        pixel = pixels[offset]
        if 255 != pixel[0] or 255 != pixel[1] or 255 != pixel[2]:
            palette.append(pixels[offset])

print(palette)

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
