from PIL import Image, ImageDraw
import random



sloubce = 18
radky = 12
rozmery = 20
pocet = 3

img = Image.new('RGB', (radky*rozmery, sloubce*rozmery), color="white")
draw = ImageDraw.Draw(img)

def nakresliZnak(r, s):
    cr = r * rozmery + rozmery / 2
    cs = s * rozmery + rozmery / 2
    for i in range(random.randint(0, pocet)):
        x = random.randint(1, rozmery / 2)
        y = random.randint(1, rozmery / 2)
        draw.ellipse([(cr - x, cs - y), (cr + x, cs + y,)], outline = "black")
    

for i in range(radky):
    for j in range(sloubce):
        nakresliZnak(i, j)
        
img.save("/Users/martinpoupa/Documents/GitHub/ZakladyAlgoritmizace/lekce13/export.png")
