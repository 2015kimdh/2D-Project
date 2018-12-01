from pico2d import *
import game_world
import game_framework
import random
import math
import player
from player import Player
from Enemybullet import Enmey_Bullet
import main_state

class Enemy_2:

    image = None
    sound = None

    def __init__(self, x, y, xpull, ypull, dx, dy):

        self.Type_one_starting_point_x = x
        self.Type_one_starting_point_y = y
        self.x_pull = xpull
        self.y_pull = ypull
        self.dx, self.dy = dx, dy
        if Enemy_2.image == None:
            Enemy_2.image = load_image('enemy.png')
        if Enemy_2.sound == None:
            Enemy_2.sound = load_wav('Bomb.wav')
            Enemy_2.sound.set_volume(2)
        self.time = 0
        self.x, self.y, self.velocity = self.Type_one_starting_point_x, self.Type_one_starting_point_y, 1
        self.sx, self.sy = self.x, self.y
        self.state = 2
        self.type = 2
        self.Hp = 40
        self.slice = 500
        self.frame = 0
        self.move = 0
        self.randomnum = 0

    def draw(self):
        if self.state == 2:
            self.image.clip_draw(15, 265, 120, 45, self.x, self.y,150, 100)
        elif self.state == 3:
            if int(self.frame) < 2:
                self.image.clip_draw(137, 393, 114, 100, self.x, self.y, 200, 200)
            elif int(self.frame) < 4:
                self.image.clip_draw(137, 313, 114, 77, self.x, self.y, 200, 200)
            elif int(self.frame) < 6:
                self.image.clip_draw(137, 240, 114, 57, self.x, self.y, 200, 150)
            elif int(self.frame) < 8:
                self.image.clip_draw(137, 80, 114, 80, self.x, self.y, 200, 150)
                game_world.remove_object(self)
            self.frame = (self.frame + player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time) % 8

        draw_rectangle(*self.get_bb())

    def update(self):
        if self.time < self.slice:
            if self.move == 0:
                self.x = (1 - self.time / self.slice) * (1 - self.time / self.slice) * self.sx + 2 * (1 - self.time / self.slice) * (self.time / self.slice) * (self.sx + self.dx + self.x_pull) + (self.time / self.slice) * (self.time / self.slice) * self.dx
                self.y = (1 - self.time / self.slice) * (1 - self.time / self.slice) * self.sy + 2 * (1 - self.time / self.slice) * (self.time / self.slice) * (self.sy + self.dy + self.y_pull) + (self.time / self.slice) * (self.time / self.slice) * self.dy
            elif self.move == 1 and self.time % 50 < 2:
                if self.x < 1550:
                    self.randomnumx = random.randint(-3, 3)
                elif self.x > 1550:
                    self.randomnumx = random.randint(-3, -1)
                if self.y < 800 and self.y > 50:
                    self.randomnumy = random.randint(-3, 3)
                elif self.y > 800:
                    self.randomnumy = random.randint(-3, -1)
                elif self.y < 50:
                    self.randomnumy = random.randint(1, 3)
            if self.move == 1:
                self.x += (player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time) * self.randomnumx
                self.y += (player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time) * self.randomnumy
            self.time += (player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time) * 3
        if self.time > self.slice:
            self.time = 0
            self.move = 1
        if self.Hp == 0:
            self.state = 3
        if self.time % 120 < 2:
            for i in range(5):
                self.fire_bullet(-(i * 30))


    def fire_bullet(self, angle):
            self.angle = angle
            enemybullet = Enmey_Bullet(self.x, self.y, self.angle)
            game_world.add_object(enemybullet, 1)

    def reduce_Hp(self):
        self.Hp -= 1

    def get_bb(self):  # 충돌체크용 좌표 받아오기
        # fill here
        return self.x - 60, self.y - 100, self.x + 60, self.y + 100
