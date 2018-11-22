import random
import json
import os

from pico2d import *
import game_framework
import game_world

from enemy import Enemy
from player import Player
from sky import Sky
from bullet import P_Bullet

name = "MainState"

boy = None
pbullet = []

def enter():
    global player
    player = Player()
    sky = Sky()

    global enemy
    enemy = Enemy()


    game_world.add_object(sky, 0)
    game_world.add_object(player, 1)
    game_world.add_object(enemy, 1)


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
        if collide(enemy, P_Bullet):
            print("COLLISION")
            pbullet.remove(P_Bullet)
    for P_Bullet in game_world.objects[1]:
        if collide(enemy, P_Bullet) and P_Bullet.state == 1:
            print("COLLISION")
            game_world.remove_object(P_Bullet)

    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






