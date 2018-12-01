import main_state
import game_world
import game_framework
import player
from enemy_1 import Enemy_1
from enemy_2 import Enemy_2
from enemy_3 import Enemy_3
from enemy_4 import Enemy_4
from enemy_5 import Enemy_5
from enemy_6 import Enemy_6
from enemy_7 import Enemy_7
from pico2d import *

class Mapcounter:

    image = None
    def __init__(self, stage):
        if Mapcounter.image == None:
            Mapcounter.image = load_image('gage.png')
        self.stage = stage
        self.counter = 0
        self.phase = 0
        self.spawntimer = 0
        self.type1_counter = 0
        self.type2_counter = 0
        self.type3_counter = 0
        self.type4_counter = 0
        self.soundon = 0
        self.sound = load_music('Ace.mp3')
        self.font = load_font('ENCR10B.TTF', 16)
        self.state = 80

    def draw(self):
        self.image.clip_draw(0, 45, 100, 56, 100, 100, 160, 30)
        self.image.clip_draw(0, 0, 100, 44, 100 - 80+self.counter/2, 100, self.counter, 30)

    def update(self):
        self.spawntimer += (player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time)*5
        if self.soundon == 0:
            self.sound.repeat_play()
            self.sound.set_volume(50)
            self.soundon += 1

    def stage2(self):
        self.spawn_enemy2()

    def spawn_enemy2(self):
        if self.phase == 0:
            self.stage2_phase0()
        elif self.phase == 1:
            self.stage2_phase1()
        elif self.phase == 2:
            self.stage2_phase2()
        elif self.phase == 3:
            self.stage2_phase3()
        elif self.phase == 4:
            self.stage2_phase4()

        if self.spawntimer > 750:
            self.spawntimer = 0
        if self.counter > 40:
            self.phase = 1
        if self.counter > 110:
            self.phase = 2
        if self.counter > 160:
            self.phase = 3
        self.update()

    def stage2_phase0(self):
        if int(self.spawntimer) % 30 == 0:  # type1 spawn
            if self.type1_counter < 8 and self.spawntimer < 500:
                enemy = Enemy_4(1200, 1000, 500, -500, 0, -200)
                game_world.add_object(enemy, 1)
                enemy = Enemy_4(1200, -200, 500, 500, 0, 800)
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
            elif self.type1_counter < 8 and self.spawntimer > 500:
                enemy = Enemy_4(1800, 200, 500, 300, 0, 0)
                game_world.add_object(enemy, 1)
                enemy = Enemy_4(1800, 600, 0, -500, -300, 600)  # 시작위치, 꺾이는 정도, 끝 위치
                game_world.add_object(enemy, 1)
                self.type1_counter += 2

    def stage2_phase1(self):
        if int(self.spawntimer) % 30 == 0:  # type1 spawn
            if self.type1_counter < 5 and self.spawntimer < 500:
                enemy = Enemy_4(1200, 1000, 500, -500, 0, -200)
                game_world.add_object(enemy, 1)
                enemy = Enemy_4(1200, -200, 500, 200, 0, 800)
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
            elif self.type1_counter < 5 and self.spawntimer > 500:
                enemy = Enemy_4(1800, 200, 500, 300, 0, 0)
                game_world.add_object(enemy, 1)
                enemy = Enemy_4(1800, 600, 0, -500, 0, 600)  # 시작위치, 꺾이는 정도, 끝 위치
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
        if self.type2_counter < 2 and self.spawntimer < 250:  # type2 spawn
            enemy = Enemy_5(1700, 550, -500, 0, 1400, 550)
            game_world.add_object(enemy, 1)
            enemy = Enemy_5(1700, 200, -500, 0, 1400, 350)
            game_world.add_object(enemy, 1)
            self.type2_counter += 2

    def stage2_phase2(self):
        if int(self.spawntimer) % 30 == 0:  # type1 spawn
            if self.type1_counter < 6 and self.spawntimer < 500:
                enemy = Enemy_4(1200, 1000, 500, -200, 0, -200)
                game_world.add_object(enemy, 1)
                enemy = Enemy_4(1200, -200, 500, 200, 0, 800)
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
            elif self.type1_counter < 6 and self.spawntimer > 500:
                enemy = Enemy_4(1800, 200, 500, 200, 0, 0)
                game_world.add_object(enemy, 1)
                enemy = Enemy_4(1800, 600, 0, -500, 0, 600)  # 시작위치, 꺾이는 정도, 끝 위치
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
        if self.type2_counter < 2 and int(self.spawntimer) % 200 == 0:
            enemy = Enemy_5(1700, 700, -500, 0, 1400, 550)
            game_world.add_object(enemy, 1)
            enemy = Enemy_5(1700, 200, -500, 0, 1400, 350)
            game_world.add_object(enemy, 1)
            enemy = Enemy_5(1700, 0, -500, -500, 1400, 200)
            game_world.add_object(enemy, 1)
            self.type2_counter += 3

    def stage2_phase3(self):
        if int(self.spawntimer) % 30 == 0:  # type1 spawn
            if self.type1_counter < 2 and self.spawntimer < 500:
                enemy = Enemy_4(1200, 1000, 500, -200, 0, -200)
                game_world.add_object(enemy, 1)
                enemy = Enemy_4(1200, -200, 500, 200, 0, 800)
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
            elif self.type1_counter < 2 and self.spawntimer > 500:
                enemy = Enemy_4(1800, 200, 500, 200, 0, 0)
                game_world.add_object(enemy, 1)
                enemy = Enemy_4(1800, 600, 0, -500, 0, 600)  # 시작위치, 꺾이는 정도, 끝 위치
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
        if self.type3_counter < 1 and int(self.spawntimer) % 350 == 0:
            enemy = Enemy_6(1700, 200, -500, 0, 1400, 350)
            game_world.add_object(enemy, 1)
            self.type3_counter += 1

    def stage2_phase4(self):
        if self.type4_counter < 1 and int(self.spawntimer) % 350 == 0:
            enemy = Enemy_7(1900, 200, -500, 0, 1500, 350)
            game_world.add_object(enemy, 1)
            self.type4_counter += 1

    def stage1(self):
        self.spawn_enemy1()


    def spawn_enemy1(self):
        if self.phase == 0:
            self.phase0()
        elif self.phase == 1:
            self.phase1()
        elif self.phase == 2:
            self.phase2()
        elif self.phase == 3:
            self.phase3()

        if self.spawntimer > 750:
            self.spawntimer = 0
        if self.counter > 40:
            self.phase = 1
        if self.counter > 110:
            self.phase = 2
        if self.counter > 160:
            self.phase = 3
        self.update()


    def phase0(self):
        if int(self.spawntimer) % 30 == 0:  # type1 spawn
            if self.type1_counter < 10 and self.spawntimer < 500:
                enemy = Enemy_1(1200, 1000, 500, -200, 0, -200)
                game_world.add_object(enemy, 1)
                enemy = Enemy_1(1200, -200, 500, 200, 0, 800)
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
            elif self.type1_counter < 10 and self.spawntimer > 500:
                enemy = Enemy_1(1800, 200, 500, 200, 0, 0)
                game_world.add_object(enemy, 1)
                enemy = Enemy_1(1800, 600, 0, -500, 0, 600)  # 시작위치, 꺾이는 정도, 끝 위치
                game_world.add_object(enemy, 1)
                self.type1_counter += 2

    def phase1(self):
        if int(self.spawntimer) % 30 == 0:  # type1 spawn
            if self.type1_counter < 6 and self.spawntimer < 500:
                enemy = Enemy_1(1200, 1000, 500, -200, 0, -200)
                game_world.add_object(enemy, 1)
                enemy = Enemy_1(1200, -200, 500, 200, 0, 800)
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
            elif self.type1_counter < 6 and self.spawntimer > 500:
                enemy = Enemy_1(1800, 200, 500, 200, 0, 0)
                game_world.add_object(enemy, 1)
                enemy = Enemy_1(1800, 600, 0, -500, 0, 600)  # 시작위치, 꺾이는 정도, 끝 위치
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
        if self.type2_counter < 2 and self.spawntimer < 150:  # type2 spawn
            enemy = Enemy_2(1700, 550, -500, 0, 1400, 550)
            game_world.add_object(enemy, 1)
            enemy = Enemy_2(1700, 200, -500, 0, 1400, 350)
            game_world.add_object(enemy, 1)
            enemy = Enemy_2(1700, 350, -500, 0, 1400, 200)
            game_world.add_object(enemy, 1)
            self.type2_counter += 3

    def phase2(self):
        if int(self.spawntimer) % 30 == 0:  # type1 spawn
            if self.type1_counter < 6 and self.spawntimer < 500:
                enemy = Enemy_1(1200, 1000, 500, -200, 0, -200)
                game_world.add_object(enemy, 1)
                enemy = Enemy_1(1200, -200, 500, 200, 0, 800)
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
            elif self.type1_counter < 6 and self.spawntimer > 500:
                enemy = Enemy_1(1800, 200, 500, 200, 0, 0)
                game_world.add_object(enemy, 1)
                enemy = Enemy_1(1800, 600, 0, -500, 0, 600)  # 시작위치, 꺾이는 정도, 끝 위치
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
        if self.type2_counter < 3 and int(self.spawntimer) % 350 == 0:
            enemy = Enemy_2(1700, 700, -500, 0, 1400, 550)
            game_world.add_object(enemy, 1)
            enemy = Enemy_2(1700, 200, -500, 0, 1400, 350)
            game_world.add_object(enemy, 1)
            enemy = Enemy_2(1700, 0, -500, -500, 1400, 200)
            game_world.add_object(enemy, 1)
            self.type2_counter += 3

    def phase3(self):
        if self.type3_counter < 1 and int(self.spawntimer) % 350 == 0:
            enemy = Enemy_3(1700, 200, -500, 0, 1400, 350)
            game_world.add_object(enemy, 1)
            self.type3_counter += 1