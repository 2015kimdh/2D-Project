import game_framework
from pico2d import *
import main_state
import title_state

name = "PauseState"
image = None
global timer
timer = 0

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)


def draw():
    clear_canvas()
    main_state.player.draw()
    main_state.sky.draw()
    image.clip_draw(0, 0, 1600, 800, 800, 400, 1600, 800)
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass






