from pico2d import *

class Mapcounter:
    def __init__(self):
        self.image = load_image('cloud.png')   #밝은 하늘
        self.image2 = load_image('cloud_1.png')    #저녁 노을
        self.x = 0
        self.y = 400
        self.sx = 0
        self.sy = 400
        self.night = 0

    def update(self):
        self.x = self.x % 3200 + 10
        self.sx = self.sx % 3200 + 10
    def draw(self):
        if self.night == 0:
            self.image.clip_draw(0, 0, 1600, 800, -(self.x)+800, self.y, 1600, 800)
            self.image.clip_composite_draw(0, 0, 1600, 600, 0, 'h', -(self.sx)+2400, self.y, 1600, 800)
            self.image.clip_draw(0, 0, 1600, 800, -(self.x) + 4000, self.y, 1600, 800)
        else:
            self.image2.clip_draw(0, 0, 1600, 800, -(self.x) + 800, self.y, 1600, 800)
            self.image2.clip_composite_draw(0, 0, 1600, 600, 0, 'h', -(self.sx) + 2400, self.y, 1600, 800)
            self.image2.clip_draw(0, 0, 1600, 800, -(self.x) + 4000, self.y, 1600, 800)