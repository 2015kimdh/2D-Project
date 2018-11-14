from pico2d import *
import game_framework
import player
import game_world

class P_missile:
    image = None

    def __init__(self, x = 400, y = 300):
        if P_missile.image == None:
            P_missile.image = load_image('jet.png')
        self.x, self.y = x + 50, y-20
        self.sx, self.sy = x, y-20
        self.dx, self.dy = 1400, y-10
        self.time = 0
        self.frame = 0

    def draw(self):
        self.image.clip_draw(473, 380 + int(self.frame) * 52, 200, 50, self.x, self.y, 100, 25)

    def update(self):   # 스플라인 곡선 그리기
        self.x = (1 - self.time / 100)*(1 - self.time / 100)*self.sx + 2*(1 - self.time / 100)*(self.time / 100)*(self.sx + self.dx - 1800) + (self.time / 100)*(self.time / 100)*self.dx
        self.y = (1 - self.time / 100)*(1 - self.time / 100)*self.sy + 2*(1 - self.time / 100)*(self.time / 100)*(self.sy + self.dy-500) + (self.time / 100)*(self.time / 100)*self.dy
        self.time += 1
        self.frame = 1+(self.frame + player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time) % 3

        if self.x > 1400 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10   #위치 좌표 받아오기
