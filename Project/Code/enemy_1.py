from pico2d import *
import game_world
import random
import math
from player import Player
from Enemybullet import Enmey_Bullet
import main_state

class Enemy_1:

    image = None
    sound = None

    def __init__(self, x, y, xpull, ypull, dx, dy):

        self.Type_one_starting_point_x = x
        self.Type_one_starting_point_y = y
        self.x_pull = xpull
        self.y_pull = ypull
        self.dx, self.dy = dx, dy
        if Enemy_1.image == None:
            Enemy_1.image = load_image('enemy.png')
        self.time = 0
        self.x, self.y, self.velocity = self.Type_one_starting_point_x, self.Type_one_starting_point_y, 1
        self.sx, self.sy = self.x, self.y
        self.state = 2
        self.Hp = 3
        self.slice = 300

    def draw(self):
        self.image.clip_draw(37, 432, 67, 32, self.x, self.y,60, 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x = (1 - self.time / self.slice) * (1 - self.time / self.slice) * self.sx + 2 * (1 - self.time / self.slice) * (self.time / self.slice) * (self.sx + self.dx+self.x_pull) + (self.time / self.slice) * (self.time / self.slice) * self.dx
        self.y = (1 - self.time / self.slice) * (1 - self.time / self.slice) * self.sy + 2 * (1 - self.time / self.slice) * (self.time / self.slice) * (self.sy + self.dy + self.y_pull) + (self.time / self.slice) * (self.time / self.slice) * self.dy
        self.time += 1
        if self.time == self.slice:
            self.time = 0
        if self.Hp == 0:
            self.state = 3
        if self.time % 120 == 0:
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
        return self.x - 30, self.y - 20, self.x + 30, self.y + 20
