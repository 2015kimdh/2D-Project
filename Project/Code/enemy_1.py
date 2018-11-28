from pico2d import *
import game_world
import random

class Enemy_1:

    image = None
    sound = None

    def __init__(self):

        self.Type_one_starting_point_x = 1200
        self.Type_one_starting_point_y = -300
        if Enemy_1.image == None:
            Enemy_1.image = load_image('enemy.png')
            self.time = 0
            self.x, self.y, self.velocity = self.Type_one_starting_point_x, self.Type_one_starting_point_y, 1
            self.sx, self.sy = self.x, self.y
            self.dx, self.dy = self.x - 1200, self.y + 1200
            self.state = 2
            self.Hp = 2
            self.slice = 300
            self.x_pull = 500
            self.y_pull = 200


    def draw(self):
        self.image.clip_draw(37, 432, 67, 32, self.x, self.y,60, 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x = (1 - self.time / self.slice) * (1 - self.time / self.slice) * self.sx + 2 * (1 - self.time / self.slice) * (self.time / self.slice) * (self.sx + self.dx+self.x_pull) + (self.time / self.slice) * (self.time / self.slice) * self.dx
        self.y = (1 - self.time / self.slice) * (1 - self.time / self.slice) * self.sy + 2 * (1 - self.time / self.slice) * (self.time / self.slice) * (self.sy + self.dy + self.y_pull) + (self.time / self.slice) * (self.time / self.slice) * self.dy
        self.time += 1
        if self.time == self.slice:
            self.time = 0
        if self.hp == 0:
            self.state = 3


    def reduce_Hp(self):
        self.Hp -= 1

    def get_bb(self):  # 충돌체크용 좌표 받아오기
        # fill here
        return self.x - 30, self.y - 20, self.x + 30, self.y + 20
