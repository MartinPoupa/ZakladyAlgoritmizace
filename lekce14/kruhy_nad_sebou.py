from PIL import Image, ImageDraw
import random


IMAGE_DIMENSIONS = 1000

MIN_RADIUS = 50
MAX_RADIUS =  200
CIRCUIT_COLOR_1 = "red"
CIRCUIT_COLOR_2 = "blue"


radius1 = random.randint(MIN_RADIUS, MAX_RADIUS)
radius2 = random.randint(MIN_RADIUS, MAX_RADIUS)


print(radius1)
print(radius2)

img = Image.new('RGB', (IMAGE_DIMENSIONS, IMAGE_DIMENSIONS ), color="white")
draw = ImageDraw.Draw(img)



if radius1 < radius2:
    draw.ellipse((IMAGE_DIMENSIONS / 2 - radius1, IMAGE_DIMENSIONS / 2 - radius1 * 2, IMAGE_DIMENSIONS / 2 + radius1, IMAGE_DIMENSIONS / 2), fill = CIRCUIT_COLOR_1, outline = CIRCUIT_COLOR_1)
    draw.ellipse((IMAGE_DIMENSIONS / 2 - radius2, IMAGE_DIMENSIONS / 2, IMAGE_DIMENSIONS / 2 + radius2, IMAGE_DIMENSIONS / 2 + radius2 * 2), fill = CIRCUIT_COLOR_2, outline = CIRCUIT_COLOR_2)
elif radius1 == radius2:
    draw.ellipse((IMAGE_DIMENSIONS / 2 - radius1 * 2, IMAGE_DIMENSIONS / 2 - radius1, IMAGE_DIMENSIONS / 2, IMAGE_DIMENSIONS / 2 + radius1), fill = CIRCUIT_COLOR_1, outline = CIRCUIT_COLOR_1)
    draw.ellipse((IMAGE_DIMENSIONS / 2, IMAGE_DIMENSIONS / 2 - radius2, IMAGE_DIMENSIONS / 2 + radius2 * 2, IMAGE_DIMENSIONS / 2 + radius2), fill = CIRCUIT_COLOR_2, outline = CIRCUIT_COLOR_2)
else: 
    draw.ellipse((IMAGE_DIMENSIONS / 2 - radius2, IMAGE_DIMENSIONS / 2 - radius2 * 2, IMAGE_DIMENSIONS / 2 + radius2, IMAGE_DIMENSIONS / 2), fill = CIRCUIT_COLOR_2, outline = CIRCUIT_COLOR_2)
    draw.ellipse((IMAGE_DIMENSIONS / 2 - radius1, IMAGE_DIMENSIONS / 2, IMAGE_DIMENSIONS / 2 + radius1, IMAGE_DIMENSIONS / 2 + radius1 * 2), fill = CIRCUIT_COLOR_1, outline = CIRCUIT_COLOR_1)

img.save("/Users/martinpoupa/Documents/GitHub/ZakladyAlgoritmizace/lekce14/export.png")
