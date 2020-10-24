from PIL import Image, ImageDraw

def rectangle2(draw, x ,y ,l ,h, Fill, Outline):
    x1 = x + l
    y1 = y + h
    draw.rectangle((x1, y1, x, y), fill=Fill, outline=Outline)

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255,192,3)
red = (185, 13, 8)
green = (170, 207, 66)
blue = (0,112,192)
blueLight = (4, 178, 241)
k = 10

class HomoBlog:
    
    def __init__(self, name):
        self.name = name
        self.img = Image.new('RGB', (19 * k, 22 * k), color = (255, 255, 255))
        self.draw = ImageDraw.Draw(self.img)
    
    def head(self):
        rectangle2(self.draw, 7 * k, 1 * k, 5 * k, 4 * k, blue, black)
        rectangle2(self.draw, 8 * k, 5 * k, 3 * k, 1 * k, blueLight, black)
    
    def heands(self):
        rectangle2(self.draw, 1 * k, 7 * k, 5 * k, 2 * k, yellow, black)
        rectangle2(self.draw, 13 * k, 7 * k, 5 * k, 2 * k, yellow, black)
        
    def leags(self):
        rectangle2(self.draw, 7 * k, 16 * k, 2 * k, 5 * k, red, black)
        rectangle2(self.draw, 10 * k, 16 * k, 2 * k, 5 * k, red, black)
        
    def body(self):
        rectangle2(self.draw, 6 * k, 6 * k, 7 * k, 10 * k, green, black)
        
    def a(self, export):
        self.img.save(export)
        
        
    
