from pico2d import *
import game_world

class P_missile:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if P_missile.image == None:
            P_missile.image = load_image('jet.png')
        self.x, self.y, self.velocity = x + 50, y-10, velocity
        self.sx, self.sy = x, y-20
        self.dx, self.dy = 1400, y-10
        self.time = 0

    def draw(self):
        self.image.clip_draw(630, 0, 60, 20, self.x, self.y)

    def update(self):
        self.x = (1 - self.time / 100)*(1 - self.time / 100)*self.sx + 2*(1 - self.time / 100)*(self.time / 100)*(self.sx + self.dx - 1600) + (self.time / 100)*(self.time / 100)*self.dx
        self.y = (1 - self.time / 100)*(1 - self.time / 100)*self.sy + 2*(1 - self.time / 100)*(self.time / 100)*(self.sy + self.dy-500) + (self.time / 100)*(self.time / 100)*self.dy
        self.time += 1

        if self.x > 1400 - 25:
            game_world.remove_object(self)
