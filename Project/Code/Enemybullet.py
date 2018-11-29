from pico2d import *
import game_world
import main_state
import player

class Enmey_Bullet:
    image = None
    def __init__(self, x, y, angle):
        if Enmey_Bullet.image == None:
            Enmey_Bullet.image = load_image('enemy.png')
        self.x, self.y, self.angle = x, y, angle
        self.state = 3

    def draw(self):
        self.image.clip_draw(37, 432, 67, 32, self.x, self.y,20, 20)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += math.cos(self.angle)*(5)
        self.y += math.sin(self.angle)*(5)

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)


    def get_bb(self):  # 충돌체크용 좌표 받아오기
        # fill here
        return self.x - 20, self.y - 10, self.x + 30, self.y + 10
