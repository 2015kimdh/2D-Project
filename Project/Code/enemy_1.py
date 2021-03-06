from pico2d import *
import game_world
import game_framework
import random
import math
import player
from player import Player
from Enemybullet import Enmey_Bullet
import main_state

PIXEL_PER_METER = (10.0 / 0.6) # 10 pix 60cm
FLY_SPEED_KMPH = 120.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)
FLY_UP_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

class Enemy_1:

    image = None
    sound = None

    def __init__(self, x, y, xpull, ypull, dx, dy):

        self.Type_one_starting_point_x = x
        self.Type_one_starting_point_y = y
        self.x_pull = xpull
        self.y_pull = ypull
        self.rect = 0
        self.dx, self.dy = dx, dy
        if Enemy_1.image == None:
            Enemy_1.image = load_image('enemy.png')
        self.time = 0
        self.x, self.y, self.velocity = self.Type_one_starting_point_x, self.Type_one_starting_point_y, 1
        self.sx, self.sy = self.x, self.y
        self.state = 2
        self.type = 1
        self.Hp = 3
        self.slice = 300
        self.frame = 0

    def draw(self):
        if self.state == 2:
            self.image.clip_draw(37, 432, 67, 32, self.x, self.y,60, 50)
        elif self.state == 3:
            if int(self.frame) < 2:
                self.image.clip_draw(137, 393, 114, 100, self.x, self.y, 120, 120)
            elif int(self.frame) < 4:
                self.image.clip_draw(137, 313, 114, 77, self.x, self.y, 120, 120)
            elif int(self.frame) < 6:
                self.image.clip_draw(137, 240, 114, 57, self.x, self.y, 120, 80)
            elif int(self.frame) < 8:
                self.image.clip_draw(137, 80, 114, 80, self.x, self.y, 120, 80)
                game_world.remove_object(self)
            self.frame = (self.frame + player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time) % 8
        if main_state.player.rect == 0:
            draw_rectangle(*self.get_bb())

    def update(self):
        self.x = (1 - self.time / self.slice) * (1 - self.time / self.slice) * self.sx + 2 * (1 - self.time / self.slice) * (self.time / self.slice) * (self.sx + self.dx+self.x_pull) + (self.time / self.slice) * (self.time / self.slice) * self.dx
        self.y = (1 - self.time / self.slice) * (1 - self.time / self.slice) * self.sy + 2 * (1 - self.time / self.slice) * (self.time / self.slice) * (self.sy + self.dy + self.y_pull) + (self.time / self.slice) * (self.time / self.slice) * self.dy
        self.time += (player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time) * 5
        if self.time > self.slice:
            self.time = 0
        if self.Hp == 0:
            self.state = 3
        if self.time % 120 < 2:
            self.fire_bullet()


    def fire_bullet(self):
            anglex = main_state.player.x - self.x;
            angley = main_state.player.y - self.y;
            self.angle = math.atan2(angley,anglex)
            enemybullet = Enmey_Bullet(self.x, self.y, self.angle)
            game_world.add_object(enemybullet, 1)

    def reduce_Hp(self):
        self.Hp -= 1

    def get_bb(self):  # 충돌체크용 좌표 받아오기
        # fill here
        return self.x - PIXEL_PER_METER * 1.5, self.y - PIXEL_PER_METER * 1, self.x + PIXEL_PER_METER * 1.5, self.y + PIXEL_PER_METER * 1
