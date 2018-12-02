import random
import json
import os
import title_state
import pause_state
from pico2d import *
import game_framework
import game_world
import stageload

from enemy_1 import Enemy_1
from player import Player
from sky import Sky
from bullet import P_Bullet
from map_counter import Mapcounter
import stageload

name = "MainState"

mainstage = None

def enter():
    global  mainstage
    mainstage = title_state.stage
    global player
    player = Player()
    global sky
    if stageload.stage == 2:
        sky = Sky(stageload.stage)
    else:
        sky = Sky(mainstage)


    global map_counter
    if stageload.stage == 2:
        map_counter = Mapcounter(stageload.stage)
    else:
        map_counter = Mapcounter(mainstage)

    game_world.add_object(sky, 0)
    game_world.add_object(player, 1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            player.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for P_Bullet in game_world.objects[1]:
        for Enemy_1 in game_world.objects[1]:
            if collide(Enemy_1, P_Bullet) and Enemy_1.state == 2 and P_Bullet.state == 1:
                game_world.remove_object(P_Bullet)
                if Enemy_1.Hp > 0:
                    Enemy_1.Hp -=1
                if Enemy_1.Hp == 0:
                    Enemy_1.state = 3
                    map_counter.counter += 1
                    if Enemy_1.type == 1:
                        map_counter.type1_counter -=1
                    if Enemy_1.type == 2:
                        map_counter.type2_counter -= 1
                    if Enemy_1.type == 3:
                        map_counter.type3_counter -= 1
                    if Enemy_1.type == 4:
                        map_counter.type4_counter -= 1
            if collide(Enemy_1, P_Bullet) and Enemy_1.state == 5 and P_Bullet.state == 0:
                game_world.remove_object(Enemy_1)
                player.state = 8
    if map_counter.stage == 1:
        Mapcounter.stage1(map_counter)
    if map_counter.stage == 2:
        Mapcounter.stage2(map_counter)



    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    Mapcounter.draw(map_counter)
    update_canvas()






