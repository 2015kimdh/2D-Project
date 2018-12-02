from pico2d import *
import game_world
import game_framework
import main_state
import player

PIXEL_PER_METER = (10.0 / 0.6) # 10 pix 60cm
FLY_SPEED_KMPH = 120.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)
FLY_UP_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

class Enmey_Bullet:
    image = None
    def __init__(self, x, y, angle):
        if Enmey_Bullet.image == None:
            Enmey_Bullet.image = load_image('enemy.png')
        self.x, self.y, self.angle = x, y, angle
        self.state = 5

    def draw(self):
        self.image.clip_draw(48, 329, 9, 9, self.x, self.y,25, 25)
        if main_state.player.rect == 0:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.x += math.cos(self.angle)*FLY_SPEED_PPS/4 * game_framework.frame_time
        self.y += math.sin(self.angle)*FLY_SPEED_PPS/4 * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25 or self.y < 0 or self.y > 800:
            game_world.remove_object(self)


    def get_bb(self):  # 충돌체크용 좌표 받아오기
        # fill here
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5
