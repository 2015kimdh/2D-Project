import main_state
import game_world
from enemy_1 import Enemy_1
from pico2d import *

class Mapcounter:


    def __init__(self):
        self.counter = 0
        self.phase = 1
        self.spawntimer = 0
        self.type1_counter = 0
        self.soundon = 0
        self.sound = load_music('Ace.mp3')

    def draw(self):
        pass

    def update(self):
        self.spawntimer += 1
        if self.soundon == 0:
            self.sound.play()
            self.sound.set_volume(50)
            self.soundon += 1

    def spawn_enemy(self):
        if self.spawntimer % 30 == 0: #type1 spawn
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

        if self.spawntimer % 30 == 0 and self.spawntimer < 500: #type2 spawn
            pass

        if self.spawntimer == 1000:
            self.spawntimer = 0
            self.phase = 1
        self.update()