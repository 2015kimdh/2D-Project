import game_framework
from pico2d import *
from bullet import P_Bullet
import random

import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 6.0)
FLY_SPEED_KMPH = 1200.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)
FLY_UP_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, PULLUP_DOWN, PULLUP_UP, PUSHDOWN_DOWN, PUSHDOWN_UP, SLEEP_TIMER, BULLET_UP, BULLET_DOWN = range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_z): BULLET_UP,
    (SDL_KEYDOWN, SDLK_z): BULLET_DOWN,
    (SDL_KEYDOWN, SDLK_UP): PULLUP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): PUSHDOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): PULLUP_UP,
    (SDL_KEYUP, SDLK_DOWN): PUSHDOWN_UP
}


# Boy States


class RunState:

    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += FLY_SPEED_PPS
        elif event == LEFT_DOWN:
            player.velocity -= FLY_SPEED_PPS
        elif event == RIGHT_UP:
            player.velocity -= FLY_SPEED_PPS
        elif event == LEFT_UP:
            player.velocity += FLY_SPEED_PPS

        if event == PULLUP_DOWN:
            player.altitude += FLY_UP_SPEED_PPS
        elif event == PUSHDOWN_DOWN:
            player.altitude -= FLY_UP_SPEED_PPS
        elif event == PULLUP_UP:
            player.altitude -= FLY_UP_SPEED_PPS
        elif event == PUSHDOWN_UP:
            player.altitude += FLY_UP_SPEED_PPS

        if event == BULLET_DOWN:
            player.armed = 1
        elif event == BULLET_UP:
            player.armed = 0

        player.dir = 1


    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        player.x += player.velocity * game_framework.frame_time
        player.y += player.altitude * game_framework.frame_time
        player.shottime = get_time()
        if player.armed == 1 and player.shottime % player.bullet_load >= 0.01:
            player.player_fire_bullet()

    @staticmethod
    def draw(player):
            player.image.clip_draw(0, int(player.frame) * 85, 370, 85, player.x, player.y, 185, 42.5)


next_state_table = {
    RunState: {PUSHDOWN_DOWN : RunState, PUSHDOWN_UP : RunState, PULLUP_DOWN : RunState, PULLUP_UP : RunState, RIGHT_UP: RunState, LEFT_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, BULLET_DOWN: RunState, BULLET_UP: RunState}
}

class Player:

    def __init__(self):
        self.x, self.y = 0+150, 800 / 2
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('jet.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.altitude = 0
        self.armed = 0
        self.frame = 0
        self.shottime = 0
        self.bullet_load = 0.015
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.gimage = load_image('animation_sheet.png')
        self.angle = 0


    def player_fire_bullet(self):
        pbullet = P_Bullet(self.x, self.y, self.dir*15)
        game_world.add_object(pbullet, 3)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

