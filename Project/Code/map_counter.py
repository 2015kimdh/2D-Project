import main_state
import game_world
from enemy_1 import Enemy_1

class Mapcounter:

    def __init__(self):
        self.counter = 0
        self.phase = 0
        self.spawntimer = 0

    def draw(self):
        pass

    def update(self):
        self.spawntimer += 1

    def spawn_enemy(self):
        if self.spawntimer % 100 == 0:
            enemy = Enemy_1(1200, -400)
            if self.phase == 0:
                main_state.enemy1.append(enemy)
                game_world.add_object(enemy, 1)
            elif self.phase == 1:
                main_state.enemy1.append(enemy)
                game_world.add_object(enemy, 1)
            if self.spawntimer == 1000:
                self.spawntimer = 0
                self.phase = 1
        self.update()