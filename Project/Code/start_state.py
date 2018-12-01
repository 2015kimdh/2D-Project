import game_framework
from pico2d import *
import title_state

name = "StartState"
image = None
image1 = None
logo_time = 0.0


def enter():
    global image
    image = load_image('AceCombat7-25.png')

    global  image1
    image1 = load_image('black.png')


def exit():
    global image
    del(image)

    global image1
    del (image1)


def update():
    global logo_time

    if(logo_time > 3.0):
        logo_time = 0

        #game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    global image1
    clear_canvas()
    if logo_time < 1.0:
        image.opacify(logo_time)
    elif logo_time > 2.0 and logo_time < 3.0:
        image.opacify(3.0-logo_time)
    image1.clip_draw(0, 0, 100, 100, 800, 400, 1600, 800)
    image.clip_draw(0, 0, 2560, 1600, 800, 400, 1600, 800)

    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




