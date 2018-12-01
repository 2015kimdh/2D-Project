import game_framework
import game_world
from pico2d import *
import main_state

name = "TitleState"
image = None
sound = None
stage = None

def enter():
    global image
    image = load_image('f22.png')

    global sound
    sound = load_music('Ace_Combat.mp3')
    sound.set_volume(40)
    sound.repeat_play()


def exit():
    global image
    del(image)

    global sound
    sound.pause()
    del(sound)


def handle_events():
    events = get_events()
    for event in events:
        global stage
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
                stage = 1
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                stage = 2
                game_framework.change_state(main_state)
            else :
                pass


def draw():
    clear_canvas()
    image.clip_draw(0, 0, 1920, 1080, 800, 400, 1600, 800)
    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass






