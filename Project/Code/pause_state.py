import game_framework
from pico2d import *
import main_state

name = "TitleState"
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


def draw():
    global timer
    clear_canvas()
    if timer < 200 :
        image.draw(400, 300)
    timer += 1
    if timer == 400 :
        timer = 0
    main_state.grass.draw()
    main_state.boy.draw()
    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass






