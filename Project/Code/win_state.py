import game_framework
from pico2d import *
import title_state
import main_state

name = "loadState"
image = None
image1 = None
image2 = None
logo_time = 0.0


def enter():
    global image
    image = load_image('win.png')

    global image1
    image1 = load_image('black.png')

    global image2
    image2 = load_image('youwon.png')

def exit():
    global image
    del(image)

    global image1
    del (image1)

    global image2
    del (image2)

    global logo_time
    logo_time = 0

def update():
    global logo_time
    if logo_time < 1.0:
        image1.opacify(logo_time * 0.02)
        image2.opacify(logo_time)
    delay(0.01)
    logo_time += 0.01
    if logo_time > 5:
        game_framework.change_state(title_state)

def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 1600, 800, 800, 400, 1600, 800)
    image1.clip_draw(0, 0, 1600, 800, 800, 400, 1600, 800)
    image2.clip_draw(0, 0, 1600, 800, 800, 400, 1600, 800)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




