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
        self.image.clip_draw(48, 329, 9, 9, self.x, self.y,15, 15)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += math.cos(self.angle)*(4)
        self.y += math.sin(self.angle)*(4)

        if self.x < 25 or self.x > 1600 - 25 or self.y < 0 or self.y > 800:
            game_world.remove_object(self)


    def get_bb(self):  # 충돌체크용 좌표 받아오기
        # fill here
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5
