from PIL import Image, ImageDraw, ImageFont
import random


numberOfCalls = 100
sizeOfPicture = 500

img = Image.new('RGB', (sizeOfPicture, sizeOfPicture), color=(255, 255, 255))
draw = ImageDraw.Draw(img)


def nahodne_cislo():
    x = random.randint(0, sizeOfPicture)
    y = random.randint(0, sizeOfPicture)
    test = random.randint(100000, 999999)
    draw.text((x, y), str(test), (0, 0, 0))


for i in range(numberOfCalls):
    nahodne_cislo()

img.save("/Users/martinpoupa/Documents/GitHub/ZakladyAlgoritmizace/lekce09/export.png")
