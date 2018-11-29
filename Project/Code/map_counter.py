import main_state
import game_world
from enemy_1 import Enemy_1

class Mapcounter:

    def __init__(self):
        self.counter = 0
        self.phase = 1
        self.spawntimer = 0
        self.type1_counter = 0

    def draw(self):
        pass

    def update(self):
        self.spawntimer += 1

    def spawn_enemy(self):
        if self.spawntimer % 30 == 0 and self.spawntimer < 500:
            if self.phase == 0 and self.type1_counter < 10:
                enemy = Enemy_1(1200, 1000, 500, -200, 0, -200)
                game_world.add_object(enemy, 1)
                enemy = Enemy_1(1200, -200, 500, 200, 0, 800)
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
            elif self.phase == 1 and self.type1_counter < 10:
                enemy = Enemy_1(1800, 200, 500, 200, 0, 0)
                game_world.add_object(enemy, 1)
                enemy = Enemy_1(1800, 600, 0, -500, 0, 600)
                game_world.add_object(enemy, 1)
                self.type1_counter += 2
        if self.spawntimer == 1000:
            self.spawntimer = 0
            self.phase = 1
        self.update()