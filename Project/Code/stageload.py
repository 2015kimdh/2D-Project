import game_framework
from pico2d import *
import title_state
import main_state

name = "loadState"
image = None
sound = None
stage = 0
logo_time = 0.0


def enter():
    global image
    image = load_image('F_22.png')



def exit():
    global image
    del(image)

    global logo_time
    logo_time = 0

def update():
    global logo_time
    delay(0.01)
    logo_time += 0.01
    if logo_time > 3:
        global stage
        stage = 2
        game_framework.change_state(main_state)


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 1600, 800, 800, 400, 1600, 800)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




