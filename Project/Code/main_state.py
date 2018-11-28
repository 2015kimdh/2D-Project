import random
import json
import os

from pico2d import *
import game_framework
import game_world

from enemy_1 import Enemy_1
from player import Player
from sky import Sky
from bullet import P_Bullet
from map_counter import Mapcounter

name = "MainState"

boy = None
pbullet = []

def enter():
    global player
    player = Player()
    sky = Sky()


    global map_counter
    map_counter = Mapcounter()


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            player.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for P_Bullet in pbullet:
        if collide(Enemy_1, P_Bullet):
            print("COLLISION")
            pbullet.remove(P_Bullet)
    for P_Bullet in game_world.objects[1]:
        if collide(Enemy_1, P_Bullet) and P_Bullet.state == 1:
            print("COLLISION")
            game_world.remove_object(P_Bullet)
            if Enemy_1.state != 3:
                Enemy_1.reduce_Hp(Enemy_1)
            if Enemy_1.state == 3:
                game_world.remove_object(Enemy_1)
    Mapcounter.spawn_enemy(map_counter)


    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()






