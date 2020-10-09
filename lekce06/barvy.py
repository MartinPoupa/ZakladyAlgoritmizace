from PIL import Image, ImageDraw

img = Image.new('RGB', (120 + 90 + 120 + 60 , 120 + 90 + 120 + 60 ), color = (255, 255, 255))

draw = ImageDraw.Draw(img)

def rectangle2(x ,y ,l ,h, Fill):
    x1 = x + l
    y1 = y + h
    draw.rectangle((x1, y1, x, y), fill=Fill)

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255,255,0)
red = (255, 0, 0)
green = (0, 255, 0)


rectangle2(30, 150, 120 + 90 + 120, 90, red)
rectangle2(150, 30, 90, 120 + 90 + 120, green)
rectangle2(150, 150, 90, 90, yellow)

img.save("export.png")
