import main_state
import game_world
from enemy_1 import Enemy_1

class Mapcounter:

    def __init__(self):
        self.counter = 0
        self.phase = 0
        self.spawntimer = 0


    def update(self):
        self.spawntimer += 1

    def spawn_enemy(self):
        if self.spawntimer % 10 == 0:
            if self.phase == 0:
                game_world.add_object(Enemy_1, 1)
            elif self.phase == 1:
                game_world.add_object(Enemy_1, 1)
            if self.spawntimer == 1000:
                self.spawntimer = 0
                self.phase = 1