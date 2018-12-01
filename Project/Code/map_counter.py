import main_state
import game_world
import game_framework
import player
from enemy_1 import Enemy_1
from enemy_2 import Enemy_2
from pico2d import *

class Mapcounter:


    def __init__(self):
        self.counter = 0
        self.phase = 0
        self.spawntimer = 0
        self.type1_counter = 0
        self.type2_counter = 0
        self.soundon = 0
        self.sound = load_music('Ace.mp3')

    def draw(self):
        pass

    def update(self):
        self.spawntimer += (player.FRAMES_PER_ACTION * player.ACTION_PER_TIME * game_framework.frame_time)*5
        if self.soundon == 0:
            self.sound.play()
            self.sound.set_volume(50)
            self.soundon += 1

    def spawn_enemy(self):
        if self.phase == 0:
            if int(self.spawntimer) % 30 == 0: #type1 spawn
                if self.type1_counter < 10 and self.spawntimer < 500:
                    enemy = Enemy_1(1200, 1000, 500, -200, 0, -200)
                    game_world.add_object(enemy, 1)
                    enemy = Enemy_1(1200, -200, 500, 200, 0, 800)
                    game_world.add_object(enemy, 1)
                    self.type1_counter += 2
                elif self.type1_counter < 10 and self.spawntimer > 500:
                    enemy = Enemy_1(1800, 200, 500, 200, 0, 0)
                    game_world.add_object(enemy, 1)
                    enemy = Enemy_1(1800, 600, 0, -500, 0, 600) #시작위치, 꺾이는 정도, 끝 위치
                    game_world.add_object(enemy, 1)
                    self.type1_counter += 2
        elif self.phase == 1:
            if int(self.spawntimer) % 30 == 0: #type1 spawn
                if self.type1_counter < 6 and self.spawntimer < 500:
                    enemy = Enemy_1(1200, 1000, 500, -200, 0, -200)
                    game_world.add_object(enemy, 1)
                    enemy = Enemy_1(1200, -200, 500, 200, 0, 800)
                    game_world.add_object(enemy, 1)
                    self.type1_counter += 2
                elif self.type1_counter < 6 and self.spawntimer > 500:
                    enemy = Enemy_1(1800, 200, 500, 200, 0, 0)
                    game_world.add_object(enemy, 1)
                    enemy = Enemy_1(1800, 600, 0, -500, 0, 600) #시작위치, 꺾이는 정도, 끝 위치
                    game_world.add_object(enemy, 1)
                    self.type1_counter += 2
            if self.type2_counter < 2 and self.spawntimer < 150: #type2 spawn
                enemy = Enemy_2(1700, 550, -500, 0, 1400, 550)
                game_world.add_object(enemy, 1)
                enemy = Enemy_2(1700, 200, -500, 0, 1400, 350)
                game_world.add_object(enemy, 1)
                enemy = Enemy_2(1700, 350, -500, 0, 1400, 200)
                game_world.add_object(enemy, 1)
                self.type2_counter += 3
        elif self.phase == 2:
            if int(self.spawntimer) % 30 == 0: #type1 spawn
                if self.type1_counter < 6 and self.spawntimer < 500:
                    enemy = Enemy_1(1200, 1000, 500, -200, 0, -200)
                    game_world.add_object(enemy, 1)
                    enemy = Enemy_1(1200, -200, 500, 200, 0, 800)
                    game_world.add_object(enemy, 1)
                    self.type1_counter += 2
                elif self.type1_counter < 6 and self.spawntimer > 500:
                    enemy = Enemy_1(1800, 200, 500, 200, 0, 0)
                    game_world.add_object(enemy, 1)
                    enemy = Enemy_1(1800, 600, 0, -500, 0, 600) #시작위치, 꺾이는 정도, 끝 위치
                    game_world.add_object(enemy, 1)
                    self.type1_counter += 2
            if self.type2_counter < 3 and int(self.spawntimer) % 350:
                enemy = Enemy_2(1700, 700, -500, 0, 1400, 550)
                game_world.add_object(enemy, 1)
                enemy = Enemy_2(1700, 200, -500, 0, 1400, 350)
                game_world.add_object(enemy, 1)
                enemy = Enemy_2(1700, 0, -500, -500, 1400, 200)
                game_world.add_object(enemy, 1)
                self.type2_counter += 3



        if self.spawntimer > 750:
            self.spawntimer = 0
        if self.counter > 40:
            self.phase = 1
        if self.counter > 120:
            self.phase = 2
        if self.counter > 180:
            self.phase = 3
        self.update()