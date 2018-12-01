import game_framework
from pico2d import *
import title_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('AceCombat7-25.png')


def exit():
    global image
    del(image)


def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 2560, 1600, 800, 400, 1600, 800)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




