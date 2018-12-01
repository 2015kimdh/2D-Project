import game_framework
import game_world
from pico2d import *
import main_state
import title_state

name = "TitleState"
image = None
image1 = None
stage = None

def enter():
    global image
    image = load_image('f22.png')
    global image1
    image1 = load_image('info.png')

def exit():
    global image
    del(image)
    global image1
    del (image1)


def handle_events():
    events = get_events()
    for event in events:
        global stage
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i):
                game_framework.pop_state()
            else :
                pass


def draw():
    clear_canvas()
    image.clip_draw(0, 0, 2560, 1600, 800, 400, 1600, 800)
    image1.clip_draw(0, 0, 1600, 800, 800, 400, 1600, 800)
    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass






