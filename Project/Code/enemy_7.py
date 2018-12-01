from pico2d import *
import game_world
import game_framework
import random
import math
import player
import main_state
from player import Player
from Enemybullet import Enmey_Bullet
from enemy_1 import Enemy_1


PIXEL_PER_METER = (10.0 / 0.6) # 10 pix 60cm
FLY_SPEED_KMPH = 120.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)
FLY_UP_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

class Enemy_7:

    image = None
    sound = None

    def __init__(self, x, y, xpull, ypull, dx, dy):

        self.Type_one_starting_point_x = x
        self.Type_one_starting_point_y = y
        self.x_pull = xpull
        self.y_pull = ypull
        self.dx, self.dy = dx, dy
        if Enemy_7.image == None:
            Enemy_7.image = load_image('enemy.png')
        if Enemy_7.sound == None:
            Enemy_7.sound = load_wav('Bomb.wav')
            Enemy_7.sound.set_volume(20)
        self.time = 0
        self.x, self.y, self.velocity = self.Type_one_starting_point_x, self.Type_one_starting_point_y, 1
        self.sx, self.sy = self.x, self.y
        self.state = 2
        self.type = 4
        self.Hp = 1100
        self.slice = 580
        self.frame = 0
        self.move = 0
        self.randomnum = 0
        self.bullet_phase = 0

    def draw(self):
        if self.state == 2:
            self.image.clip_draw(269, 80, 209, 90, self.x, self.y,400, 250)
        elif self.state == 3:
            if int(self.frame) < 6:
                self.image.clip_draw(137, 393, 114, 100, self.x, self.y, 400, 250)
                self.image.clip_draw(137, 393, 114, 100, self.x-100, self.y+100, 400, 250)
                self.image.clip_draw(137, 393, 114, 100, self.x + 100, self.y - 100, 400, 250)
                self.image.clip_draw(137, 393, 114, 100, self.x + 100, self.y - 100, 400, 250)
                self.image.clip_draw(137, 393, 114, 100, self.x - 100, self.y + 100, 400, 250)
                if int(self.frame) == 0:
                    Enemy_7.sound.play()
            elif int(self.frame) < 12:
                self.image.clip_draw(137, 313, 114, 77, self.x, self.y, 400, 250)
                self.image.clip_draw(137, 313, 114, 77, self.x - 100, self.y + 100, 400, 250)
                self.image.clip_draw(137, 313, 114, 77, self.x + 100, self.y - 100, 400, 250)
                self.image.clip_draw(137, 313, 114, 77, self.x + 100, self.y - 100, 400, 250)
                self.image.clip_draw(137, 313, 114, 77, self.x - 100, self.y + 100, 400, 250)
            elif int(self.frame) < 18:
                self.image.clip_draw(137, 240, 114, 57, self.x, self.y, 400, 250)
                self.image.clip_draw(137, 240, 114, 57, self.x - 100, self.y + 100, 400, 250)
                self.image.clip_draw(137, 240, 114, 57, self.x + 100, self.y - 100, 400, 250)
                self.image.clip_draw(137, 240, 114, 57, self.x + 100, self.y - 100, 400, 250)
                self.image.clip_draw(137, 240, 114, 57, self.x - 100, self.y + 100, 400, 250)
                if int(self.frame) == 12:
                    Enemy_7.sound.play()
            elif int(self.frame) < 24:
                self.image.clip_draw(137, 80, 114, 80, self.x, self.y, 300, 190)
                self.image.clip_draw(137, 80, 114, 80, self.x - 100, self.y + 100, 300, 190)
                self.image.clip_draw(137, 80, 114, 80, self.x + 100, self.y - 100, 300, 190)
                self.image.clip_draw(137, 80, 114, 80, self.x + 100, self.y - 100, 300, 190)
                self.image.clip_draw(137, 80, 114, 80, self.x - 100, self.y + 100, 300, 190)
            elif int(self.frame) < 30:
                self.image.clip_draw(137, 80, 114, 80, self.x, self.y, 170, 130)
                self.image.clip_draw(137, 80, 114, 80, self.x - 50, self.y + 50, 170, 130)
                self.image.clip_draw(137, 80, 114, 80, self.x + 50, self.y - 50, 170, 130)
                self.image.clip_draw(137, 80, 114, 80, self.x + 50, self.y - 50, 170, 130)
                self.image.clip_draw(137, 80, 114, 80, self.x - 50, self.y + 50, 170, 130)
                if int(self.frame) == 24:
                    Enemy_7.sound.play()
            elif int(self.frame) >= 30:
                game_world.remove_object(self)
            self.frame = (self.frame + player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time) % 31
        if main_state.player.rect == 0:
            draw_rectangle(*self.get_bb())

    def update(self):
        if self.time < self.slice:
            if self.move == 0:
                self.x = (1 - self.time / self.slice) * (1 - self.time / self.slice) * self.sx + 2 * (1 - self.time / self.slice) * (self.time / self.slice) * (self.sx + self.dx + self.x_pull) + (self.time / self.slice) * (self.time / self.slice) * self.dx
                self.y = (1 - self.time / self.slice) * (1 - self.time / self.slice) * self.sy + 2 * (1 - self.time / self.slice) * (self.time / self.slice) * (self.sy + self.dy + self.y_pull) + (self.time / self.slice) * (self.time / self.slice) * self.dy
            elif self.move == 1 and self.time % 50 < 2:
                if self.x < 1450 and self.x > 1000:
                    self.randomnumx = random.randint(-1, 1)
                elif self.x < 1000:
                    self.randomnumx = 1
                elif self.x > 1450:
                    self.randomnumx = -1
                if self.y < 600 and self.y > 250:
                    self.randomnumy = random.randint(-1, 1)
                elif self.y > 600:
                    self.randomnumy = -1
                elif self.y < 250:
                    self.randomnumy = 1
            if self.move == 1:
                self.x += FLY_SPEED_PPS/12 * game_framework.frame_time * self.randomnumx
                self.y += FLY_SPEED_PPS/12 * game_framework.frame_time * self.randomnumy
            self.time += (player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time) * 3
        if self.time > self.slice:
            self.time = 0
            self.move = 1
        if self.Hp == 0:
            self.state = 3
        if self.Hp > 900:
            self.bullet_phase0()
        elif self.Hp < 900 and self.Hp > 700:
            self.bullet_phase1()
        elif self.Hp < 700 and self.Hp > 400:
            self.bullet_phase2()
        elif self.Hp < 400:
            self.bullet_phase3()

    def fire_bullet(self, angle):
            self.angle = angle
            enemybullet = Enmey_Bullet(self.x, self.y, self.angle)
            game_world.add_object(enemybullet, 1)

    def reduce_Hp(self):
        self.Hp -= 1

    def get_bb(self):  # 충돌체크용 좌표 받아오기
        # fill here
        return self.x - PIXEL_PER_METER * 7, self.y - PIXEL_PER_METER * 6, self.x + PIXEL_PER_METER * 7, self.y + PIXEL_PER_METER * 6

    def bullet_phase0(self):
        if self.time % 40 < 13:
            radian = ((self.time % 13) * 30) / 180 * math.pi
            self.fire_bullet(radian)
        if int(self.time % 50) == 0:
            Enemy_1.fire_bullet(self)
    def bullet_phase1(self):
        if self.time % 20 < 9:
            radian = ((self.time % 9) * 45) / 180 * math.pi
            self.fire_bullet(radian)
        if int(self.time % 10) == 0 and int(self.time) < 250:
            radian = ((self.time % 90)+150) / 180 * math.pi
            self.fire_bullet(radian)
        if int(self.time % 30) == 0:
            Enemy_1.fire_bullet(self)
    def bullet_phase2(self):
        if int(self.time % 20) == 0 and int(self.time) < 400:
            radian = ((self.time % 90)) / 180 * math.pi
            self.fire_bullet(radian)
            radian = ((self.time % 90)+90) / 180 * math.pi
            self.fire_bullet(radian)
            radian = (-(self.time % 90) + 180) / 180 * math.pi
            self.fire_bullet(radian)
            radian = ((self.time % 90) + 270) / 180 * math.pi
            self.fire_bullet(radian)
        if int(self.time % 5) == 0 and int(self.time) > 300:
            radian = ((self.time % 120)+120) / 180 * math.pi
            self.fire_bullet(radian)
        if int(self.time % 20) == 0:
            Enemy_1.fire_bullet(self)
    def bullet_phase3(self):
        if self.time % 20 < 9:
            radian = ((self.time % 9) * 45) / 180 * math.pi
            self.fire_bullet(radian)
        if int(self.time % 10) == 0 and int(self.time) < 250:
            radian = ((self.time % 90)+150) / 180 * math.pi
            self.fire_bullet(radian)
        if int(self.time % 20) == 0:
            self.fire_bullet_boss()

    def fire_bullet_boss(self):
        anglex = main_state.player.x - self.x;
        angley = main_state.player.y - self.y;
        if self.time % 120 < 20:
            self.angle = math.atan2(angley,anglex) - (self.time % 11) + 11/2
        enemybullet = Enmey_Bullet(self.x, self.y, self.angle)
        game_world.add_object(enemybullet, 1)