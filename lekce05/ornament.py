from PIL import Image, ImageDraw





img = Image.new('RGB', (150, 150), color = (255, 255, 255))


draw = ImageDraw.Draw(img)

def rectangle2(x ,y ,l ,h, Fill, Outline):
    x1 = x + l
    y1 = y + h
    draw.rectangle((x1, y1, x, y), fill=Fill, outline=Outline)

white = (255, 255, 255)
black = (0, 0, 0)

rectangle2(50 ,50 ,50 ,50, white, black)

rectangle2(50 ,25 ,25 ,25, white, black)
rectangle2(25 ,75 ,25 ,25, white, black)
rectangle2(100 ,50 ,25 ,25, white, black)
rectangle2(75 ,100 ,25 ,25, white, black)

img.save("export.png")
