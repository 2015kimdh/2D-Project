from pico2d import *
import game_world

class Enmey_Bullet:
    image = None
    sound = None
    def __init__(self, x = 400, y = 300, velocity = -1):
        if Enmey_Bullet.image == None:
            Enmey_Bullet.image = load_image('jet.png')
        self.x, self.y, self.velocity = x + 50, y-10, velocity
        self.state = 1


    def draw(self):
        self.image.clip_draw(630, 0, 60, 20, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def get_bb(self):  # 충돌체크용 좌표 받아오기
        # fill here
        return self.x - 20, self.y - 10, self.x + 30, self.y + 10
