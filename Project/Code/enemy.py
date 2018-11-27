from pico2d import *
import game_world
import random

class Enemy:

    image = None
    sound = None
    def __init__(self):
        self.Type_one_starting_point_x = 1200
        self.Type_one_starting_point_y = 400
        if Enemy.image == None:
            Enemy.image = load_image('enemy.png')
        self.identity = 1

        if self.identity == 1:
            self.x, self.y, self.velocity = self.Type_one_starting_point_x, self.Type_one_starting_point_y, 1
            self.state = 2
            self.Hp = 2


    def draw(self):
        self.image.clip_draw(37, 432, 67, 32, self.x, self.y,60, 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.identity == 1:
            self.x = (self.x % 1200) + 5
            if self.x % 300 == 0:

            self.y = (self.x % 800) + 5
            pass

    def reduce_Hp(self):
        self.Hp -= 0

    def get_bb(self):  # 충돌체크용 좌표 받아오기
        # fill here
        return self.x - 30, self.y - 20, self.x + 30, self.y + 20
