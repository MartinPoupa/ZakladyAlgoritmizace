from PIL import Image, ImageDraw
import random


numberOfBox = 21
boxSize = 10
wight = (255, 255, 255)
black = (0, 0, 0)


def rectangle2(draw, x, y, lenth, hight, Fill):
    x1 = x + lenth
    y1 = y + hight
    draw.rectangle((x1, y1, x, y), fill=Fill)


img = Image.new('RGB', (numberOfBox*boxSize, numberOfBox*boxSize), color=wight)
draw = ImageDraw.Draw(img)

for x in range(numberOfBox):
    for y in range(numberOfBox):
        if random.randint(0, 1):
            rectangle2(draw, (x * boxSize), (y * boxSize), boxSize, boxSize, Fill=black)

img.save("/Users/martinpoupa/Documents/GitHub/ZakladyAlgoritmizace/lekce10/export.png")
