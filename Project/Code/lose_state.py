import game_framework
from pico2d import *
import title_state

name = "StartState"
image = None
sound = None
logo_time = 0.0


def enter():
    global image
    image = load_image('die.png')

    global image1
    image1 = load_image('black.png')

    global sound
    sound = load_music('Died.mp3')
    sound.play(1)


def exit():
    global image
    del(image)

    global logo_time
    logo_time = 0

    global image1
    del (image1)


def update():
    global logo_time
    delay(0.01)
    logo_time += 0.01
    if logo_time > 5:
        game_framework.push_state(title_state)

def draw():
    global image
    global image1
    clear_canvas()
    if logo_time < 1.0:
        image.opacify(logo_time)
    image1.clip_draw(0, 0, 100, 100, 800, 400, 1600, 800)
    image.clip_draw(0, 0, 2560, 1600, 800, 400, 1600, 800)

    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




